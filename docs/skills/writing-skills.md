# 写作 Skill 清单

这里整理文镜项目当前使用的写作类 Codex Skill。

## 总览

| Skill | 平台 | 最适合的任务 | 主要产出 |
| --- | --- | --- | --- |
| `wechat-article-writer` | 微信公众号 | 公众号文章、自媒体长文、教程型文章 | 正文、备选标题、排版建议、配图建议 |
| `copywriting-skills` | 小红书 | 小红书正文、产品推荐、品牌语气、教程笔记 | 笔记正文、CTA、口语化改写 |
| `huashu-douyin-script` | 抖音 | 种草视频、带货脚本、千川素材、竞品拆解 | 视频分析、爆款公式、完整脚本、分镜表 |

## 安装命令

当前这台电脑已安装这三个 Skill。新机器可以用下面命令复现：

```powershell
npx skills add iamzhihuix/happy-claude-skills --skill wechat-article-writer -g -a codex -y
npx skills add vivy-yi/xiaohongshu-skills --skill copywriting-skills -g -a codex -y
npx skills add alchaincyf/huashu-skills --skill huashu-douyin-script -g -a codex -y
```

默认安装位置：

```text
C:\Users\<用户名>\.codex\skills
```

## `wechat-article-writer`

适用关键词：公众号、微信文章、自媒体写作、爆款文章、内容创作。

核心流程：

1. 搜索资料：优先找最新资料，多来源交叉验证。
2. 撰写文章：通常 1000 到 1500 字，使用故事化开头。
3. 生成标题：输出 5 个备选标题，突出痛点、数字、结果和悬念。
4. 排版优化：控制段落长度，补充配图位置、代码块和金句处理建议。

推荐输入：

- 文章主题
- 目标读者
- 写作目的
- 是否需要搜索最新资料
- 风格偏好
- 预计字数

工作流文档：[微信公众号文章工作流](../workflows/wechat-article.md)

## `copywriting-skills`

适用关键词：小红书正文、caption、产品描述、品牌语气、教程笔记、情绪故事。

核心原则：

1. 开头先给钩子，快速抓住注意力。
2. 用口语表达，避免正式、公司化、学术化语气。
3. 保留真实细节，例如使用场景、价格、周期、人群特征。
4. 用情绪连接读者，例如共鸣、惊喜、后悔没早发现。
5. 结尾给明确 CTA，例如点赞收藏、评论互动、关注。

推荐输入：

- 笔记主题
- 人设或品牌语气
- 产品信息或观点素材
- 目标人群
- 想要的情绪
- 是否需要种草、教程、测评或故事风格

工作流文档：[小红书正文文案工作流](../workflows/xiaohongshu-copy.md)

## `huashu-douyin-script`

适用关键词：抖音脚本、爆款拆解、竞品分析、带货脚本、千川素材、种草脚本、视频拆解。

核心流程：

1. 收集输入：竞品视频链接、产品信息、脚本类型和目标时长。
2. 下载视频：使用 `yt-dlp` 下载对标视频。
3. 视频分析：用 Gemini 分析前 3 秒钩子、分镜、节奏、视觉和转化设计。
4. 爆款公式提炼：汇总竞品共性，形成钩子、分镜、节奏和 CTA 模板。
5. 脚本和分镜生成：输出完整口播脚本和分镜表。
6. 审校：检查口语化、钩子强度、时长、合规和 AI 味。

运行依赖：

- `uv`
- `yt-dlp`
- `GEMINI_API_KEY`
- 已登录抖音的 Chrome 浏览器

推荐输入：

- 1 到 5 个对标或竞品视频链接
- 产品名称、核心卖点、目标人群、价格
- 脚本类型：种草视频或千川投放素材
- 目标时长
- 品牌调性和投放目标

工作流文档：[抖音视频脚本工作流](../workflows/douyin-script.md)

## 平台选择建议

| 需求 | 优先使用 |
| --- | --- |
| 写一篇完整公众号文章 | `wechat-article-writer` |
| 把一个产品写成小红书笔记 | `copywriting-skills` |
| 拆解竞品视频并生成脚本 | `huashu-douyin-script` |
| 已有长文，需要改成小红书风格 | 先用 `wechat-article-writer` 梳理内容，再用 `copywriting-skills` 改写 |
| 已有产品卖点，需要做抖音带货视频 | `huashu-douyin-script` |
