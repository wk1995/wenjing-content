---
name: cnblogs-publisher
description: 把已写好的 Markdown 随笔通过博客园官方 MetaWeblog 提交到用户自己的博客。用户要求发布、存草稿、检查博客园令牌或读取最近随笔时使用。不要在写稿阶段自动调用。
---

# 博客园发布

只使用博客园官方 MetaWeblog：`https://rpc.cnblogs.com/metaweblog/{blog_id}`。

默认保存为草稿。只有用户明确说「发布」「公开」时才加 `--publish`。

## 凭据

凭据不进仓库，也不写进对话记录。需要这三项：

- `CNBLOGS_USERNAME`：博客园登录名
- `CNBLOGS_ACCESS_TOKEN`：设置页生成的访问令牌，不是登录密码
- `CNBLOGS_BLOG_ID`：博客地址 `https://www.cnblogs.com/{blog_id}` 中的 `{blog_id}`

优先读当前进程的环境变量。没有时再读调用目录下未跟踪的 `.env`。示例见 `.env.example`。

## 命令

在技能目录执行：

```bash
python scripts/publish_cnblogs.py check
python scripts/publish_cnblogs.py recent --limit 5
python scripts/publish_cnblogs.py publish path/to/article.md
python scripts/publish_cnblogs.py publish path/to/article.md --publish
```

`publish` 从 front matter 的 `title` 或正文第一个一级标题取标题。可用 `--title`、`--categories`、`--tags` 覆盖。分类会自动加上 `[Markdown]`，这是博客园客户端让正文按 Markdown 渲染的既有约定。

提交成功后把返回的 `post_id` 和状态写回文章 front matter 的 `cnblogs_post_id`、`cnblogs_status`。不要把令牌写进文章。

## 边界

- 不调用博客园 REST OpenAPI 发随笔。那套接口只能读取随笔。
- 不使用第三方登录态、网页私有接口或浏览器自动化。
- 缺少令牌时停下来向用户要这三项，不要猜测，也不要改用其他发布方式。
- 更新已有随笔、删除和上传图片本次不做。需要时再单独加。
