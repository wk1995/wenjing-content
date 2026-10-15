# 博客园发布技能来源

本目录是仓库自有技能，不是第三方仓库的裁剪副本。

| 项 | 值 |
| --- | --- |
| 官方接口 | <https://rpc.cnblogs.com/metaweblog/{blog}> |
| 接口核验日期 | 2026-10-15 |
| 参数依据 | 官方页面列出的 `metaWeblog.newPost`、`blogger.getUsersBlogs`、`metaWeblog.getCategories`、`metaWeblog.getRecentPosts` |
| 实现 | `scripts/publish_cnblogs.py`，只使用 Python 标准库 `xmlrpc.client` |

参考过两个第三方实现，但没有复制其代码：

- [zhiliye/cnblog-publisher-skill](https://github.com/zhiliye/cnblog-publisher-skill)，MIT。它把用户名和令牌写在脚本里，本技能不采用。
- [mintonzhang/cnblogs-mcp](https://github.com/mintonzhang/cnblogs-mcp)，MIT。它调用的是另一套 REST 地址，不是本次采用的 MetaWeblog。

Markdown 分类 `[Markdown]` 来自博客园客户端的既有约定，用来让正文按 Markdown 渲染。官方方法页只声明 `categories` 是字符串数组，没有单独的 Markdown 参数。
