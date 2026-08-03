# AI 端侧基础项目资料与结构

---
template: project/sources
template_version: 2026-07-16
status: draft
---

## 资料原则

- 本项目当前先做方案和大纲，具体文章写作前再补充最新资料。
- 涉及工具、模型、框架、系统能力、手机/PC 厂商功能时，必须查一手来源。
- 不把发布会宣传、二手转述或社区体验直接当成确定事实。
- 每篇文章至少保留 3 个可核验来源。

## 首月 15 篇的写作资料卡

首月发布计划以 2026-08-05 为首发日、每两天一篇。第 01 篇已重写为约 1,000 字的候选稿，但尚未在本项目中记录为已发布；发布前仍应按当天产品与地区可用性复核易变事实。

| 篇号 | 核心读者问题 | 论点与结构 | 标题备选 | 资料要求 |
| --- | --- | --- | --- | --- |
| 01 | 端侧 AI 和我有什么关系？ | 日常场景 → 概念 → 云端/端侧/协同 → 设备自查 | AI 为什么开始走进手机和电脑？ / 你的手机里，其实已经有一部分 AI | 系统官方文档、日常功能说明 |
| 02 | 为什么账号开始写端侧 AI？ | Android 生活经验 → AI 已进入设备 → 系列承诺 → 征集问题 | 以前写 Android 生活，为什么现在要聊端侧 AI？ / 我想把 AI 讲得离日常设备更近一点 | 不依赖外部硬事实，以作者立场和读者互动为主 |
| 03 | 手机上的 AI 是不是都在本地跑？ | 三种运行位置 → 例子 → 判断方法 → 边界 | 手机上的 AI，到底哪些是真的在本地跑？ / 一个 AI 功能，到底在手机里还是云端？ | Android/应用官方隐私与技术说明 |
| 04 | 端侧 AI 已经改变了什么？ | 字幕、相册、降噪等 3–4 个场景 → 好处与限制 | 端侧 AI 先改变了哪些小事？ / 你每天可能都在用的端侧 AI | 每个例子回到对应官方帮助页 |
| 05 | CPU、GPU、NPU 有何区别？ | 一句比喻 → 各自任务 → 不必迷信参数 → 设备自查 | CPU、GPU、NPU 到底谁在跑 AI？ / 买设备时，NPU 到底值不值得看？ | 芯片/系统官方文档，不拿营销 TOPS 直接比较体验 |
| 06 | 是否应为 AI 换手机？ | 五问清单：功能、离线、更新、价格、替代方案 | 下一台手机要不要为 AI 多花钱？ / 别急着为 AI 换机，先回答这 5 个问题 | 当期机型、政策和价格必须发布当天核验 |
| 07 | 云端和端侧是否对立？ | 三种方案对比 → 任务分类 → 隐私与能力边界 | 云端 AI、端侧 AI、端云协同，为什么不是二选一 | 官方架构/隐私资料与明确案例 |
| 08 | Android 手机能否跑本地 AI？ | 系统/内存/存储/发热 → 预期管理 → 体验路线 | 你的 Android 手机能跑本地 AI 吗？ / 手机上跑本地 AI，先看这 4 个限制 | 工具与设备兼容列表须当天核验 |
| 09 | 小模型为什么重要？ | 大小模型任务差异 → 量化直觉 → 不追参数 | 小模型是什么？ / 为什么“小”反而更适合端侧 AI？ | 模型卡、官方框架资料 |
| 10 | 8GB 电脑能做什么？ | 设备自查 → 可做/不宜做 → 第一项低门槛任务 | 8GB 内存电脑，端侧 AI 能先做什么？ / 没有独显，也能开始本地 AI 吗？ | 工具最低要求与实测设备记录 |
| 11 | 本地就等于隐私吗？ | 模型运行位置、联网、权限、日志、上传 → 检查表 | 本地处理就一定更隐私吗？ / 端侧 AI 的隐私，别只看“本地”两个字 | 隐私政策、权限说明和网络行为，不作绝对承诺 |
| 12 | 首次体验该选哪个设备？ | 任务 → Android/Windows/macOS 对比 → 选择建议 | 第一次本地 AI 体验，手机还是电脑？ / Windows、macOS、Android 怎么选 | 平台官方支持范围 |
| 13 | 近期哪些更新值得普通人关心？ | 只选 3–5 项 → 对谁有影响 → 是否已可用 → 限制 | 端侧 AI 两周情报：只看真正影响普通用户的更新 | 当天的一手公告、Release、文档；无可靠素材则延期 |
| 14 | 想开发该先学什么？ | 目标设备 → Python/C++ → 平台分支 → 一个小项目 | 想做端侧 AI，要先学什么语言？ / 不要一上来全学：端侧 AI 语言路线 | 官方框架文档与本项目已整理学习资源 |
| 15 | 读者下一步最需要什么？ | 30 天复盘 → 高频问题 → 选题投票 → 第二阶段预告 | 这 30 天，读者最关心的端侧 AI 问题 / 写端侧 AI 一个月后，我想听听你的问题 | 自有文章数据与读者留言；标明样本边界 |

## 优先资料类型

| 类型 | 适合内容 | 备注 |
| --- | --- | --- |
| 官方文档 | 框架、系统能力、平台限制 | 用于确认功能和支持范围 |
| GitHub 仓库 | 本地推理工具、开源模型、端侧应用 | 关注 README、release、issue、最近提交 |
| 模型卡 | 模型大小、许可证、使用限制 | 注意商用限制和推荐硬件 |
| 实测记录 | 低配置实践、速度、内存、发热 | 尽量记录设备配置 |
| 厂商页面 | Windows/macOS/Android 平台能力 | 区分宣传与可用功能 |

## 第 1 篇：公众号文章结构

对应输出文件：

- `wechat/article-01.md`

### 本次写作记录（2026-08-03）

- 输出：`wechat/article-01.md`，约 1,000 字，状态为 `draft`。
- 开头钩子：从“AI 原本像网页里的聊天框”与实时字幕、会议效果等设备能力的反差切入。
- 读者问题：端侧 AI 与日常使用有什么关系，是否必须购买新设备或学习复杂工具。
- 结构：日常场景 → 端侧/云端/端云协同 → 为什么现在出现 → 三个判断问题 → 设备自查与下一篇预告。
- 行动引导：让读者留言“最希望设备代劳的一件小事”。
- 作者定位：以“我也在学习与核验”的同行者口吻写作；已确认的内容说明来源，设备差异或仍在观察的内容如实标注，不把自己包装成全知专家。
- 本次润色：使用 `wenjing-anti-ai-writing` 的 `edit` 模式，收紧“趋势式”总结和对称句式，改为更具体的设备场景与读者问题；保留“我也还在学”的口吻，以及所有已核验事实、适用条件和来源。
- 开头微调：直接以“端侧 AI 有用的地方”承接云端限制，避免“另一种形式”这类抽象过渡。
- 开头补充：先说明云端 AI 对网络、Token/计算成本和数据处理边界的现实要求，再引出“让设备完成小而频繁任务”的端侧 AI 动机；不将云端 AI 简化为“不安全”。
- 发布交付：新增 `wechat/article-01-publish.md`，仅保留读者可见的标题、正文与资料来源链接；使用 `wechat-anthropic` 作为 tardiformatter 的推荐样式，富文本在浏览器预览后复制到微信后台，不提交 HTML 或浏览器会话图片链接。
- 事实边界：实时字幕、Windows Studio Effects、Gemini Nano 均有明确的设备或功能支持条件；文章不将其泛化为所有 Android 或 Windows 设备都可用。

### 文章目标

让零基础读者知道：AI 过去主要依赖云端，但现在一部分能力正在进入手机、电脑和其他设备；端侧 AI 的价值在于低延迟、隐私、离线和个性化，但它也受到硬件限制。

### 目标读者

- 听过 AI、大模型、ChatGPT，但不知道模型在哪里运行。
- 想知道自己的电脑或手机能不能跑 AI。
- 没有编程基础，不熟悉硬件配置。

### 核心观点

端侧 AI 不是把最大的云端模型塞进设备，而是在设备限制下，让合适的小模型完成合适的本地任务。

### 标题池

1. AI 为什么开始走进手机和电脑？一篇读懂端侧 AI
2. 你的手机里真的有 AI 吗？普通人也能看懂的端侧 AI
3. 不靠云端，AI 能在自己的电脑上跑起来吗？
4. 端侧 AI 到底是什么？从聊天、修图和语音输入讲起
5. 低配置电脑也绕不开 AI：先从端侧 AI 说起

本次推荐标题：**AI 为什么开始走进手机和电脑？一篇读懂端侧 AI**

### 摘要

这是“端侧 AI 观察”系列的第一篇。文章从普通人已经接触过的实时字幕、视频会议美化、写作工具和相册处理讲起，说明 AI、云端 AI、端侧 AI 和端云协同的区别。最后给出一个不需要编程的设备自查清单，帮助读者理解自己的电脑或手机处在什么位置。

### 正文大纲

1. 从日常 AI 功能开头：修图、语音输入、实时字幕、会议美化、相册搜索，让读者先意识到 AI 已经进入设备功能。
2. 解释 AI 在哪里运行：很多 AI 能力仍在云端完成，端侧 AI 关注的是推理是否发生在用户自己的设备上。
3. 用三句话解释 AI：模型是能力包，训练是学习规律，推理是真正使用 AI 的过程。
4. 对比云端 AI、端侧 AI 和端云协同：分别说明运行位置、优点和限制。
5. 说明 AI 走向端侧的原因：小模型变强、设备芯片增强、隐私需求、实时响应、云端成本。
6. 介绍现阶段端侧 AI 能做什么：实时字幕、会议效果、写作辅助、相册搜索、本地总结、私人文件问答和小型离线助手。
7. 说明能力边界：复杂推理、长文本分析、高质量创作、多步骤任务规划仍然更适合云端大模型。
8. 讨论低配置设备：强调不是人人都有高端显卡或旗舰手机，先建立合理硬件分档。
9. 给出简单观察动作：检查系统、内存、存储、显卡或 NPU、离线需求和可接受速度。
10. 结尾引导：后续继续解释模型、训练、推理，并观察端侧 AI 资讯、工具情报、体验记录和读者问答。

### 硬件基线

- 4GB：极低配或老设备，只作为兜底讨论，不作为主流基线。
- 8GB：今天更合理的低配起点，可以观察和尝试轻量工具。
- 16GB：普通电脑更舒服的基础线，可以承载更多本地 AI 体验。
- 32GB 及以上：更适合继续观察本地模型、长一点的上下文和更复杂的任务。
- 独显、NPU、高端手机：作为进阶观察对象，不作为理解端侧 AI 的前提。

### 实践插入点

第一篇不做复杂实践，只做“设备自查”：

- 我的设备系统是什么？
- 内存是多少？
- 磁盘剩余多少？
- 是否有独显或 NPU？
- 是否能接受模型下载几百 MB 到 1GB？
- 是否需要完全离线？
- 是否能接受 CPU 推理较慢？

### 排版与配图建议

- 首图：手机、电脑与云端服务器的简洁关系图，文字只保留“本地处理 / 云端处理”。
- 正文配图 1：实时字幕或会议背景虚化的真实设置页截图；发布前确认截图所属设备、系统与功能可用性。
- 正文配图 2：一张“端侧 / 云端 / 端云协同”的三列对比卡片。
- 结尾图：三个自查问题——“设备支不支持？需要联网吗？能省什么麻烦？”

### 写作注意

- 不用“端侧推理框架”“量化格式”“Token/s”等术语轰炸读者。
- 不把端侧 AI 写成万能趋势。
- 每个概念都接一个例子。
- 不默认读者有独显或会命令行。
- 平台目录中的 `article-01.md` 只保留公众号输出内容；标题池、结构、资料来源、排版建议统一放在本文件。

## 来源列表

| 编号 | 类型 | 标题 | 链接 | 发布时间 | 核验日期 | 用途 | 可信度 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 官方文档 | Microsoft Learn：Use local AI with Microsoft Foundry on Windows | https://learn.microsoft.com/en-us/windows/ai/overview | 2026-04-21 | 2026-08-03 | Windows 本地 AI、Windows AI APIs、Foundry Local、Windows ML；性能和模型支持随硬件而异 | 高 |
| S2 | 官方文档 | Android Developers：Gemini Nano | https://developer.android.com/ai/gemini-nano | 2026-04-02 | 2026-08-03 | Gemini Nano 经 AICore 在设备端执行；离线、本地处理与设备支持边界 | 高 |
| S3 | 官方文档 | Google Developers：Google AI Edge | https://developers.google.com/edge | 持续更新 | 2026-07-20 | Google AI Edge、跨平台端侧 AI 工具栈 | 高 |
| S4 | 官方文档 | Apple Developer Documentation：Foundation Models | https://developer.apple.com/documentation/foundationmodels | 持续更新 | 2026-07-20 | Apple Intelligence 相关本地/私有云模型能力 | 高 |
| S5 | 官方文档 | Google Developers：ML Kit GenAI APIs | https://developers.google.com/ml-kit/genai | 持续更新 | 2026-07-20 | Gemini Nano、AICore、本地处理和隐私场景 | 高 |
| S6 | 官方帮助 | Google Help：Live Caption: Caption media & calls on your device | https://support.google.com/accessibility/android/answer/9350862?hl=en | 持续更新 | 2026-08-03 | Android 实时字幕的本地处理、下载语言包、机型与语言限制 | 高 |
| S7 | 官方文档 | Microsoft Learn：Windows Studio Effects Overview | https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/studio-effects | 2026-05-04 | 2026-08-03 | 兼容 NPU 的 Windows 设备上的背景虚化、眼神校正、自动取景与语音聚焦；须有对应硬件与驱动 | 高 |
| S8 | 官方页面 | Apple：Apple Intelligence | https://www.apple.com/apple-intelligence/ | 持续更新 | 2026-07-20 | Apple Intelligence 端侧处理与 Private Cloud Compute 背景 | 高 |
| S9 | 官方帮助 | Apple Support：Use Writing Tools with Apple Intelligence on iPhone | https://support.apple.com/guide/iphone/find-the-right-words-with-writing-tools-iph6f08da1d2/ios | 持续更新 | 2026-07-20 | 写作工具、摘要、校对、改写等日常 AI 示例 | 高 |
| S10 | 官方调查 | Steam Hardware & Software Survey：June 2026 | https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam | 2026-06 | 2026-07-20 | PC 内存分布参考：4GB、8GB、16GB、32GB 占比 | 中高 |
| S11 | 研究机构 | Counterpoint Research：Global Smartphone Average DRAM Hits Record 8.4GB in 2025 | https://counterpointresearch.com/en/insights/Global-Smartphone-Average-DRAM-Hits-Record-8.4GB-in-2025 | 2026-02-26 | 2026-07-20 | 智能手机平均 DRAM 参考 | 中高 |
| S12 | 研究机构 | IDC：How the memory crisis is reshaping the PC and smartphone outlook | https://www.idc.com/resource-center/blog/higher-asps-lower-unit-volumes-how-the-memory-crisis-is-reshaping-the-pc-and-smartphone-outlook/ | 2026-02-26 | 2026-07-20 | 内存价格影响 PC/手机配置，8GB/12GB 档位变化 | 中高 |
| S13 | GitHub 官方课程 | Microsoft：Edge AI for Beginners | https://github.com/microsoft/edgeai-for-beginners | 持续更新 | 2026-08-03 | 端侧 AI 入门课程；覆盖 SLM、优化、部署与本地 Agent | 高 |
| S14 | GitHub 官方教学资料 | Edge Impulse：Embedded Machine Learning Courseware | https://github.com/edgeimpulse/courseware-embedded-machine-learning | 持续更新 | 2026-08-03 | 嵌入式 ML/TinyML 课件、阅读、练习和视频资料 | 高 |
| S15 | GitHub 官方课程 | Arm University：AI on Arm | https://github.com/arm-university/AI-on-Arm | 持续更新 | 2026-08-03 | Raspberry Pi、Arm、量化与云边推理取舍实验 | 高 |
| S16 | GitHub 官方项目 | Google AI Edge Gallery | https://github.com/google-ai-edge/gallery | 持续更新 | 2026-08-03 | 手机上的离线模型体验与端侧 GenAI 应用参考 | 高 |
| S17 | GitHub 官方示例 | Google AI Edge：LiteRT Samples | https://github.com/google-ai-edge/litert-samples | 持续更新 | 2026-08-03 | Android、iOS、Python/Raspberry Pi 的视觉、音频和推理示例 | 高 |
| S18 | GitHub 官方项目 | Google AI Edge：LiteRT | https://github.com/google-ai-edge/litert | 持续更新 | 2026-08-03 | Google 端侧 ML/GenAI 运行时、优化和硬件加速动态 | 高 |
| S19 | GitHub 官方案例库 | Edge Impulse Expert Projects | https://github.com/edgeimpulse/expert-projects | 持续更新 | 2026-08-03 | 视觉、音频、异常检测、手势和机器人项目案例 | 高 |
| S20 | GitHub 资源导航 | crespum/edge-ai：A curated list of resources for embedded AI | https://github.com/crespum/edge-ai | 持续更新 | 2026-08-03 | 嵌入式 AI 的项目、教程、论文与工具线索 | 中 |
| S21 | GitHub 资源导航 | AI-in-Transportation-Lab/awesome-tinyml | https://github.com/gauravfs-14/awesome-tinyml | 持续更新 | 2026-08-03 | TinyML 的库、教程、论文和项目线索 | 中 |
| S22 | GitHub 官方示例 | Google AI Edge：MediaPipe Samples | https://github.com/google-ai-edge/mediapipe-samples | 持续更新 | 2026-08-03 | 跨平台实时媒体与端侧 LLM 示例 | 高 |
| S23 | GitHub 课程教材 | Harvard Edge：CS249r Machine Learning Systems | https://github.com/harvard-edge/cs249r_book | 持续更新 | 2026-08-03 | 云、边缘、移动端和 TinyML 的 ML 系统学习资料 | 高 |
| S24 | GitHub 官方组织 | NVIDIA AI IoT | https://github.com/NVIDIA-AI-IOT | 持续更新 | 2026-08-03 | Jetson、视觉、机器人与边缘 AI 动态跟踪入口 | 高 |

## GitHub 学习与动态跟踪清单

### 课程与教学

- [Microsoft Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)：端侧 AI 系统入门，适合先建立全局认知。
- [Edge Impulse Embedded Machine Learning Courseware](https://github.com/edgeimpulse/courseware-embedded-machine-learning)：偏嵌入式 ML/TinyML 的教学资料，可拆成课程或选题参考。
- [Arm University AI on Arm](https://github.com/arm-university/AI-on-Arm)：偏 Arm 设备优化与实验，适合完成基础科普后继续学习。
- [Harvard CS249r Machine Learning Systems](https://github.com/harvard-edge/cs249r_book)：面向进阶读者的 ML 系统教材，涉及云、边缘、移动端和 TinyML。

### 项目与示例

- [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery)：完整的 Android 端侧 GenAI 应用参考。
- [LiteRT Samples](https://github.com/google-ai-edge/litert-samples)：官方端侧视觉、音频和推理示例。
- [MediaPipe Samples](https://github.com/google-ai-edge/mediapipe-samples)：跨平台实时媒体与端侧 LLM 示例；Android LLM 示例位于 `examples/llm_inference/android`。
- [Edge Impulse Expert Projects](https://github.com/edgeimpulse/expert-projects)：面向真实设备的可复刻案例库。
- [Awesome Edge AI](https://github.com/crespum/edge-ai) 与 [Awesome TinyML](https://github.com/gauravfs-14/awesome-tinyml)：用于继续扩展项目线索。

### 新闻与版本动态

GitHub 不适合作为单一新闻源，但适合追踪一手项目变更。优先关注下列组织或仓库的 **Releases**、**Watch → Custom**、**Issues** 与 **Discussions**：

- [google-ai-edge](https://github.com/google-ai-edge)：LiteRT、MediaPipe、LiteRT-LM、Gallery 等端侧框架和应用动态。
- [LiteRT](https://github.com/google-ai-edge/litert)：GPU/NPU、模型转换、端侧 GenAI 运行时的更新。
- [edgeimpulse](https://github.com/edgeimpulse)：嵌入式 ML、传感器和工业端侧 AI 的教程、工具与案例。
- [NVIDIA-AI-IOT](https://github.com/NVIDIA-AI-IOT)：Jetson、视觉、机器人与边缘 AI 动态。

写资讯时必须回到对应的 Release、提交、官方公告或文档确认；不要将 README 中的路线图、未发布功能或 Issue 讨论写成已上线能力。

## 可引用事实

| 事实 | 来源编号 | 可用于哪些平台 | 备注 |
| --- | --- | --- | --- |
| Windows 已提供本地 AI 相关能力入口，包括 Windows AI APIs、Foundry Local 和 Windows ML | S1 | 微信公众号、掘金 | 作为 Windows 平台背景，不展开教程 |
| Android 的 Gemini Nano 通过 AICore 系统服务运行，强调端侧低延迟并利用设备硬件 | S2 | 微信公众号 | 注意设备和系统支持边界 |
| Google AI Edge 定位为构建和部署端侧 ML/AI 的工具栈 | S3 | 微信公众号、掘金 | 可用于后续框架介绍 |
| Apple Foundation Models 框架提供 Apple Intelligence 相关模型能力入口 | S4 | 微信公众号、掘金 | 不在第一篇展开开发细节 |
| ML Kit GenAI APIs 基于 AICore 和 Gemini Nano，强调本地处理与隐私场景 | S5 | 微信公众号 | 可用于 Android 场景说明 |
| Android Live Caption 可以为设备上的媒体和通话语音生成字幕 | S6 | 微信公众号 | 作为普通用户已接触端侧/本地 AI 能力的例子 |
| Windows Studio Effects 在兼容 NPU 的 Windows 设备上提供背景虚化、眼神校正、自动取景、语音聚焦等 AI 效果 | S7 | 微信公众号 | 作为 PC 端侧 AI 场景例子 |
| Apple Intelligence 结合设备端处理和 Private Cloud Compute，写作工具可用于校对、改写和摘要 | S8/S9 | 微信公众号 | 用于说明端云协同，不写成完全本地 |
| Steam 2026 年 6 月硬件调查中，4GB 系统内存为 1.44%，8GB 为 7.76%，16GB 为 41.57%，32GB 为 36.79% | S10 | 微信公众号 | Steam 样本偏游戏用户，不代表全体 PC，但可说明 4GB 已非常边缘 |
| Counterpoint 报告称 2025 年 12 月全球智能手机平均 DRAM 达 8.4GB | S11 | 微信公众号 | 用于修正 Android/手机硬件基线 |
| IDC 提到受内存价格影响，原本 12GB/256GB 的手机可能以 8GB/128GB 配置上市，低端市场受冲击更大 | S12 | 微信公众号 | 用于说明 8GB 更像当下低配/基础档，4GB 不宜作为主流假设 |
| 端侧 AI 不等同于云端大模型完整本地化，需要根据设备能力选择任务和模型 | S1-S5 | 微信公众号 | 属于基于多来源的项目判断 |

## 不确定信息

- 第一篇实践工具选择。
- 适合极低配/老设备的替代观察方案。
- Android 端最低可接受设备配置。
