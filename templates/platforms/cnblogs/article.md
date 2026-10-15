# 博客园文章模板

---
template: platforms/cnblogs/article
template_version: 2026-10-15
platform: cnblogs
content_type: article
status: draft
---

## 基本信息

- 文章主题：
- 目标读者：
- 文章类型：随笔 / 实践记录 / 源码笔记
- 预计字数：
- 分类：
- 标签：

## 内容要求

- 必须覆盖：
- 代码或环境：
- 不展开：
- 参考资料：

## 结构

1. 问题：
2. 做法：
3. 关键代码：
4. 结果和限制：
5. 来源：

## 交付

- 标题：
- 正文：Markdown
- 分类名：与博客园后台已有分类一致，发布前核对

## 发布限制

- 2026-10-15 核对：博客随笔发布使用 MetaWeblog，端点为 `https://rpc.cnblogs.com/metaweblog/{blog}`。
- 官方方法包括 `metaWeblog.newPost`、`metaWeblog.editPost`、`metaWeblog.getPost`、`metaWeblog.getRecentPosts`、`metaWeblog.getCategories`、`metaWeblog.newMediaObject`、`blogger.deletePost`。
- 博客园 REST OpenAPI 可以读取随笔、新闻、博问和闪存，文档中的随笔接口只有读取，不用于发文。
- 访问令牌在登录后的博客园设置里开启。令牌不写入仓库。
- 发布动作单独确认，不在生成稿件时自动调用。
