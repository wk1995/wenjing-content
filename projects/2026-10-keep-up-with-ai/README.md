---
template: project/readme
template_version: 2026-07-16
status: planning
---

# keep-up-with-ai 项目

## 项目简介

- 项目 slug：2026-10-keep-up-with-ai
- 创建日期：2026-10-11
- 主题调整：2026-10-15（原「普通研发如何跟上 AI」定位停用）
- 项目状态：planning
- 核心主题：最新 AI 资讯日更。每天一条，覆盖 GitHub 开源库、行业前沿技术、大厂 AI 动态；另加周一周报和每月 1 日月报。
- 目标读者：想用很短时间知道「今天 AI 圈发生了什么」的人，包括开发者和普通观众。
- 项目目标：在抖音、快手、微信公众号同步日更，并稳定产出周总结、月总结。

## 更新节奏

| 类型 | 频率 | 选材 | 平台 |
| --- | --- | --- | --- |
| 日更 | 每天 1 条，含周一和每月 1 日 | 当天最值得讲的 1 条：开源库 / 前沿技术 / 大厂动态 | 抖音、快手、公众号同一事实、三种讲法 |
| 周报 | 每周一，另加，不替换日报 | 刚结束的一周留下的少数几条，按三类归纳 | 公众号为主，短视频做 60–90 秒回顾 |
| 月报 | 每月 1 日，另加，不替换日报 | 刚结束的月份：趋势、还值得记住的、已经过时的 | 公众号长文为主，短视频只讲 3 个结论 |

周报、月报和当天日报同时发。1 日若正好是周一，当天发三条：昨天所在月的月报、刚结束那一周的周报、当天日报。

当天若有重大发布，日更选这条，不机械轮换三类。没登上日更、但仍然重要的条目，放进周报。

## 项目结构

说明：`sources.md` 负责资料来源、可引用事实、单条大纲和标题池；平台目录只放对应平台的成稿。

```text
.
├── README.md
├── brief.md
├── plan.md
├── sources.md
├── research/
│   └── topic-research.md
├── shared/
│   ├── outline.md
│   └── key-points.md
├── assets/
├── wechat/          # 公众号日更、周总结、月总结
├── douyin/          # 抖音口播脚本
└── kuaishou/        # 快手口播脚本
```

成稿命名：

```text
wechat/daily/YYYY-MM-DD.md
wechat/weekly/YYYY-Www.md
wechat/monthly/YYYY-MM.md
douyin/daily/YYYY-MM-DD-script.md
kuaishou/daily/YYYY-MM-DD-script.md
```

`wechat/article.md` 是旧定位草稿，已停用，不作为当前系列成稿。

## 平台规划

| 平台 | 内容形式 | 状态 | 文件 |
| --- | --- | --- | --- |
| 微信公众号 | 日更短文 + 周总结 + 月总结 | planning | `wechat/` |
| 抖音 | 日更短视频，前 3 秒给结论 | planning | `douyin/` |
| 快手 | 日更短视频，更口语、更讲「能干嘛」 | planning | `kuaishou/` |
| 小红书 | 不做 | 移出范围 | — |
| 掘金 | 不做 | 移出范围 | — |

## 当前进展

- 2026-10-15：主题改为 AI 资讯日更，平台定为抖音、快手、微信公众号。
- 日更信源清单、开更日期尚未定。
- 旧稿 `wechat/article.md` 保留，状态为 archived。

## 复盘

- 发布结果：
- 数据表现：
- 可复用经验：
- 下次调整：
