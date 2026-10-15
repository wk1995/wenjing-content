#!/usr/bin/env python3
"""Publish a Markdown draft to cnblogs through the official MetaWeblog API.

Credentials stay outside the repository. Set them in the process environment
or in an untracked .env file:

    CNBLOGS_USERNAME
    CNBLOGS_ACCESS_TOKEN
    CNBLOGS_BLOG_ID
"""

import argparse
import os
import re
import sys
import xmlrpc.client
from pathlib import Path


METAWEBLOG_URL = "https://rpc.cnblogs.com/metaweblog/{blog_id}"
MARKDOWN_CATEGORY = "[Markdown]"
ENV_FILE_NAME = ".env"


class ConfigError(RuntimeError):
    pass


def load_env_file(path):
    values = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def resolve_config(env_file):
    file_values = {}
    if env_file is not None:
        path = Path(env_file)
        if not path.is_file():
            raise ConfigError(f"配置文件不存在: {path}")
        file_values = load_env_file(path)

    def value(name):
        return os.environ.get(name) or file_values.get(name) or ""

    config = {
        "username": value("CNBLOGS_USERNAME"),
        "access_token": value("CNBLOGS_ACCESS_TOKEN"),
        "blog_id": value("CNBLOGS_BLOG_ID"),
    }
    missing = [name for name, item in (
        ("CNBLOGS_USERNAME", config["username"]),
        ("CNBLOGS_ACCESS_TOKEN", config["access_token"]),
        ("CNBLOGS_BLOG_ID", config["blog_id"]),
    ) if not item]
    if missing:
        raise ConfigError("缺少配置: " + ", ".join(missing))
    return config


def read_markdown(path):
    text = Path(path).read_text(encoding="utf-8")
    body = text
    front_matter = {}
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            raw_front_matter = text[4:end]
            body = text[end + 5:]
            for line in raw_front_matter.splitlines():
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                front_matter[key.strip()] = value.strip().strip('"').strip("'")
    title = front_matter.get("title", "")
    if not title:
        match = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
        if match:
            title = match.group(1).strip()
    return title, body.strip() + "\n"


def split_list(value):
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def build_categories(extra):
    categories = [MARKDOWN_CATEGORY]
    for item in extra:
        if item not in categories:
            categories.append(item)
    return categories


def connect(blog_id):
    url = METAWEBLOG_URL.format(blog_id=blog_id)
    return xmlrpc.client.ServerProxy(url), url


def command_check(server, config):
    blogs = server.blogger.getUsersBlogs("", config["username"], config["access_token"])
    categories = server.metaWeblog.getCategories(
        config["blog_id"], config["username"], config["access_token"]
    )
    print(f"连接成功，博客数: {len(blogs)}")
    for blog in blogs:
        print(f"- {blog.get('blogName', '')} {blog.get('url', '')}")
    print(f"分类数: {len(categories)}")
    for category in categories:
        print(f"- {category.get('title', '')}")


def command_recent(server, config, limit):
    posts = server.metaWeblog.getRecentPosts(
        config["blog_id"], config["username"], config["access_token"], limit
    )
    for post in posts:
        print(f"{post.get('postid', '')}\t{post.get('title', '')}")


def command_publish(server, config, args):
    title, body = read_markdown(args.file)
    title = args.title or title
    if not title:
        raise ConfigError("文章没有标题。用 --title 传入，或在文件开头写一级标题。")
    categories = build_categories(split_list(args.categories))
    post = {
        "title": title,
        "description": body,
        "categories": categories,
    }
    if args.tags:
        post["mt_keywords"] = args.tags
    post_id = server.metaWeblog.newPost(
        config["blog_id"],
        config["username"],
        config["access_token"],
        post,
        args.publish,
    )
    state = "已发布" if args.publish else "已存为草稿"
    print(state)
    print(f"post_id: {post_id}")
    print(f"title: {title}")
    print(f"url: https://www.cnblogs.com/{config['blog_id']}/p/{post_id}.html")


def build_parser():
    parser = argparse.ArgumentParser(description="通过博客园官方 MetaWeblog 发布随笔。")
    parser.add_argument("--env-file", default=ENV_FILE_NAME, help="未导出环境变量时读取的本地配置文件")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check", help="验证令牌、博客和分类")
    recent = subparsers.add_parser("recent", help="读取最近随笔标题")
    recent.add_argument("--limit", type=int, default=5)

    publish = subparsers.add_parser("publish", help="提交一篇 Markdown。默认保存为草稿")
    publish.add_argument("file")
    publish.add_argument("--title")
    publish.add_argument("--categories", default="", help="额外分类，逗号分隔")
    publish.add_argument("--tags", default="", help="标签，写入 mt_keywords")
    publish.add_argument("--publish", action="store_true", help="直接公开。省略时只存草稿")
    return parser


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        config = resolve_config(args.env_file)
        server, _ = connect(config["blog_id"])
        if args.command == "check":
            command_check(server, config)
        elif args.command == "recent":
            command_recent(server, config, args.limit)
        elif args.command == "publish":
            command_publish(server, config, args)
    except ConfigError as exc:
        print(f"配置错误: {exc}", file=sys.stderr)
        return 2
    except xmlrpc.client.Fault as exc:
        print(f"博客园接口错误: {exc.faultString}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"请求失败: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
