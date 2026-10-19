# 资料来源

---
template: project/sources
template_version: 2026-07-16
status: draft
---

## 资料原则

- 仓库 star、许可证、最近推送日期以 2026-10-15 通过 GitHub API 读取的仓库元数据为准。
- Skill 是否可安装，以同日 WorkBuddy 技能检索结果为准。
- 二手文章只用于发现项目，不作为 star、许可证或效果结论的依据。
- 本次没有在本机克隆、安装或运行下列模型。听到的效果、耗时和显存都不记为已验证事实。

## 可引用事实

核验日期：2026-10-15。分支基线为 `main` 的 `2919039`。

| 编号 | 主体 | 链接 | 支持的结论 | 适用边界 |
| --- | --- | --- | --- | --- |
| S1 | RVC WebUI | https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI | 38,743 star；MIT；最近推送 2026-08-04。仓库自述可用不超过 10 分钟语音训练声音转换模型。 | 声音转换，不是从歌词直接唱完整首歌。 |
| S2 | so-vits-svc | https://github.com/svc-develop-team/so-vits-svc | 28,076 star；AGPL-3.0；最近推送 2023-11-11。 | 歌声转换老项目。近期无推送，不作为现行首选。 |
| S3 | Applio | https://github.com/IAHispano/Applio | 3,832 star；MIT；最近推送 2026-10-14。定位为易用的高质量声音转换工具。 | 许可证字段是 MIT。官方仓库另有 Terms of Use，使用前要单独读。 |
| S4 | SoulX-Singer | https://github.com/Soul-AILab/SoulX-Singer | 1,006 star；Apache-2.0；最近推送 2026-05-29。官方推理代码，定位为零样本歌声合成。 | 只确认仓库定位和许可证。音质、语言和 Mac 可运行性本次未实测。 |
| S5 | ACE-Step 1.5 | https://github.com/ace-step/ACE-Step-1.5 | 13,575 star；MIT；最近推送 2026-10-11。仓库自述支持 Mac、AMD、Intel 和 CUDA 上的本地音乐生成。 | “优于几乎所有商业方案”是仓库自述，不是本项目实测。 |
| S6 | ACE-Step | https://github.com/ace-step/ACE-Step | 4,933 star；Apache-2.0；最近推送 2026-02-15。 | 1.5 的前代仓库。新工作默认看 S5。 |
| S7 | YuE | https://github.com/multimodal-art-projection/YuE | 11,962 star；Apache-2.0；最近推送 2026-10-06。仓库自述 YuE2 支持符号规划、零样本翻唱和音乐编辑。 | 翻唱能力以仓库说明为准，本次未实测。 |
| S8 | DiffSinger（OpenVPI） | https://github.com/openvpi/DiffSinger | 3,221 star；Apache-2.0；最近推送 2026-10-13。基于浅扩散的歌声合成系统。 | 按谱合成路线。数据标注和声库制作成本本次未评估。 |
| S9 | ultimate-rvc | https://github.com/JackismyShephard/ultimate-rvc | 331 star；MIT；最近推送 2026-10-11。用 RVC 做翻唱和语音内容。 | 社区封装，不是事实标准本体。 |
| S10 | Seed-VC | https://github.com/Plachtaa/seed-vc | 3,895 star；GPL-3.0；最近推送 2025-04-20。零样本语音转换和歌声转换，支持实时。 | GPL-3.0 约束再分发。2025-04 后未见新推送。 |
| S11 | DiffRhythm | https://github.com/ASLP-lab/DiffRhythm | 2,347 star；Apache-2.0；最近推送 2025-11-27。 | 整曲扩散路线候选。本次未读论文，不评价效果。 |
| S12 | MiniMax Skills | https://github.com/MiniMax-AI/skills | 13,702 star；MIT；最近推送 2026-04-18。音乐相关官方 Skill 为 `minimax-music-gen`、`buddy-sings`、`minimax-music-playlist`。 | 生成走 MiniMax API，不是可离线的开源模型。仓库标注 Beta。 |
| S13 | WorkBuddy 可安装 Skill | 会话内技能检索，无公开仓库链接 | 检索到 `beatra-ai-music-creator`、`qinglan-music-workbench`、`mxapi`，分别覆盖写歌、音潮开放平台工作流、经网关调用 Suno 等。 | 均为云端能力。未安装，未验证音质和计费。 |

## 明确不作为事实的内容

- 各项目的音质排名、生成耗时、显存占用。检索中的二手对比未逐条回到 README 或论文。
- SoulX-Singer 是否已在当前 Mac 上可运行。
- 任一 Skill 的单价、额度和生成结果版权归属。使用前以对应平台当时的条款为准。
