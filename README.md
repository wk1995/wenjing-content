# wenjing-content

文镜内容仓库，用来管理多平台内容项目、项目调研、内容方案、平台成稿、可复用模板、写作流程和本地 Codex Skill。

这个仓库的核心单位是“项目”。每个项目都放在 `projects/` 下，项目内部再按平台拆分微信公众号、小红书、抖音、掘金、微信视频号、CSDN、博客园、思否、InfoQ、开源中国等具体内容。方案、选题调研和资料来源都属于具体项目，不放在全局目录。

## 适用内容

- 微信公众号：技术科普、教程长文、自媒体观点文、带资料搜索的深度内容。
- 小红书：种草笔记、产品推荐、教程笔记、品牌语气和正文文案。
- 抖音：技术科普短视频、种草脚本、千川投放素材、竞品视频拆解。
- 掘金：技术文章、实战教程、源码解析、工程经验沉淀。
- 微信视频号：短视频口播和演示，先写脚本，人工发布。
- CSDN、博客园：开发者实操和源码笔记。
- 思否：具体技术问题的复盘和可复现步骤。
- InfoQ：面向工程师和技术负责人的生产实践、架构决策。
- 开源中国：开源项目解读、版本变化和实践。

## 内容生命周期

```text
选题调研 -> 项目方案 -> sources.md 整理资料和单篇结构 -> 平台输出内容 -> 审校 -> 发布 -> 复盘
```

对应文件：

| 阶段 | 文件 |
| --- | --- |
| 原始需求 | `projects/{project}/brief.md` |
| 选题调研 | `projects/{project}/research/topic-research.md` |
| 内容方案 | `projects/{project}/plan.md` |
| 资料来源、可引用事实、单篇大纲、标题池、配图建议 | `projects/{project}/sources.md` |
| 跨平台共用主线和关键表达 | `projects/{project}/shared/` |
| 平台输出内容 | `projects/{project}/{platform}/` |
| 项目复盘 | `projects/{project}/README.md` |

## 快速开始

1. 创建项目目录：

   ```text
   projects/YYYY-MM-topic-slug/
   ```

2. 从 `templates/project/` 复制项目级模板：

   ```text
   README.md
   brief.md
   plan.md
   sources.md
   research/topic-research.md
   shared/outline.md
   shared/key-points.md
   ```

3. 按需创建平台目录，并从 `templates/platforms/` 复制平台模板：

   ```text
   wechat/article.md
   xiaohongshu/note.md
   douyin/script.md
   douyin/storyboard.md
   juejin/article.md
   channels/script.md
   csdn/article.md
   cnblogs/article.md
   segmentfault/article.md
   infoq/article.md
   oschina/article.md
   ```

4. 在 `sources.md` 中整理单篇大纲、标题池、资料来源、可引用事实和配图建议；平台目录只保留对应平台的输出内容。

5. 按 `docs/workflows/` 中的平台流程完成调研、方案、创作、审校和发布。

## 目录导航

| 路径 | 用途 |
| --- | --- |
| `projects/` | 具体内容项目。每个项目独立存放 brief、调研、方案、资料、共用素材和平台输出内容 |
| `templates/project/` | 项目级模板：项目 README、brief、方案、资料来源、选题调研、共用素材 |
| `templates/platforms/` | 平台级模板：微信公众号、小红书、抖音、掘金、视频号、CSDN、博客园、思否、InfoQ、开源中国 |
| `docs/platform-apis.md` | 平台官方发布接口和 MCP 的核验记录 |
| `templates/CHANGELOG.md` | 模板更新记录 |
| `docs/workflows/` | 平台级内容生产流程 |
| `docs/skills/` | 可复用的写作能力、专题方法论和选题规范 |
| `.codex/skills/` | 本仓库专用 Codex Skill |
| `AGENTS.md` | 给 Codex/代理使用的仓库工作规则 |

## 推荐项目结构

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
├── juejin/
│   └── article.md
├── channels/
│   └── script.md
├── csdn/
│   └── article.md
├── cnblogs/
│   └── article.md
├── segmentfault/
│   └── article.md
├── infoq/
│   └── article.md
└── oschina/
    └── article.md
```

## 命名规范

项目目录推荐：

```text
YYYY-MM-topic-slug
```

示例：

```text
projects/2026-07-edge-ai-intro/
projects/2026-07-local-llm-guide/
```

平台目录固定使用英文：

```text
wechat/
xiaohongshu/
douyin/
juejin/
channels/
csdn/
cnblogs/
segmentfault/
infoq/
oschina/
```

## 模板体系

| 模板 | 用途 |
| --- | --- |
| [项目 README 模板](templates/project/README.md) | 创建项目简介和项目结构说明 |
| [项目 Brief 模板](templates/project/brief.md) | 记录原始需求、目标受众和内容边界 |
| [项目方案模板](templates/project/plan.md) | 记录整体方案、平台拆分和排期 |
| [资料来源模板](templates/project/sources.md) | 记录项目资料来源、可引用事实、单篇大纲、标题池和配图建议 |
| [选题调研模板](templates/project/research/topic-research.md) | 记录选题背景、竞品内容、受众洞察和角度判断 |
| [共用大纲模板](templates/project/shared/outline.md) | 记录跨平台复用的内容主线 |
| [核心观点模板](templates/project/shared/key-points.md) | 记录关键事实、可复用表达和风险表达 |
| [公众号文章模板](templates/platforms/wechat/article.md) | 项目下 `wechat/article.md` 的内容基础 |
| [端侧 AI 公众号模板](templates/platforms/wechat/edge-ai-article.md) | 端侧 AI 科普文章的专项模板 |
| [小红书笔记模板](templates/platforms/xiaohongshu/note.md) | 项目下 `xiaohongshu/note.md` 的内容基础 |
| [抖音脚本模板](templates/platforms/douyin/script.md) | 项目下 `douyin/script.md` 的内容基础 |
| [抖音分镜模板](templates/platforms/douyin/storyboard.md) | 项目下 `douyin/storyboard.md` 的分镜基础 |
| [掘金文章模板](templates/platforms/juejin/article.md) | 项目下 `juejin/article.md` 的内容基础 |
| [视频号脚本模板](templates/platforms/channels/script.md) | 项目下 `channels/script.md` 的内容基础 |
| [CSDN 文章模板](templates/platforms/csdn/article.md) | 项目下 `csdn/article.md` 的内容基础 |
| [博客园文章模板](templates/platforms/cnblogs/article.md) | 项目下 `cnblogs/article.md` 的内容基础 |
| [思否文章模板](templates/platforms/segmentfault/article.md) | 项目下 `segmentfault/article.md` 的内容基础 |
| [InfoQ 文章模板](templates/platforms/infoq/article.md) | 项目下 `infoq/article.md` 的内容基础 |
| [开源中国文章模板](templates/platforms/oschina/article.md) | 项目下 `oschina/article.md` 的内容基础 |

模板更新时必须记录到 [模板更新记录](templates/CHANGELOG.md)。项目内容文件应保留模板名和版本，方便后续追踪。

## 工作流

| 文件 | 适用场景 |
| --- | --- |
| [微信公众号文章工作流](docs/workflows/wechat-article.md) | 公众号长文、教程、观点文、爆款标题和排版建议 |
| [微信公众号技术文工作流](docs/workflows/wechat-tech-article.md) | AI、开发工具、端侧技术、效率工具等技术科普 |
| [抖音视频文案工作流](docs/workflows/douyin-script.md) | 技术科普、产品种草、短视频脚本、千川素材和竞品拆解 |
| [小红书正文文案工作流](docs/workflows/xiaohongshu-copy.md) | 小红书笔记、产品推荐、品牌语气和口语化文案 |

### 微信公众号发布交付

- 仓库中的公众号稿保留 front matter，用于记录模板、状态、日期、系列等元信息。
- 直接复制到微信公众号编辑器前，应先生成“粘贴稿”：去掉 front matter，只保留标题、正文和读者可见的资料来源。
- 公众号编辑器检测到 Markdown 后，可以使用其“转换格式”功能；需要更完整的富文本样式时，使用 Markdown 公众号排版器或 `.codex/skills/tardiformatter-wechat-format`。
- 不要把手写 HTML、`<section ...>`、`img://...`、内部 `[S1]` 引用标记或写作备注放进发布正文。
- 若通过剪贴板交付，优先使用纯 Unicode 文本。不要把自制 HTML 富文本直接塞给微信公众号编辑器，容易出现乱码或源码粘贴。

## 本地 Codex Skills

仓库内置了文镜专用 Skill：

| Skill | 入口 |
| --- | --- |
| `$wenjing-news-article-drafter` | `.codex/skills/wenjing-news-article-drafter/SKILL.md` |
| `$wenjing-wechat-article` | `.codex/skills/wenjing-wechat-article/SKILL.md` |
| `$wenjing-video-script` | `.codex/skills/wenjing-video-script/SKILL.md` |
| `$wenjing-douyin-script` | `.codex/skills/wenjing-douyin-script/SKILL.md` |
| `$wenjing-xiaohongshu-copy` | `.codex/skills/wenjing-xiaohongshu-copy/SKILL.md` |
| `$tardiformatter-wechat-format` | `.codex/skills/tardiformatter-wechat-format/SKILL.md` |
| `$wechat-article-writer` | `.codex/skills/wechat-article-writer/SKILL.md` |

示例：

```text
使用 $wenjing-news-article-drafter，收集过去 7 天端侧 AI 更新，写入 projects/2026-07-edge-ai-weekly/ 的 sources.md、research/topic-research.md 和 wechat/article.md。

使用 $wenjing-wechat-article，基于 projects/2026-07-edge-ai-intro/wechat/article.md 写一篇端侧 AI 公众号文章。

使用 $wenjing-douyin-script，基于 projects/2026-07-edge-ai-intro/douyin/script.md 生成一条 30 秒技术科普视频脚本。

使用 $wenjing-video-script，优化 projects/2026-07-edge-ai-intro/douyin/script.md 的前三秒钩子、口播节奏和分镜，不改变已核验事实。

使用 $wenjing-xiaohongshu-copy，把 projects/2026-07-edge-ai-intro/wechat/article.md 改成小红书笔记。

使用 $tardiformatter-wechat-format，把 projects/2026-07-edge-ai-intro/wechat/article.md 准备成可复制到微信公众号编辑器的粘贴稿。
```

## 状态字段

建议在项目和内容文件的 front matter 中使用：

```yaml
status: draft | researching | planned | review | ready | published | archived
template: platforms/wechat/article
template_version: 2026-07-16
platform: wechat
publish_url:
publish_date:
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
- 新增单篇大纲、标题池、配图建议、参考资料：统一放到项目 `sources.md`。
- 新增平台输出内容：放到项目目录下的 `{platform}/`，不要在平台目录中混放大纲和资料整理文件。
- 新增稳定流程：放到 `docs/workflows/`。
- 新增可复用选题、专题框架或写作方法：放到 `docs/skills/`。
- 新增或修改模板：放到 `templates/`，并更新 `templates/CHANGELOG.md`。
- 临时素材、下载视频、分析中间产物不要提交，放到 `.gitignore` 已排除的 `_temp/` 或 `writing/_temp/`。
