#!/usr/bin/env python3
"""Validate, draft, preview, or mass-send a Markdown WeChat article.

This script deliberately has no default side effect.  A caller must select a
mode, and the two outward-facing modes require an explicit confirmation value.
Credentials are read only from environment variables.
"""

from __future__ import annotations

import argparse
import html
import json
import mimetypes
import os
import re
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


API_ROOT = "https://api.weixin.qq.com/cgi-bin"
REPO_ROOT = Path(__file__).resolve().parent.parent
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<meta>.*?)\n---\s*\n(?P<body>.*)\Z", re.S)
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")
INLINE_CODE = re.compile(r"`([^`]+)`")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
ITALIC = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


class PublishError(RuntimeError):
    """A user-actionable validation or API error."""


@dataclass
class Article:
    path: Path
    metadata: dict[str, str]
    body: str


def repo_path(value: str, label: str) -> Path:
    candidate = (REPO_ROOT / value).resolve()
    try:
        candidate.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise PublishError(f"{label} must be inside this repository: {value}") from exc
    return candidate


def parse_front_matter(path: Path) -> Article:
    if not path.is_file():
        raise PublishError(f"Article file does not exist: {path.relative_to(REPO_ROOT)}")
    match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        raise PublishError("Article must start with YAML front matter delimited by ---.")

    metadata: dict[str, str] = {}
    for line in match.group("meta").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise PublishError(f"Unsupported front matter line: {line}")
        metadata[key.strip()] = value.strip().strip("\"'")

    for key in ("title", "status", "platform"):
        if not metadata.get(key):
            raise PublishError(f"Missing required front matter field: {key}")
    if metadata["platform"] != "wechat":
        raise PublishError("Only platform: wechat articles can be published.")
    return Article(path=path, metadata=metadata, body=match.group("body").strip())


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def render_inline(text: str, image_tokens: dict[str, str]) -> str:
    rendered = html.escape(text, quote=False)
    rendered = BOLD.sub(r"<strong>\1</strong>", rendered)
    rendered = ITALIC.sub(r"<em>\1</em>", rendered)
    rendered = INLINE_CODE.sub(r"<code>\1</code>", rendered)
    rendered = LINK.sub(r'<a href="\2">\1</a>', rendered)
    for token, tag in image_tokens.items():
        rendered = rendered.replace(html.escape(token), tag)
    return rendered


def markdown_to_html(markdown: str, image_tokens: dict[str, str], title: str) -> str:
    lines = markdown.replace("\r\n", "\n").split("\n")
    if lines and re.fullmatch(r"#\s+" + re.escape(title) + r"\s*", lines[0]):
        lines = lines[1:]

    output: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_tag: str | None = None
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(f"<p>{render_inline(' '.join(paragraph), image_tokens)}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items, list_tag
        if list_items and list_tag:
            output.append(f"<{list_tag}>" + "".join(list_items) + f"</{list_tag}>")
        list_items, list_tag = [], None

    index = 0
    while index < len(lines):
        line = lines[index]
        if line.strip().startswith("```"):
            flush_paragraph()
            flush_list()
            if in_code:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
            in_code = not in_code
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue
        if not line.strip():
            flush_paragraph()
            flush_list()
            index += 1
            continue

        if index + 1 < len(lines) and "|" in line and is_table_separator(lines[index + 1]):
            flush_paragraph()
            flush_list()
            headers = split_table_row(line)
            rows: list[list[str]] = []
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append(split_table_row(lines[index]))
                index += 1
            head = "".join(f"<th>{render_inline(cell, image_tokens)}</th>" for cell in headers)
            body = "".join(
                "<tr>" + "".join(f"<td>{render_inline(cell, image_tokens)}</td>" for cell in row) + "</tr>"
                for row in rows
            )
            output.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
            continue

        heading = re.fullmatch(r"(#{1,6})\s+(.+)", line)
        if heading:
            flush_paragraph()
            flush_list()
            level = min(len(heading.group(1)) + 1, 6)  # reserve h1 for WeChat's title
            output.append(f"<h{level}>{render_inline(heading.group(2), image_tokens)}</h{level}>")
            index += 1
            continue
        quote = re.fullmatch(r">\s?(.*)", line)
        if quote:
            flush_paragraph()
            flush_list()
            output.append(f"<blockquote><p>{render_inline(quote.group(1), image_tokens)}</p></blockquote>")
            index += 1
            continue
        unordered = re.fullmatch(r"[-*+]\s+(.+)", line)
        ordered = re.fullmatch(r"\d+[.)]\s+(.+)", line)
        if unordered or ordered:
            flush_paragraph()
            wanted_tag = "ul" if unordered else "ol"
            if list_tag and list_tag != wanted_tag:
                flush_list()
            list_tag = wanted_tag
            list_items.append(f"<li>{render_inline((unordered or ordered).group(1), image_tokens)}</li>")
            index += 1
            continue
        flush_list()
        paragraph.append(line.strip())
        index += 1

    if in_code:
        raise PublishError("Unclosed Markdown code fence.")
    flush_paragraph()
    flush_list()
    return "\n".join(output)


def api_json(url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    request = urllib.request.Request(url, method="POST" if payload is not None else "GET")
    if payload is not None:
        request.add_header("Content-Type", "application/json; charset=utf-8")
        request.data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as exc:
        raise PublishError(f"WeChat API request failed: {exc}") from exc
    if result.get("errcode", 0) != 0:
        raise PublishError(f"WeChat API error {result['errcode']}: {result.get('errmsg', 'unknown error')}")
    return result


def api_multipart(url: str, field: str, file_path: Path) -> dict[str, Any]:
    boundary = "----wenjing" + secrets.token_hex(16)
    content_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    body = b"".join(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="{field}"; filename="{file_path.name}"\r\n'.encode(),
            f"Content-Type: {content_type}\r\n\r\n".encode(),
            file_path.read_bytes(),
            f"\r\n--{boundary}--\r\n".encode(),
        ]
    )
    request = urllib.request.Request(url, data=body, method="POST")
    request.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as exc:
        raise PublishError(f"WeChat media upload failed: {exc}") from exc
    if result.get("errcode", 0) != 0:
        raise PublishError(f"WeChat media API error {result['errcode']}: {result.get('errmsg', 'unknown error')}")
    return result


def access_token() -> str:
    app_id = os.environ.get("WECHAT_APP_ID")
    app_secret = os.environ.get("WECHAT_APP_SECRET")
    if not app_id or not app_secret:
        raise PublishError("WECHAT_APP_ID and WECHAT_APP_SECRET must be configured as GitHub Secrets.")
    query = urllib.parse.urlencode(
        {"grant_type": "client_credential", "appid": app_id, "secret": app_secret}
    )
    result = api_json(f"{API_ROOT}/token?{query}")
    token = result.get("access_token")
    if not token:
        raise PublishError("WeChat did not return an access token.")
    return str(token)


def token_url(endpoint: str, token: str, **query: str) -> str:
    values = {"access_token": token, **query}
    return f"{API_ROOT}/{endpoint}?{urllib.parse.urlencode(values)}"


def require_existing_file(value: str | None, label: str) -> Path | None:
    if not value:
        return None
    path = repo_path(value, label)
    if not path.is_file():
        raise PublishError(f"{label} does not exist: {value}")
    return path


def prepare_images(markdown: str, token: str, article_path: Path) -> tuple[str, dict[str, str]]:
    tokens: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        alt, source = match.group(1), match.group(2).strip()
        if source.startswith(("http://", "https://")):
            raise PublishError(
                "Inline image URLs must be repository files so the workflow can upload them to WeChat: " + source
            )
        image_path = (article_path.parent / source).resolve()
        try:
            image_path.relative_to(REPO_ROOT)
        except ValueError as exc:
            raise PublishError(f"Inline image must be inside this repository: {source}") from exc
        if not image_path.is_file():
            raise PublishError(f"Inline image does not exist: {source}")
        response = api_multipart(token_url("media/uploadimg", token), "media", image_path)
        image_url = response.get("url")
        if not image_url:
            raise PublishError("WeChat did not return an inline image URL.")
        placeholder = f"@@WECHAT_IMAGE_{len(tokens)}@@"
        tokens[placeholder] = f'<img src="{html.escape(str(image_url), quote=True)}" alt="{html.escape(alt, quote=True)}" />'
        return placeholder

    return IMAGE.sub(replace, markdown), tokens


def preflight_markdown(article: Article) -> None:
    """Run all checks that do not require credentials or WeChat API calls."""

    def replace(match: re.Match[str]) -> str:
        source = match.group(2).strip()
        if source.startswith(("http://", "https://")):
            raise PublishError(
                "Inline image URLs must be repository files so the workflow can upload them to WeChat: " + source
            )
        image_path = (article.path.parent / source).resolve()
        try:
            image_path.relative_to(REPO_ROOT)
        except ValueError as exc:
            raise PublishError(f"Inline image must be inside this repository: {source}") from exc
        if not image_path.is_file():
            raise PublishError(f"Inline image does not exist: {source}")
        return "@@WECHAT_IMAGE_CHECK@@"

    source = IMAGE.sub(replace, article.body)
    markdown_to_html(source, {}, article.metadata["title"])


def resolve_thumbnail(args: argparse.Namespace, article: Article, token: str) -> str:
    media_id = args.thumbnail_media_id or article.metadata.get("thumb_media_id")
    if media_id:
        return media_id
    thumbnail = require_existing_file(args.thumbnail_path, "thumbnail path")
    if not thumbnail:
        raise PublishError("Provide thumbnail_media_id or thumbnail_path for draft, preview, or send.")
    response = api_multipart(token_url("material/add_material", token, type="image"), "media", thumbnail)
    media_id = response.get("media_id")
    if not media_id:
        raise PublishError("WeChat did not return a thumbnail media_id.")
    return str(media_id)


def article_payload(article: Article, token: str, args: argparse.Namespace) -> dict[str, Any]:
    source, image_tokens = prepare_images(article.body, token, article.path)
    thumbnail_id = resolve_thumbnail(args, article, token)
    return {
        "articles": [
            {
                "title": article.metadata["title"],
                "author": article.metadata.get("author", ""),
                "digest": article.metadata.get("digest", ""),
                "content": markdown_to_html(source, image_tokens, article.metadata["title"]),
                "content_source_url": article.metadata.get("content_source_url", ""),
                "thumb_media_id": thumbnail_id,
                "show_cover_pic": int(article.metadata.get("show_cover_pic", "0")),
                "need_open_comment": int(article.metadata.get("need_open_comment", "0")),
                "only_fans_can_comment": int(article.metadata.get("only_fans_can_comment", "0")),
            }
        ]
    }


def write_report(path: Path | None, report: dict[str, Any]) -> None:
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


def validate_publish_request(article: Article, args: argparse.Namespace) -> None:
    if article.metadata["status"] != "ready":
        raise PublishError("Article status must be ready before it can be drafted, previewed, or sent.")
    if args.mode == "preview":
        if args.confirmation != "PREVIEW":
            raise PublishError("Preview requires --confirmation PREVIEW.")
        if not args.preview_to:
            raise PublishError("Preview requires --preview-to (a recipient OpenID).")
    if args.mode == "send":
        expected = "SEND_TO_ALL" if args.target == "all" else "SEND_TO_TAG"
        if args.confirmation != expected:
            raise PublishError(f"Mass send to {args.target} requires --confirmation {expected}.")
        if args.target == "tag" and not args.tag_id:
            raise PublishError("Mass send to a tag requires --tag-id.")


def publish(article: Article, args: argparse.Namespace) -> dict[str, Any]:
    validate_publish_request(article, args)
    token = access_token()
    draft = api_json(token_url("draft/add", token), article_payload(article, token, args))
    media_id = str(draft.get("media_id", ""))
    if not media_id:
        raise PublishError("WeChat did not return a draft media_id.")
    report: dict[str, Any] = {"mode": args.mode, "article": str(article.path.relative_to(REPO_ROOT)), "draft_media_id": media_id}

    if args.mode == "draft":
        return report
    if args.mode == "preview":
        payload = {"touser": args.preview_to, "mpnews": {"media_id": media_id}, "msgtype": "mpnews"}
        api_json(token_url("message/mass/preview", token), payload)
        report["preview_to"] = args.preview_to
        return report

    filter_payload: dict[str, Any] = {"is_to_all": args.target == "all"}
    if args.target == "tag":
        filter_payload["tag_id"] = int(args.tag_id)
    result = api_json(
        token_url("message/mass/sendall", token),
        {
            "filter": filter_payload,
            "mpnews": {"media_id": media_id},
            "msgtype": "mpnews",
            "send_ignore_reprint": 0,
        },
    )
    report.update({key: result[key] for key in ("msg_id", "msg_data_id") if key in result})
    report["target"] = args.target
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("validate", "draft", "preview", "send"))
    parser.add_argument("--article", required=True, help="Repository-relative Markdown article path")
    parser.add_argument("--thumbnail-path", help="Repository-relative cover image to upload as permanent material")
    parser.add_argument("--thumbnail-media-id", help="Existing WeChat permanent-material media_id for the cover")
    parser.add_argument("--preview-to", help="Preview recipient OpenID")
    parser.add_argument("--target", choices=("all", "tag"), default="all")
    parser.add_argument("--tag-id", help="WeChat tag id when --target tag")
    parser.add_argument("--confirmation", default="")
    parser.add_argument("--report", help="Write a sanitized JSON report to this path")
    args = parser.parse_args()

    try:
        article = parse_front_matter(repo_path(args.article, "article path"))
        report_path = Path(args.report).resolve() if args.report else None
        if args.mode == "validate":
            preflight_markdown(article)
            write_report(
                report_path,
                {"mode": "validate", "article": str(article.path.relative_to(REPO_ROOT)), "status": "valid"},
            )
            return 0
        write_report(report_path, publish(article, args))
        return 0
    except PublishError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
