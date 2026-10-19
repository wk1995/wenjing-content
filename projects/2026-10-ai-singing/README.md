# AI 唱歌

---
template: project/readme
template_version: 2026-07-16
status: planning
---

## 项目简介

- 项目 slug：`2026-10-ai-singing`
- 创建日期：2026-10-15
- 项目状态：planning
- 所在分支：`ai-singing`（从 `main` 的 `2919039` 拉出，尚未推远程）
- 核心主题：评估并落地一条可复用的 AI 唱歌内容生产链路。
- 目标读者：本仓库的内容作者；对外成稿面向对 AI 音乐好奇、但不做模型训练的普通读者。
- 项目目标：先确认做什么、用什么做、什么不能做，再产出可发布内容。不在本仓库自研歌声模型。

## 项目结构

```text
.
├── README.md
├── brief.md
├── sources.md
└── doc/
    ├── feasibility.md
    ├── prd.md
    ├── state-machine.md
    └── production-state-machine.yaml
```

`sources.md` 只记录已核验来源。平台成稿在范围确认后再建，不提前放空目录。

## 文档

| 文档 | 作用 | 状态 |
| --- | --- | --- |
| `doc/feasibility.md` | 技术、工具、硬件和合规可行性 | draft |
| `doc/prd.md` | v1 产品范围、流程和验收 | draft |
| `doc/state-machine.md` | v1 一次制作的状态、事件和禁止跳转 | draft |
| `doc/production-state-machine.yaml` | 同一状态机的机器可读定义 | draft |
| `brief.md` | 原始需求和边界 | draft |
| `sources.md` | 可引用事实和来源 | draft |

## 当前进展

- 2026-10-15：完成开源项目与 Agent Skill 检索，并写入可行性分析和 PRD。
- 尚未在本机运行任一歌声或音乐模型，文档中的效果判断均未标为实测。

## 复盘

- 发布结果：
- 数据表现：
- 可复用经验：
- 下次调整：
