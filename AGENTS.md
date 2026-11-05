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
- 记录来源时保留标题或主体、链接、核验日期和它支持的具体结论；价格、接口、模型 ID、配额、地区可用性、平台规则等易变信息还要记录适用的平台/版本，不能把某一服务商的行为泛化为通用能力。
- 无法在当前工作中核验的素材内容、媒体状态或外部事实，必须标为“用户提供”或“待核验”，不能以已观看、已试听、已测试或已验证的语气陈述。文件名、上传顺序和媒体类型都不是内容或权利的证据。
- 涉及真人、肖像、声音、品牌、版权素材或用户评价时，技术上可上传或可生成不等于已获得授权；不要将素材存在本身视为同意或事实证明。

## 生成素材与可复现记录

- AI 生成的图片、音频、视频或其他可复用内容属于具体项目资产；其规划、提示词、参考素材角色、所用平台/模型、生成日期、验收结果和关键限制写入项目 `sources.md`、`plan.md` 或对应平台的分镜/成稿，便于后续复拍、修订和事实复核。
- 参考素材应说明其用途和不可迁移项，例如身份、产品、首帧、动作、镜头、环境、节奏或风格；有冲突时，先明确每个维度由哪一份素材负责，不根据文件名、上传顺序或猜测分配。
- 引用素材的标签、资源 ID、接口字段和其他机器可识别标记必须按实际平台原样保留。不同平台的语法、能力和限制不可互相套用；未核验时保留为计划中的角色说明，不伪造可直接提交的标记或调用方式。
- 续写或迭代生成内容时，仅将已验收且实际复核过的上一版结果作为连续性依据；计划中的结尾、被拒绝的版本和未观察到的状态不得当作既成事实。

## 第三方 Skill 与运行时资料

- 可复用 Skill 放在 `.codex/skills/{skill-name}/`；项目成稿、调研和素材仍放在 `projects/`，不要把具体项目内容写入 Skill、模板或全局说明。
- 引入或更新第三方 Skill、脚本、模板包或参考资料时，必须记录来源仓库、上游项目（如有）、固定 commit/tag、许可证和本地裁剪/修改边界。优先在包内维护 `PROVENANCE.md`，不要只记录浮动分支地址。
- 若仓库只保留第三方包的运行时子集，README、校验脚本和安全说明必须与实际随仓库提交的文件一致；不得要求执行未随包提供的 CI、测试、资源或网络评测，也不得把裁剪副本描述为完整上游源码。
- 更新第三方内容前先比较固定版本与上游变更；涉及产品能力、接口、价格或平台规则的材料要重新核验一手来源。保留原作者署名和许可要求，不把密钥、账号信息、私有素材或会联网读取凭据的工具作为普通运行时内容提交。
- 新增或修改 Skill 后，至少检查入口元数据、内部链接、引用文件和可执行的本地校验；校验应覆盖实际交付边界，而不仅是文件是否存在。对外部服务的调用、验证或媒体分析必须如实标明是否真的执行。

## Git 与提交

- 提交前检查 `git status --short`。
- 不要提交 `_temp/`、`writing/_temp/`、视频下载文件、`.env`、密钥或大体积临时素材。
- 结构迁移时尽量保留 rename，让 Git 历史清楚。
- 修改后运行与变更相称的检查，例如 Markdown 链接、结构/格式校验、脚本自检或 `git diff --check`；不要用未覆盖实际运行时边界的检查替代关键行为验证。
- 提交信息建议：

```text
[codex] docs: update project templates
[codex] docs: add content project
[codex] docs: refine wechat article draft
[codex] docs: add douyin script
```

### 分支与 PR

- `main` 是默认分支且受保护：非管理员不能直接 push，必须切新分支推送后开 PR。
- PR 合入 `main` 需要 `@wk1995` 批准（`.github/CODEOWNERS` 配合 Require review from Code Owners）。批准后 PR 若再有新提交，旧批准会失效，需要重新批准。
- PR 中未 Resolve 的评审对话会阻止合并。
- 禁止 force push，禁止删除 `main`。
- 管理员绕过未被禁用：`@wk1995` 保留紧急直推和自行合并的通道，因此本人发起的 PR 会一直显示 `BLOCKED`，属正常现象。
- 保护未强制 CI 状态检查：`.github/workflows/skill-runtime.yml` 按 `paths` 过滤，无关 PR 不会上报该检查，强制要求会导致永久 pending。

推荐流程：

```bash
git fetch origin
git switch -c <type>/<slug> origin/main
# 改动并自检：git diff --check、结构/链接校验、可执行脚本自检
git push -u origin <type>/<slug>
gh pr create --base main --fill
```

分支名沿用已有习惯：`codex/<slug>`、`chore/<slug>`、`feat/<slug>`。一个 PR 只做一件事。

## 风格

- 默认用中文写作和说明。
- 路径、文件名和平台目录使用英文 slug。
- 内容文件可以中文命名，但平台入口文件优先使用稳定名称，如 `article.md`、`note.md`、`script.md`。
- 文档应简洁、可执行，避免只写抽象原则。
