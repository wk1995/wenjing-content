# 微信公众号 API 发布工作流

本工作流通过微信公众号官方接口处理 Markdown 文章，支持：校验、上传草稿、发送预览，以及向全部粉丝或指定标签群发。入口为 GitHub Actions 的 **WeChat Official Account Publish**，只允许手动触发，不能因推送代码自动发送文章。

## 发布链路

```text
Markdown（status: ready）
  → 校验 front matter 与正文
  → 上传封面/内文图片
  → 新增公众号草稿
  → 预览（可选）
  → GitHub Environment 审批
  → 群发给全部粉丝或标签
```

`draft` 只创建草稿；`preview` 会先创建草稿，再向一个指定帐号发送预览；`send` 会先创建草稿，再提交群发任务。群发任务提交成功不等于已全部投递，实际结果应以公众号后台和回调/发送记录为准。

## 一次性配置

1. 在微信公众平台确认帐号具有相应接口权限，并在开发设置中配置 API 所需的固定出口 IP 白名单。
2. 部署带 `wechat` 标签、固定公网出口 IP 的 GitHub self-hosted runner；将该出口 IP 加入公众号白名单。GitHub 托管 runner 的 IP 不稳定，不适合作为默认发布通道。无副作用的 `validate` 作业仍在 GitHub 托管 runner 上运行。
3. 在仓库 GitHub Actions Environment 中创建 `wechat-production`，设置必要的人工审批保护规则。
4. 将 `WECHAT_APP_ID`、`WECHAT_APP_SECRET` 配置为该 Environment 的 Secrets。绝不能放入 front matter、仓库文件、Actions 输入或日志。
5. 准备封面：在工作流输入中传 `thumbnail_path`（仓库内图片路径）或已有永久素材的 `thumbnail_media_id`。封面是新增草稿的必填项。

官方接口参考：

- [新增草稿](https://developers.weixin.qq.com/doc/offiaccount/Draft_Box/Add_draft.html)
- [群发接口](https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Group_messages_interface.html)
- [预览接口](https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Group_messages_interface.html)

接口权限、群发频次、外链、留言和帐号类型限制以公众号后台及官方文档的实时规则为准。

## 文章要求

- 文件位于 `projects/{project}/wechat/`，且 front matter 中必须有 `platform: wechat`、`status` 和 `title`。`validate` 可检查任意状态；`draft`、`preview`、`send` 强制要求 `status: ready`。
- 使用 Markdown；工作流会转换常用段落、标题、列表、引用、代码块和表格为公众号正文 HTML。
- 内文图片使用相对于文章文件的仓库内路径，例如 `![示意图](../assets/example.png)`。工作流会通过接口上传并替换为公众号图片地址。
- 不使用远程图片 URL、秘密字段、内部 `[S1]` 引用或写作备注作为读者可见正文。

先在本地执行无副作用校验：

```bash
python3 tools/wechat_publish.py validate \
  --article projects/2026-07-ai-on-device-foundation/wechat/article-01.md
```

## 手动触发规范

| 模式 | 会做什么 | 必填输入 | 二次确认 |
| --- | --- | --- | --- |
| `validate` | 仅校验，不调用微信 API | `article_path` | 无 |
| `draft` | 上传图片并创建草稿 | 封面路径或 `media_id` | 无 |
| `preview` | 创建草稿并发送给一个测试帐号 | 封面、测试帐号 OpenID（`preview_to`） | `PREVIEW` |
| `send` + `all` | 创建草稿并群发给全部粉丝 | 封面 | `SEND_TO_ALL` |
| `send` + `tag` | 创建草稿并群发给标签 | 封面、`tag_id` | `SEND_TO_TAG` |

建议顺序固定为：`validate` → `draft` → `preview` → 检查公众号后台草稿和预览效果 → `send`。即使工作流支持群发，也不要跳过预览和人工审批。

## 安全边界

- 不设置 `schedule`、`push` 或自动群发触发器。
- `send` 必须同时经过 GitHub Environment 审批和确认词校验；两项缺一不可。
- 工作流使用 `concurrency` 避免两个群发任务并行。
- 生成的报告不包含 `access_token` 或 `AppSecret`；仍应仅在有权限的仓库成员间查看。
- 公众号草稿、群发配额、版权、读者隐私与平台审核由运营者最终负责。
