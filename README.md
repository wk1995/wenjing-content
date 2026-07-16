# wenjing-content

文镜内容仓库，用来管理多平台内容项目、平台模板、写作流程、专题方法论和本地 Codex Skill。

这个仓库会长期包含多个内容项目。每个项目都放在 `projects/` 下，项目内部再按平台拆分公众号、小红书、抖音、掘金等具体内容。

## 快速开始

1. 在 `projects/` 下创建一个项目文件夹，例如 `projects/2026-07-edge-ai-intro/`。
2. 从 `templates/project/` 复制项目级模板，建立 `README.md`、`brief.md`、`plan.md`、`sources.md` 和 `research/topic-research.md`。
3. 在项目目录下按需创建平台文件夹，例如 `wechat/`、`xiaohongshu/`、`douyin/`、`juejin/`。
4. 从 `templates/platforms/` 复制对应平台模板到项目的平台文件夹。
5. 按 `docs/workflows/` 的流程完成调研、方案、创作、审校和发布。

## 目录导航

| 路径 | 用途 |
| --- | --- |
| `projects/` | 具体内容项目。项目内存放 brief、方案、选题调研、资料来源、共用素材和各平台内容 |
| `templates/project/` | 项目级模板：项目 README、原始 brief、方案、资料来源、选题调研 |
| `templates/platforms/` | 平台级模板：微信公众号、小红书、抖音、掘金等内容模板 |
| `templates/CHANGELOG.md` | 模板更新记录 |
| `docs/workflows/` | 平台级内容生产流程，说明输入、步骤、产出和审校要求 |
| `docs/skills/` | 可复用的写作能力、专题方法论和选题规范 |
| `.codex/skills/` | 本仓库专用 Codex Skill，让 Codex 按文镜流程执行任务 |

## 项目结构

推荐每个项目使用下面的结构：

```text
projects/{project-slug}/
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
├── wechat/
│   └── article.md
├── xiaohongshu/
│   └── note.md
├── douyin/
│   ├── script.md
│   └── storyboard.md
└── juejin/
    └── article.md
```

归属规则：

- `brief.md`：原始需求、受众、目标和内容边界。
- `research/topic-research.md`：选题调研、竞品内容、关键词、受众洞察和角度判断。
- `plan.md`：项目方案、平台拆分、排期、风险和复用资产。
- `sources.md`：项目资料来源、可引用事实和不确定信息。
- `shared/`：跨平台共用大纲、核心观点、案例、图表说明。
- `{platform}/`：对应平台的具体成稿、脚本、分镜或发布稿。

方案和选题调研都归属于具体项目，不放在仓库全局目录里。全局只保留模板和通用方法。

## 模板体系

| 模板 | 用途 |
| --- | --- |
| [项目 README 模板](templates/project/README.md) | 创建项目简介和项目结构说明 |
| [项目 Brief 模板](templates/project/brief.md) | 记录原始需求、目标受众和内容边界 |
| [项目方案模板](templates/project/plan.md) | 记录整体方案、平台拆分和排期 |
| [资料来源模板](templates/project/sources.md) | 记录项目资料来源和可引用事实 |
| [选题调研模板](templates/project/research/topic-research.md) | 记录选题背景、竞品内容、受众洞察和角度判断 |
| [共用大纲模板](templates/project/shared/outline.md) | 记录跨平台复用的内容主线 |
| [核心观点模板](templates/project/shared/key-points.md) | 记录关键事实、可复用表达和风险表达 |
| [公众号文章模板](templates/platforms/wechat/article.md) | 项目下 `wechat/article.md` 的内容基础 |
| [端侧 AI 公众号模板](templates/platforms/wechat/edge-ai-article.md) | 端侧 AI 科普文章的专项模板 |
| [小红书笔记模板](templates/platforms/xiaohongshu/note.md) | 项目下 `xiaohongshu/note.md` 的内容基础 |
| [抖音脚本模板](templates/platforms/douyin/script.md) | 项目下 `douyin/script.md` 的内容基础 |
| [抖音分镜模板](templates/platforms/douyin/storyboard.md) | 项目下 `douyin/storyboard.md` 的分镜基础 |
| [掘金文章模板](templates/platforms/juejin/article.md) | 项目下 `juejin/article.md` 的内容基础 |

模板更新时需要记录到 [模板更新记录](templates/CHANGELOG.md)。项目内容文件应保留模板名和版本，方便后续追踪。

## 工作流

| 文件 | 适用场景 | 对应模板 |
| --- | --- | --- |
| [微信公众号文章工作流](docs/workflows/wechat-article.md) | 公众号长文、教程、观点文、爆款标题和排版建议 | [公众号文章模板](templates/platforms/wechat/article.md) |
| [微信公众号技术文工作流](docs/workflows/wechat-tech-article.md) | AI、开发工具、端侧技术、效率工具等技术科普 | [公众号文章模板](templates/platforms/wechat/article.md)、[端侧 AI 公众号模板](templates/platforms/wechat/edge-ai-article.md) |
| [抖音视频文案工作流](docs/workflows/douyin-script.md) | 技术科普、产品种草、短视频脚本、千川素材和竞品拆解 | [抖音脚本模板](templates/platforms/douyin/script.md) |
| [小红书正文文案工作流](docs/workflows/xiaohongshu-copy.md) | 小红书笔记、产品推荐、品牌语气和口语化文案 | [小红书笔记模板](templates/platforms/xiaohongshu/note.md) |

## 专题沉淀

| 文件 | 内容 |
| --- | --- |
| [写作 Skill 清单](docs/skills/writing-skills.md) | 当前使用的通用写作类 Codex Skill、安装命令和平台选择建议 |
| [端侧 AI 公众号内容提炼](docs/skills/edge-ai-wechat-content.md) | 从“整理端侧 AI 资讯”对话中提炼出的端侧 AI 科普文定位、结构、实践基线和后续选题 |

## 本地 Codex Skills

仓库内置了三个文镜专用 Skill：

| Skill | 入口 |
| --- | --- |
| `$wenjing-wechat-article` | `.codex/skills/wenjing-wechat-article/SKILL.md` |
| `$wenjing-douyin-script` | `.codex/skills/wenjing-douyin-script/SKILL.md` |
| `$wenjing-xiaohongshu-copy` | `.codex/skills/wenjing-xiaohongshu-copy/SKILL.md` |

日常可以这样向 Codex 发起任务：

```text
使用 $wenjing-wechat-article，基于 projects/2026-07-edge-ai-intro/wechat/article.md 写一篇端侧 AI 公众号文章。

使用 $wenjing-douyin-script，基于 projects/2026-07-edge-ai-intro/douyin/script.md 生成一条 30 秒技术科普视频脚本。

使用 $wenjing-xiaohongshu-copy，把 projects/2026-07-edge-ai-intro/wechat/article.md 改成小红书笔记。
```

## 内容原则

- 公众号技术文不要写成教材章节，单篇文章要独立完整。
- 技术内容先用生活场景或真实问题开头，再引出概念、趋势和实践。
- 涉及“最新”“最近”“本周”等信息时，优先核验官方文档、项目仓库、发布公告和一手资料。
- 实践内容默认考虑低配置设备，不把高端显卡、高端手机或复杂开发环境当作基础门槛。
- 抖音脚本优先关注前 3 秒钩子、第一帧、视觉信息密度、口语化和平台合规。
- 小红书内容要保留真实细节、场景和情绪，不写成公司宣传稿。

## 沉淀规则

- 新增具体内容项目：放到 `projects/{project-slug}/`。
- 新增项目级信息：放到项目目录下的 `brief.md`、`plan.md`、`sources.md` 或 `research/`。
- 新增平台内容：放到项目目录下的 `{platform}/`。
- 新增稳定流程：放到 `docs/workflows/`。
- 新增可复用选题、专题框架或写作方法：放到 `docs/skills/`。
- 新增或修改模板：放到 `templates/`，并更新 `templates/CHANGELOG.md`。
- 临时素材、下载视频、分析中间产物不要提交，放到 `.gitignore` 已排除的 `_temp/` 或 `writing/_temp/`。
