# wenjing-content

文镜内容仓库，用来沉淀多平台内容创作的工作流、需求模板、专题方法论和本地 Codex Skill。

当前主要覆盖三类内容：

- 微信公众号：技术科普、教程长文、自媒体观点文、带资料搜索的深度内容。
- 抖音：技术科普短视频、种草脚本、千川投放素材、竞品视频拆解。
- 小红书：种草笔记、产品推荐、教程笔记、品牌语气和正文文案。

## 快速开始

1. 先确定内容平台和任务类型。
2. 到 `templates/briefs/` 选择对应 brief，填写主题、目标读者、资料来源、输出要求和限制条件。
3. 按 `docs/workflows/` 里的流程完成资料核验、结构设计、创作和审校。
4. 如果某个主题或方法可以复用，沉淀到 `docs/skills/`。
5. 如果要让 Codex 在本仓库中自动走固定流程，使用 `.codex/skills/` 里的本地 Skill。

## 目录导航

| 路径 | 用途 |
| --- | --- |
| `docs/workflows/` | 平台级内容生产流程，说明输入、步骤、产出和审校要求 |
| `docs/skills/` | 可复用的写作能力、专题方法论和选题规范 |
| `templates/briefs/` | 每次启动写作任务时填写的需求模板 |
| `.codex/skills/` | 本仓库专用 Codex Skill，让 Codex 按文镜流程执行任务 |
| `docs/conversation-summary.md` | 项目早期对话整理和写作 Skill 选型背景 |

## 工作流

| 文件 | 适用场景 | 对应模板 |
| --- | --- | --- |
| [微信公众号文章工作流](docs/workflows/wechat-article.md) | 公众号长文、教程、观点文、爆款标题和排版建议 | [公众号文章需求模板](templates/briefs/wechat-article-brief.md) |
| [微信公众号技术文工作流](docs/workflows/wechat-tech-article.md) | AI、开发工具、端侧技术、效率工具等技术科普 | [公众号文章需求模板](templates/briefs/wechat-article-brief.md)、[端侧 AI 公众号文章 Brief](templates/briefs/edge-ai-wechat-article.md) |
| [抖音视频文案工作流](docs/workflows/douyin-script.md) | 技术科普、产品种草、短视频脚本、千川素材和竞品拆解 | [抖音视频脚本需求模板](templates/briefs/douyin-script-brief.md) |
| [小红书正文文案工作流](docs/workflows/xiaohongshu-copy.md) | 小红书笔记、产品推荐、品牌语气和口语化文案 | [小红书笔记需求模板](templates/briefs/xiaohongshu-note-brief.md) |

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

这些 Skill 已通过 `skill-creator` 的 `quick_validate.py` 校验，用来把本仓库的 workflow、brief 和专题规范串起来。日常可以这样向 Codex 发起任务：

```text
使用 $wenjing-wechat-article，基于 templates/briefs/edge-ai-wechat-article.md 写一篇端侧 AI 公众号文章。

使用 $wenjing-douyin-script，按 templates/briefs/douyin-script-brief.md 生成一条 30 秒技术科普视频脚本。

使用 $wenjing-xiaohongshu-copy，把这篇公众号文章改成小红书笔记。
```

## 平台选择

| 需求 | 优先使用 |
| --- | --- |
| 写完整公众号文章 | `docs/workflows/wechat-article.md` |
| 写公众号技术科普或教程 | `docs/workflows/wechat-tech-article.md` |
| 写端侧 AI 主题文章 | `docs/skills/edge-ai-wechat-content.md` + `templates/briefs/edge-ai-wechat-article.md` |
| 拆解抖音竞品并生成脚本 | `docs/workflows/douyin-script.md` |
| 写小红书种草或产品笔记 | `docs/workflows/xiaohongshu-copy.md` |

## 内容原则

- 公众号技术文不要写成教材章节，单篇文章要独立完整。
- 技术内容先用生活场景或真实问题开头，再引出概念、趋势和实践。
- 涉及“最新”“最近”“本周”等信息时，优先核验官方文档、项目仓库、发布公告和一手资料。
- 实践内容默认考虑低配置设备，不把高端显卡、高端手机或复杂开发环境当作基础门槛。
- 抖音脚本优先关注前 3 秒钩子、第一帧、视觉信息密度、口语化和平台合规。
- 小红书内容要保留真实细节、场景和情绪，不写成公司宣传稿。

## 沉淀规则

- 新增一个稳定流程：放到 `docs/workflows/`。
- 新增一个可复用选题、专题框架或写作方法：放到 `docs/skills/`。
- 新增一个任务输入表：放到 `templates/briefs/`。
- 临时素材、下载视频、分析中间产物不要提交，放到 `.gitignore` 已排除的 `_temp/` 或 `writing/_temp/`。
