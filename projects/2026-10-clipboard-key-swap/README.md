---
template: project/readme
template_version: 2026-07-16
status: drafting
---

# 复制 API Key 时，文案被悄悄换掉

## 项目简介

- 项目 slug：2026-10-clipboard-key-swap
- 创建日期：2026-10-17
- 项目状态：drafting
- 核心主题：一次真实排查。复制 `hlg_` 开头的密钥时，剪贴板内容会在几百毫秒内被换成另一串。用 WorkBuddy 配合 Deepseek-V4.1-Flash 做对照实验，最后定位到被注入的系统进程和伪装计划任务。
- 目标读者：用 AI 编程、经常复制 API Key 的开发者；也给普通读者一个可执行的判断方法。
- 项目目标：把「怎么发现、怎么排查、怎么溯源、怎么修复」写成一篇能独立阅读的长文，并拆成短视频口播。

## 事实边界

- 会话记录更新到 2026-10-18 17:08。第一轮是 grok-4.7，其后是 Deepseek-V4.1-Flash。
- 可读原对话在 `sources.md`，含 10 月 18 日新增轮次和中间思考。工具摘录在 `sources/conversation-data.json`。分享页仍是 10 月 17 日的旧导出，不是这份的来源。
- 入库前所有 `hlg_` 密钥样例已替换为 `hlg_[REDACTED]`。
- 对外成稿仍停在 10 月 17 日的发现、排查、溯源和修复建议，没有改写成 10 月 18 日的清理和逆向结果。
- 10 月 18 日的记录显示部分清理已经执行，但结束时注入和对外连接又出现了。不能把「已经修好」写成结论。
- 10 月 23 日这台机器重装系统，10 月 24 日按原 IOC 做过一次复查：未发现残留，复制改写未复现。复查不等于「清理成功」，对象是新系统。详见 `research/post-reinstall-check.md`。

## 项目结构

```text
.
├── README.md
├── brief.md
├── plan.md
├── sources.md
├── research/
│   ├── topic-research.md
│   └── post-reinstall-check.md
├── shared/
│   ├── outline.md
│   └── key-points.md
├── sources/
│   ├── conversation.md
│   └── conversation-data.json
├── wechat/
│   └── article.md
├── douyin/
│   ├── script.md
│   └── storyboard.md
└── channels/
    └── script.md
```

## 平台规划

| 平台 | 内容形式 | 状态 | 文件 |
| --- | --- | --- | --- |
| 微信公众号 | 技术复盘长文 | drafting | `wechat/article.md` |
| 抖音 | 90 秒口播 + 分镜 | drafting | `douyin/script.md`、`douyin/storyboard.md` |
| 微信视频号 | 与抖音同一事实的口播 | drafting | `channels/script.md` |
| 小红书 | 暂不制作 |  |  |
| 掘金 / CSDN / 博客园 / 思否 / InfoQ / 开源中国 | 暂不制作 |  |  |

## 当前进展

- 2026-10-17：从默认分支 `main` 新建 `2026-10-clipboard-key-swap`，保存完整对话，写出公众号、抖音和视频号初稿。
- 2026-10-24：重装系统后复查原 IOC 与复制改写行为，未发现残留、未复现，结论登记为 `research/post-reinstall-check.md`。

## 复盘

- 发布结果：未发布
- 数据表现：
- 可复用经验：剪贴板异常要先做对照，不要先怪正在用的编辑器。
- 下次调整：复测结果已补（重装后未复现），只能把「修复」限定为「重装后未复现」，仍不能升级为「已验证修复」。

## 工作文件导航

[全部项目](../README.md) · [仓库首页](../../README.md)

- [原始需求](brief.md)
- [内容方案](plan.md)
- [资料来源与单篇结构](sources.md)
- [选题调研](research/topic-research.md)
- [共用大纲](shared/outline.md)
- [核心观点](shared/key-points.md)
