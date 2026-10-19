# AI 唱歌 v1 制作状态机

---
status: draft
version: 0.1
date: 2026-10-15
project: 2026-10-ai-singing
depends_on: doc/prd.md
machine: doc/production-state-machine.yaml
---

## 结论

v1 的一次制作从 `idle` 开始，只在四种终态结束：`recorded_internal`、`recorded_publishable`、`failed`、`stopped`。

生成最多 3 次。入口未确认、权利不通过、条款不明确时，不能进入生成。终态不能继续生成；下一首必须新开一次制作。机器可读定义在 `doc/production-state-machine.yaml`，与本文不一致时以 YAML 的迁移表为准，并同时改本文。

这台状态机不包含平台成稿、本地模型部署和音色替换。那些行为不是未画出的后续状态，而是禁止事件。

## 状态

| 状态 | 含义 | 是否终态 |
| --- | --- | --- |
| `idle` | 还没有本次材料 | 否 |
| `materials_draft` | 正在写主题、语言、时长、歌词和风格 | 否 |
| `rights_blocked` | 材料涉及特定歌手、现成歌曲、他人音色或未授权音源 | 否 |
| `provider_unconfirmed` | 材料合格，云端入口尚未确认 | 否 |
| `ready` | 入口已确认，可以生成 | 否 |
| `generating` | 已提交，等待可播放结果 | 否 |
| `reviewing` | 已有可播放结果，等待听评 | 否 |
| `revision_pending` | 本轮不采纳，还可改歌词或风格 | 否 |
| `recorded_internal` | 记录完成，但不得公开 | 是 |
| `recorded_publishable` | 记录完成，且条款允许公开 | 是 |
| `failed` | 3 次都未采纳，原因已记录 | 是 |
| `stopped` | 入口不可用、条款不明确，或试图换工具 | 是 |

`recorded_publishable` 只表示这条 demo 按入口条款可以公开。它不进入公众号、小红书、抖音或掘金成稿。

## 上下文

每次制作单独计数，不跨歌曲累计。

| 字段 | 初值 | 规则 |
| --- | --- | --- |
| `attempt` | 0 | 每次 `generate` 加 1，最大 3 |
| `public_use` | `unknown` | 只有确认入口时改为 `allowed` 或 `denied` |

`public_use` 仍是 `unknown` 时，确认入口不能成功，制作进入 `stopped`。

## 迁移

守卫不满足时停在原状态，不产生副作用。

| 当前状态 | 事件 | 守卫 | 下一状态 |
| --- | --- | --- | --- |
| `idle` | `begin` | 无 | `materials_draft` |
| `materials_draft` | `submit_materials` | 权利违规 | `rights_blocked` |
| `materials_draft` | `submit_materials` | 材料合格，入口未确认 | `provider_unconfirmed` |
| `materials_draft` | `submit_materials` | 材料合格，入口已确认 | `ready` |
| `materials_draft` | `abort` | 已记录原因 | `stopped` |
| `rights_blocked` | `replace_materials` | 无 | `materials_draft` |
| `rights_blocked` | `abort` | 已记录原因 | `stopped` |
| `provider_unconfirmed` | `confirm_provider` | 账号可用、价格已知、公开使用权明确 | `ready` |
| `provider_unconfirmed` | `provider_blocked` | 已记录原因 | `stopped` |
| `ready` | `generate` | `attempt < 3` | `generating` |
| `ready` | `abort` | 已记录原因 | `stopped` |
| `generating` | `audio_ready` | 音频可播放且不进入 Git | `reviewing` |
| `generating` | `audio_failed` | `attempt < 3` 且已记录原因 | `revision_pending` |
| `generating` | `audio_failed` | `attempt = 3` 且已记录原因 | `failed` |
| `reviewing` | `reject_take` | `attempt < 3` 且已记录原因 | `revision_pending` |
| `reviewing` | `reject_take` | `attempt = 3` 且已记录原因 | `failed` |
| `reviewing` | `accept_take` | 记录完整，且 `public_use = denied` | `recorded_internal` |
| `reviewing` | `accept_take` | 记录完整，且 `public_use = allowed` | `recorded_publishable` |
| `reviewing` | `abort` | 已记录原因 | `stopped` |
| `revision_pending` | `revise_materials` | 材料仍然合格 | `ready` |
| `revision_pending` | `revise_materials` | 修改后权利违规 | `rights_blocked` |
| `revision_pending` | `abort` | 已记录原因 | `stopped` |

`generate` 是唯一增加 `attempt` 的事件。听评和失败记录不增加次数。

材料合格指：有主题、语言、30–90 秒时长、8–16 行原创歌词和风格，且风格不点名自然人声音。

记录完整指：主题、歌词、原文提示词、工具名称、接口或模型标识、日期、听评、AI 生成标识、是否允许公开，均已写入本次记录。

## 禁止事件

以下事件没有通往生成或发布的迁移。发生时先写原因，再进入 `stopped`。

- `switch_tool`：更换云端入口、改用尚未评估的工具，或把本次制作改成音色替换、翻唱、本地部署。
- 从任一终态 `resume`：终态不能回到 `ready`、`generating` 或 `reviewing`。

权利问题不能用 `confirm_provider` 绕过。入口问题不能用 `submit_materials` 绕过。未听评不能 `accept_take`。

## 与 PRD 的对应关系

| PRD 规则 | 状态机约束 |
| --- | --- |
| 先确认一个云端入口 | `provider_unconfirmed` 只能到 `ready` 或 `stopped` |
| 主题和歌词不得指向现成歌曲或特定歌手 | 违规进入 `rights_blocked`，不能生成 |
| 最多再生成 2 次，合计 3 次 | `attempt` 达到 3 后只能 `failed`、接受当前结果或 `stopped` |
| 失败也要记录 | 进入 `failed` 或 `stopped` 前必须已有原因 |
| 条款不允许公开时只作内部验证 | `public_use = denied` 时只能到 `recorded_internal` |
| 条款不明确时停止 | 确认入口失败，进入 `stopped`，不生成 |
| 音频不提交 | `audio_ready` 要求文件留在仓库外 |
| v1 不制作平台成稿 | `recorded_publishable` 是终态 |

M3 的停止、改写内容或本地验证 ACE-Step 1.5，是 v1 终态之后的另一次决策，不是本状态机的状态。
