# AGENTS.md

本文件给 Codex 和其他代理说明如何在 `wenjing-content` 仓库中工作。

## 仓库定位

这是一个多平台内容项目仓库，不是应用代码仓库。核心目标是管理：

- 具体内容项目：`projects/`
- 项目级调研、方案、资料来源和复盘
- 微信公众号、小红书、抖音、掘金等平台内容
- 可复用模板：`templates/`
- 写作流程与方法论：`docs/`
- 本地 Codex Skill：`.codex/skills/`

## 最重要的规则

1. 具体内容必须写进 `projects/{project-slug}/`。
2. 方案、选题调研、资料来源都归属于具体项目。
3. 单篇大纲、标题池、参考资料、配图建议等写作结构写进项目 `sources.md`。
4. 平台目录只放对应平台的输出内容，例如文章正文、笔记正文、脚本和分镜。
5. `templates/` 只放空白模板，不放具体项目内容。
6. 修改模板时必须更新 `templates/CHANGELOG.md`。
7. 不要把临时下载视频、原始大媒体文件、密钥、`.env` 或中间产物提交进仓库。

## 新建项目

新项目放在：

```text
projects/YYYY-MM-topic-slug/
```

推荐创建：

```text
README.md
brief.md
plan.md
sources.md
research/topic-research.md
shared/outline.md
shared/key-points.md
assets/
```

按需要创建平台目录：

```text
wechat/
xiaohongshu/
douyin/
juejin/
```

创建项目文件时，从 `templates/project/` 和 `templates/platforms/` 复制对应模板结构。

## 文件归属

| 内容 | 放置位置 |
| --- | --- |
| 原始需求 | `projects/{project}/brief.md` |
| 选题调研 | `projects/{project}/research/topic-research.md` |
| 内容方案 | `projects/{project}/plan.md` |
| 资料来源、可引用事实、单篇大纲、标题池、配图建议 | `projects/{project}/sources.md` |
| 跨平台共用主线 | `projects/{project}/shared/outline.md` |
| 核心观点和可复用表达 | `projects/{project}/shared/key-points.md` |
| 公众号文章 | `projects/{project}/wechat/article.md` |
| 小红书笔记 | `projects/{project}/xiaohongshu/note.md` |
| 抖音脚本 | `projects/{project}/douyin/script.md` |
| 抖音分镜 | `projects/{project}/douyin/storyboard.md` |
| 掘金文章 | `projects/{project}/juejin/article.md` |

## 写作流程

默认顺序：

1. 阅读项目 `brief.md`。
2. 若主题依赖事实、趋势或近期信息，先补 `sources.md` 和 `research/topic-research.md`。
3. 在 `plan.md` 中确定核心观点、平台拆分和风险边界。
4. 在 `sources.md` 中整理单篇大纲、标题池、资料来源、可引用事实和配图建议。
5. 在 `shared/` 中沉淀跨平台共用主线和关键表达。
6. 再写具体平台输出内容。
7. 完成后检查状态字段、引用来源、模板版本和平台适配。

## 平台规则

### 微信公众号

- 适合长文、技术科普、教程和观点文。
- 单篇要独立完整，不写成教材章节。
- 技术内容先给场景，再解释概念。
- 使用 `docs/workflows/wechat-article.md` 或 `docs/workflows/wechat-tech-article.md`。
- 平台稿可保留 front matter；直接交付给微信公众号编辑器前必须准备无 front matter 的粘贴稿。
- 粘贴稿只放标题、正文和读者可见的资料来源，不保留 `[S1]` 等内部资料编号、写作备注或标题池。
- 直接写入剪贴板时优先使用纯 Unicode Markdown；不要自行构造 HTML 富文本剪贴板，避免公众号编辑器出现乱码或粘出 `<section ...>` 源码。
- 需要富文本样式时，使用 Markdown 公众号排版器或 `tardiformatter-wechat-format`，并在微信编辑器中最终检查表格、引用块和图片。

### 小红书

- 适合种草、教程笔记、产品推荐和轻观点表达。
- 要保留真实场景、细节和情绪。
- 不要写成公司宣传稿。
- 使用 `docs/workflows/xiaohongshu-copy.md`。

### 抖音

- 适合短视频脚本、口播、分镜和竞品拆解。
- 优先处理前 3 秒钩子、第一帧、节奏和合规。
- 脚本和分镜分开存放。
- 使用 `docs/workflows/douyin-script.md`。

### 掘金

- 适合技术实战、工程经验、源码解析和开发者向文章。
- 要重视代码、环境、踩坑和可复现步骤。
- 使用 `templates/platforms/juejin/article.md`。

## 模板规则

- 项目级模板放在 `templates/project/`。
- 平台级模板放在 `templates/platforms/{platform}/`。
- 模板文件应保留 front matter：

```yaml
template: platforms/wechat/article
template_version: 2026-07-16
status: draft
```

- 修改模板时，在 `templates/CHANGELOG.md` 增加记录，说明日期、影响范围和迁移建议。

## 资料与事实核验

- 涉及“最新”“最近”“本周”“趋势”“价格”“政策”“产品能力”等内容时，必须核验一手来源。
- 优先使用官方文档、发布公告、GitHub、论文、产品页面和原始视频/截图。
- 二手文章可以作为线索，但不要作为关键事实的唯一依据。
- 项目内所有重要来源记录到 `sources.md`。

## Git 与提交

- 提交前检查 `git status --short`。
- 不要提交 `_temp/`、`writing/_temp/`、视频下载文件、`.env`、密钥或大体积临时素材。
- 结构迁移时尽量保留 rename，让 Git 历史清楚。
- 提交信息建议：

```text
docs: update project templates
docs: add content project
docs: refine wechat article draft
docs: add douyin script
```

## 风格

- 默认用中文写作和说明。
- 路径、文件名和平台目录使用英文 slug。
- 内容文件可以中文命名，但平台入口文件优先使用稳定名称，如 `article.md`、`note.md`、`script.md`。
- 文档应简洁、可执行，避免只写抽象原则。
