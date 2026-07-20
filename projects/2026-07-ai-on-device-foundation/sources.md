# AI 端侧基础项目资料来源

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

## 优先资料类型

| 类型 | 适合内容 | 备注 |
| --- | --- | --- |
| 官方文档 | 框架、系统能力、平台限制 | 用于确认功能和支持范围 |
| GitHub 仓库 | 本地推理工具、开源模型、端侧应用 | 关注 README、release、issue、最近提交 |
| 模型卡 | 模型大小、许可证、使用限制 | 注意商用限制和推荐硬件 |
| 实测记录 | 低配置实践、速度、内存、发热 | 尽量记录设备配置 |
| 厂商页面 | Windows/macOS/Android 平台能力 | 区分宣传与可用功能 |

## 来源列表

| 编号 | 类型 | 标题 | 链接 | 发布时间 | 核验日期 | 用途 | 可信度 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 官方文档 | Microsoft Learn：Use local AI with Microsoft Foundry on Windows | https://learn.microsoft.com/en-us/windows/ai/overview | 2026-04 左右 | 2026-07-20 | Windows 本地 AI、Windows AI APIs、Foundry Local、Windows ML | 高 |
| S2 | 官方文档 | Android Developers：Gemini Nano | https://developer.android.com/ai/gemini-nano | 2026-04 左右 | 2026-07-20 | Android AICore、Gemini Nano、端侧低延迟 | 高 |
| S3 | 官方文档 | Google Developers：Google AI Edge | https://developers.google.com/edge | 持续更新 | 2026-07-20 | Google AI Edge、跨平台端侧 AI 工具栈 | 高 |
| S4 | 官方文档 | Apple Developer Documentation：Foundation Models | https://developer.apple.com/documentation/foundationmodels | 持续更新 | 2026-07-20 | Apple Intelligence 相关本地/私有云模型能力 | 高 |
| S5 | 官方文档 | Google Developers：ML Kit GenAI APIs | https://developers.google.com/ml-kit/genai | 持续更新 | 2026-07-20 | Gemini Nano、AICore、本地处理和隐私场景 | 高 |
| S6 | 官方帮助 | Google Help：Live Caption: Caption media & calls on your device | https://support.google.com/accessibility/android/answer/9350862 | 持续更新 | 2026-07-20 | Android 实时字幕作为普通人接触端侧 AI 的例子 | 高 |
| S7 | 官方文档 | Microsoft Learn：Windows Studio Effects Overview | https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/studio-effects | 2026-05 左右 | 2026-07-20 | Windows 会议摄像头/麦克风 AI 效果示例 | 高 |
| S8 | 官方页面 | Apple：Apple Intelligence | https://www.apple.com/apple-intelligence/ | 持续更新 | 2026-07-20 | Apple Intelligence 端侧处理与 Private Cloud Compute 背景 | 高 |
| S9 | 官方帮助 | Apple Support：Use Writing Tools with Apple Intelligence on iPhone | https://support.apple.com/guide/iphone/find-the-right-words-with-writing-tools-iph6f08da1d2/ios | 持续更新 | 2026-07-20 | 写作工具、摘要、校对、改写等日常 AI 示例 | 高 |

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
| 端侧 AI 不等同于云端大模型完整本地化，需要根据设备能力选择任务和模型 | S1-S5 | 微信公众号 | 属于基于多来源的项目判断 |

## 不确定信息

- 第一篇实践工具选择。
- 适合 4GB 内存设备的替代实验。
- Android 端最低可接受设备配置。
