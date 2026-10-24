#!/usr/bin/env python3
"""
Batch-download public Furina PV videos from social-media URLs.

The script wraps yt-dlp, so platform support follows yt-dlp's extractors.
Typical supported sources include Bilibili, YouTube, TikTok/Douyin,
X/Twitter, Weibo, Instagram and many other public video pages.

Usage:
  python "projects/最后的借口+芙宁娜pv/tools/furina_pv_downloader.py" --url-file "projects/最后的借口+芙宁娜pv/tools/furina_pv_urls.example.txt"
  python "projects/最后的借口+芙宁娜pv/tools/furina_pv_downloader.py" "https://www.bilibili.com/video/..."
  python "projects/最后的借口+芙宁娜pv/tools/furina_pv_downloader.py" --playlist "https://www.bilibili.com/video/..."

Install dependency:
  python -m pip install -U yt-dlp
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = PROJECT_ROOT / "_temp" / "downloads"
DEFAULT_KEYWORDS = ["芙宁娜", "Furina", "Focalors", "芙卡洛斯"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Download public social-media videos related to Genshin Impact's "
            "Furina PV from a list of URLs."
        )
    )
    parser.add_argument("urls", nargs="*", help="Video/post URLs to download.")
    parser.add_argument(
        "-f",
        "--url-file",
        type=Path,
        help="Text file containing one URL per line. Blank lines and # comments are ignored.",
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help=f"Download directory. Default: {DEFAULT_OUT_DIR}",
    )
    parser.add_argument(
        "--format",
        default="bv*+ba/b",
        help="yt-dlp format selector. Default downloads best video+audio.",
    )
    parser.add_argument(
        "--merge-output-format",
        default="mp4",
        choices=["mp4", "mkv", "webm"],
        help="Container used when yt-dlp merges video and audio. Default: mp4.",
    )
    parser.add_argument(
        "--playlist",
        action="store_true",
        help=(
            "Download every item from a playlist or Bilibili multi-language anthology. "
            "By default, only the primary video is downloaded."
        ),
    )
    parser.add_argument(
        "--cookies",
        type=Path,
        help="Netscape-format cookies.txt for platforms that require login.",
    )
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="Read cookies from a browser, for example: chrome, edge, firefox.",
    )
    parser.add_argument("--proxy", help="Proxy URL passed through to yt-dlp.")
    parser.add_argument("--limit-rate", help="Limit download rate, for example: 2M.")
    parser.add_argument(
        "--filter-furina",
        action="store_true",
        help=(
            "Skip entries whose title does not contain Furina keywords. Useful for "
            "playlist/search URLs; avoid it for posts with empty or vague titles."
        ),
    )
    parser.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="Additional keyword used by --filter-furina. Can be repeated.",
    )
    parser.add_argument(
        "--write-subs",
        action="store_true",
        help="Download available subtitles/captions in zh/en when present.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the yt-dlp command without downloading.",
    )
    return parser


def find_ytdlp_command() -> list[str] | None:
    if importlib.util.find_spec("yt_dlp") is not None:
        return [sys.executable, "-m", "yt_dlp"]

    executable = shutil.which("yt-dlp")
    if executable:
        return [executable]

    return None


def read_urls(url_file: Path | None, inline_urls: Iterable[str]) -> list[str]:
    urls: list[str] = []

    if url_file:
        if not url_file.exists():
            raise FileNotFoundError(f"URL file not found: {url_file}")

        for raw_line in url_file.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            urls.append(line)

    urls.extend(url.strip() for url in inline_urls if url.strip())
    return dedupe(urls)


def dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def build_match_filter(keywords: list[str]) -> str:
    escaped = [re.escape(keyword) for keyword in keywords if keyword.strip()]
    return "title ~= (?i)(" + "|".join(escaped) + ")"


def build_ytdlp_args(args: argparse.Namespace, urls: list[str]) -> list[str]:
    out_dir = args.out_dir
    archive_file = out_dir / "download-archive.txt"
    output_template = (
        "%(extractor_key)s/%(upload_date>%Y-%m-%d|unknown)s - "
        "%(title).160B [%(id)s].%(ext)s"
    )

    command: list[str] = [
        "--ignore-errors",
        "--no-overwrites",
        "--continue",
        "--download-archive",
        str(archive_file),
        "--paths",
        str(out_dir),
        "--output",
        output_template,
        "--format",
        args.format,
        "--merge-output-format",
        args.merge_output_format,
        "--write-info-json",
        "--write-thumbnail",
        "--restrict-filenames",
    ]

    # Bilibili treats its multi-language editions as an anthology. Most project
    # downloads need the primary (Chinese) item only; retain all entries only
    # when the caller explicitly asks for them.
    if not args.playlist:
        command.append("--no-playlist")

    if args.filter_furina:
        command.extend(["--match-filter", build_match_filter(DEFAULT_KEYWORDS + args.keyword)])

    if args.write_subs:
        command.extend(["--write-subs", "--write-auto-subs", "--sub-langs", "zh.*,en.*"])

    if args.cookies:
        command.extend(["--cookies", str(args.cookies)])

    if args.cookies_from_browser:
        command.extend(["--cookies-from-browser", args.cookies_from_browser])

    if args.proxy:
        command.extend(["--proxy", args.proxy])

    if args.limit_rate:
        command.extend(["--limit-rate", args.limit_rate])

    command.extend(urls)
    return command


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        urls = read_urls(args.url_file, args.urls)
    except OSError as exc:
        print(f"Failed to read URLs: {exc}", file=sys.stderr)
        return 2

    if not urls:
        parser.error("Provide at least one URL or --url-file.")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    ytdlp_command = find_ytdlp_command()
    if not ytdlp_command:
        if args.dry_run:
            ytdlp_command = [sys.executable, "-m", "yt_dlp"]
        else:
            print(
                "yt-dlp is required but was not found.\n"
                "Install it with: python -m pip install -U yt-dlp",
                file=sys.stderr,
            )
            return 2

    command = ytdlp_command + build_ytdlp_args(args, urls)

    if args.dry_run:
        print(" ".join(quote_part(part) for part in command))
        return 0

    try:
        completed = subprocess.run(command, check=False)
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130

    return completed.returncode


def quote_part(value: str) -> str:
    if re.search(r"\s", value):
        return '"' + value.replace('"', '\\"') + '"'
    return value


if __name__ == "__main__":
    raise SystemExit(main())
