# 平台接口核验

核验日期：2026-10-15。

这里只记录内容发布相关的官方接口。网页后台里未公开的请求、第三方数据接口和浏览器自动化，都不算官方开放接口。官方 MCP 指平台自己发布并维护的 MCP；第三方包装的数据查询服务单独注明。

| 平台 | 官方内容发布接口 | 官方 MCP | 仓库处理 |
| --- | --- | --- | --- |
| 微信视频号 | 无普通动态发布接口 | 无官方发布 MCP | 只准备脚本，人工发布 |
| CSDN | 未找到公开文档 | 未找到 | Markdown 成稿，人工粘贴 |
| 博客园 | 有，MetaWeblog | 未找到 | 用 `.codex/skills/cnblogs-publisher`，默认存草稿 |
| 思否 | 未找到 | 未找到 | 人工发布 |
| InfoQ | 未找到，公开路径是作者投稿和审核 | 未找到 | 人工投稿，审核通过才算发布 |
| 开源中国 | 旧 OpenAPI 入口已返回页面未找到 | 未找到 | 人工发布 |

## 微信视频号

官方接口目录：<https://developers.weixin.qq.com/doc/channels/api/>

2026-10-15 读取该目录，视频号助手 API 列出的是：

- 直播基础信息
- 橱窗管理
- 留资组件
- 留资直播数据
- 直播大屏数据
- 罗盘达人版

同页还有本地生活商品、库存、订单、核销和资金接口。目录中没有普通视频动态的上传、草稿、发布或已发布列表接口。

因此不能把视频号写成可自动发布的平台。直播、橱窗和本地生活接口也不能用来发普通视频。

第三方存在视频号数据查询 MCP，例如 SocialDataX 的托管服务。它声明只读取热榜、视频、评论和用户内容，不提供登录、发布、编辑、点赞、评论或转发。它不是微信官方 MCP，本仓库不接入。

## CSDN

2026-10-15 访问 `https://openapi.csdn.net/`，返回 `403 Forbidden`。没有找到由 CSDN 维护的公开文章发布文档。

网上流传的 `api.csdn.net`、`mp.csdn.net` 发布地址来自二次文章或页面抓包，不能作为官方接口写入模板。发布使用 CSDN 编辑器人工完成。

## 博客园

博客园有两套官方接口，用途不同。

REST OpenAPI 文档：<https://api.cnblogs.com/help>

文档中的随笔接口只有读取：

- `GET /api/blogs/{blogApp}/posts`
- `GET /api/blogposts/{id}/body`
- `GET /api/blogposts/@sitehome`

同一文档还提供新闻、博问、闪存、知识库和班级等接口。闪存、新闻评论和博问有发布操作；博客随笔没有创建、编辑、删除。

随笔发布使用 MetaWeblog：<https://rpc.cnblogs.com/metaweblog/{blog}>

2026-10-15 读取 `https://rpc.cnblogs.com/metaweblog/sitehome`，页面列出：

- `metaWeblog.newPost`
- `metaWeblog.editPost`
- `metaWeblog.getPost`
- `metaWeblog.getRecentPosts`
- `metaWeblog.getCategories`
- `metaWeblog.newMediaObject`
- `blogger.deletePost`
- `blogger.getUsersBlogs`
- `wp.newCategory`

账号需在博客园设置中开启客户端访问并使用访问令牌。令牌不是登录密码，不写入仓库。

本地接入在 `.codex/skills/cnblogs-publisher`。脚本使用 Python 标准库调用 `metaWeblog.newPost`，默认 `publish=false` 存草稿；只有明确要求公开时才传 `true`。GitHub 上有第三方 MCP 和 Skill，但没有博客园官方 MCP，本仓库不接入第三方实现。

生成稿件不会自动调用这些方法。更新、删除和上传图片还没有接入。

## 思否

2026-10-15 读取 <https://segmentfault.com/help>。帮助中心没有文章发布 API 或开放平台入口。

未找到思否官方内容发布接口和官方 MCP。文章在思否编辑器人工发布。

## InfoQ

InfoQ 中文写作社区的公开投稿路径是作者注册、写作社区投稿和编辑审核，见 InfoQ 征文活动中的投稿说明。

2026-10-15 未找到 InfoQ 面向第三方的文章创建、草稿或发布 API，也未找到官方 MCP。编辑审核未通过的稿件不能标为已发布。

## 开源中国

2026-10-15 访问以下地址，均返回「抱歉，您访问的页面没找到」：

- <https://www.oschina.net/openapi>
- <https://www.oschina.net/openapi/api>

旧资料仍把 `http://www.oschina.net/openapi` 列为可申请的 OpenAPI，但本次访问已经打不开。没有找到替代的官方发布文档，也不能证明它是否只是临时故障。在官方页面恢复并核到具体方法前，按无可用发布接口处理。

未找到开源中国官方内容发布 MCP。博客在开源中国网站人工发布。
