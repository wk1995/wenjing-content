# 项目来源与文件索引

---
template: project/sources
template_version: 2026-07-16
status: draft
---

## 项目主线文件

- [video/芙宁娜PV字幕文件.srt](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E5%AD%97%E5%B9%95%E6%96%87%E4%BB%B6.srt)
- [video/芙宁娜角色PV最终定稿-口径统一版.md](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E8%A7%92%E8%89%B2PV%E6%9C%80%E7%BB%88%E5%AE%9A%E7%A8%BF-%E5%8F%A3%E5%BE%84%E7%BB%9F%E4%B8%80%E7%89%88.md)
- [video/芙宁娜PV时间轴剪辑脚本.xlsx](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E6%97%B6%E9%97%B4%E8%BD%B4%E5%89%AA%E8%BE%91%E8%84%9A%E6%9C%AC.xlsx)
- [video/芙宁娜PV歌词卡点表.xlsx](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E6%AD%8C%E8%AF%8D%E5%8D%A1%E7%82%B9%E8%A1%A8.xlsx)
- [video/芙宁娜PV字幕时间轴.xlsx](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E5%AD%97%E5%B9%95%E6%97%B6%E9%97%B4%E8%BD%B4.xlsx)
- [video/芙宁娜PV字幕设计规范.docx](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E5%AD%97%E5%B9%95%E8%AE%BE%E8%AE%A1%E8%A7%84%E8%8C%83.docx)
- [video/芙宁娜PV素材需求清单.xlsx](video/%E8%8A%99%E5%AE%81%E5%A8%9CPV%E7%B4%A0%E6%9D%90%E9%9C%80%E6%B1%82%E6%B8%85%E5%8D%95.xlsx)

## 平台输出文件

- [douyin/script.md](douyin/script.md)：按经核验音频 `3:44.84` 优化的抖音短视频脚本
- [douyin/storyboard.md](douyin/storyboard.md)：按经核验音频 `3:44.84` 优化的抖音分镜表

## 关键来源与依据

- 创意方向：源于角色剧情语境（自定义写作）
- 技术与节奏依据：`video/芙宁娜PV歌词卡点表.xlsx`、`video/芙宁娜PV时间轴剪辑脚本.xlsx`
- 口径定义来源：`video/芙宁娜角色PV最终定稿-口径统一版.md`
- 音频来源：用户提供 `C:/Users/wk/Desktop/7月25日.mp4`；核验日期：2026-07-29；音频流为 AAC、44.1 kHz、双声道，容器时长为 `224.839002` 秒（执行时长 `3:44.84`）。
- 执行时长依据：上述 MP4 的媒体元数据；旧版 `约3:10` 预估不再作为剪辑执行时长。
- 字幕同步说明：`video/芙宁娜PV字幕文件.srt`、字幕时间轴、剪辑时间轴、歌词卡点表、素材需求清单与工程规范已同步；最终句位于 `3:31-3:40`，`3:40-3:44.84` 为无字幕的原曲尾音。

## 官方参考视频与下载记录

- [S1｜Bilibili 原神官方账号：《原神》芙宁娜角色PV——「戏中人」](https://www.bilibili.com/video/BV1oa4y1X7Zt/)；核验日期：2026-07-30。用于参考舞台、剧场与角色叙事的视觉语言；已下载该条目的 4 个官方多语言分集，文件位于 `_temp/downloads/BiliBili/`，不纳入 Git。
- [S2｜Bilibili 原神官方账号：《原神》角色演示-「芙宁娜：世界皆舞台」](https://www.bilibili.com/video/BV1ZG411X71k/)；核验日期：2026-07-30。用于参考动作、音乐剧节奏与舞台调度；已下载该条目的 4 个官方多语言分集，文件位于 `_temp/downloads/BiliBili/`，不纳入 Git。
- 微博官方账号：[原神](https://weibo.com/ysmihoyo?tabtype=home)；核验日期：2026-07-30。已确认账号页面，但公开搜索无法取得可核验的上述两条对应视频原帖，因此本次未下载微博素材，也没有使用搬运账号内容。
- 下载条件：本次公开素材通过项目工具下载；未登录状态可取得的最高可用清晰度为 1080P，未取得 1080P 60 帧会员规格。公开下载只用于内部参考，不代表已获得剪辑、二创发布或再分发授权。

## 可引用内容

- S1、S2 仅作为内部镜头与节奏参考；未经另行取得授权或确认适用许可，不将其中的画面、音乐、音频或字幕直接用于成片发布。
- 本项目对外成稿仍以内部脚本版本与时间轴文件为准。

## 项目工具

- [tools/furina_pv_downloader.py](tools/furina_pv_downloader.py)：下载公开的芙宁娜 PV 参考链接；默认输出到项目 `_temp/downloads/`，默认仅下载视频主分集，使用 `--playlist` 才下载多语言分集，不提交下载媒体。
- [tools/furina_pv_urls.example.txt](tools/furina_pv_urls.example.txt)：已核验的官方 B 站参考链接清单；微博链接仅在取得具体、可核验的公开视频原帖后添加。
- [tools/local_srt_from_media.py](tools/local_srt_from_media.py)：使用本地 `faster-whisper` 从音视频生成 SRT；歌曲或 PV 的演唱识别结果必须人工核对。
- [tools/media_tool_gui.py](tools/media_tool_gui.py) 与 [tools/run_media_tool_gui.bat](tools/run_media_tool_gui.bat)：项目工具图形界面及 Windows 启动入口。

运行时依赖不随项目提交：下载工具需要 `yt-dlp`；本地转写需要 `faster-whisper`；图形界面的拖拽支持可选安装 `tkinterdnd2`。

### 剪映草稿自动搭建（2026-07-30）

- 本仓库已纳入本地 Skill：`.codex/skills/jianying-editor-pinned/`；来源、固定 commit、MIT 许可证与本地修改边界见其 `PROVENANCE.md`。本地镜像与上游在纳入时均为 commit `f421c8a036f4fda888a83b38fc90bb9c00d6faa9`。
- [tools/build_jianying_draft.py](tools/build_jianying_draft.py)：从已获准的本地素材、固定 `3:44.839` 秒主时间轴与本项目 SRT 创建供审片的国内剪映专业版草稿。默认不会覆盖同名草稿；只有显式传入 `--replace` 才会替换。
- [tools/jianying-media-manifest.example.json](tools/jianying-media-manifest.example.json)：素材映射模板。实际文件须复制为 `jianying-media-manifest.json`，使用绝对路径填写，且已被 `.gitignore` 排除；不得填入未获准发布的素材。
- 自动化仅完成已列素材的编排和 SRT 导入；`2:31-2:45` 的 BGM 压低、原生特效资源 ID、字幕安全区与最终导出必须在剪映内审片确认。未因本次工程准备调用 Pixelle-Video 或生成任何 AI 角色/补画面素材。

## 素材清单（内部）

| 类型 | 文件 | 说明 |
| --- | --- | --- |
| 抖音脚本 | `douyin/script.md` | 当前审阅版，按 `3:44.84` 的实际音频优化 |
| 抖音分镜 | `douyin/storyboard.md` | 当前审阅版，补足 3:10 后尾段并给出字幕后移建议 |
| 纯文本脚本 | `video/芙宁娜角色PV优化版剪辑脚本-chatgpt.docx` | 优化版镜头草稿，旧版时长约 `3:10` |
| 备选文本 | `video/芙宁娜角色PV剪辑脚本-deepseek.docx` | 备选镜头/口播草稿，旧版时长约 `3:10` |
| 项目说明 | `video/原脚本优化分析.docx` | 改稿依据 |
| 规范文档 | `video/芙宁娜PV剪映工程搭建规范.xlsx` | 剪辑工程设置 |
| 创意说明 | `video/芙宁娜PV创意说明.xlsx` | 叙事定位与调性 |
