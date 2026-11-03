# 用 Obsidian 管理文镜内容

## 打开仓库

1. 在 Obsidian 的库管理界面选择“打开文件夹为仓库（Open folder as vault）”。
2. 选择整个 `wenjing-content/` 文件夹，让 `projects/`、`templates/`、`docs/` 处于同一个库中。
3. 打开[仓库首页](../../README.md)，再从[项目导航](../../projects/README.md)进入项目。可把首页加入核心“书签”插件，方便随时返回。

配置保存在根目录 `.obsidian/`。若打开库时配置尚未加载，关闭并重新打开该库。无需社区插件；现有核心插件开关沿用本机初始化配置。

## 编辑和导航

- 新链接采用相对路径 Markdown 格式，例如 `[资料来源](../sources.md)`；插入链接时选择带目录的目标，避免多个 `README.md`、`article.md` 同名误选。
- 重命名文件时自动更新链接。文件移动或重命名尽量在 Obsidian 中完成，并检查 Git 差异；终端或其他编辑器的移动不保证触发链接更新。
- 默认使用实时预览。长文可借助右侧“大纲”跳转标题，通过“反向链接”查看哪些工作文件引用当前笔记。
- 隐藏文件名形式的行内标题，正文仍保留自己的一级标题。

本仓库保留标准 Markdown 正文，便于在 GitHub 和其他编辑器阅读。发布正文中避免加入 Obsidian 专用的块引用、笔记嵌入或查询语法；内部资料编号与 front matter 仍按各平台交付规则处理。

## 创建内容和管理属性

复制 `templates/project/` 到 `projects/YYYY-MM-topic-slug/`，再复制需要的平台模板。核心“模板”插件只能插入单个模板，不能替代目录复制。

YAML front matter 必须从文件第一行开始，例如：

```yaml
---
template: project/readme
template_version: 2026-11-03
status: drafting
---
```

`template_version` 保留所复制模板的实际版本，不统一改成当天日期。历史项目此次只调整元信息位置，原版本和状态保持原值。若通过属性面板编辑，日期可能被 Obsidian 显示为日期类型；精确维护原始字段可切换到源代码模式。

## 图片和附件

默认粘贴或拖入的附件进入当前笔记旁的 `assets/` 子目录，例如在 `wechat/article.md` 中粘贴图片会保存到 `wechat/assets/`。只在具体项目笔记中导入素材，避免在仓库首页或全局模板里粘贴项目图片。

多个平台共用的素材统一整理到该项目根目录的 `assets/`；在 Obsidian 中移动文件后检查引用是否跟随更新。已有图片可直接用相对路径引用，例如公众号正文引用 `![配图说明](../assets/example.png)`，不必重新导入。

项目资产仍遵循仓库规则：不提交临时下载、大视频、私有素材或密钥；生成素材的提示词、来源和验收记录写进项目 `sources.md` 或对应分镜。附件设置不改变这些归属和提交要求。

## 配置与 Git

共享 `.obsidian/app.json`、`appearance.json` 和 `core-plugins.json`，分别记录通用编辑设置、外观设置及现有核心插件开关。

窗口布局、最近打开文件、热键、主题、社区插件和其他设备状态默认忽略；已有本地 `workspace.json` 保留。`.trash/` 也不提交。同步或更新仓库配置前先关闭 Obsidian，避免应用退出时将内存中的旧设置写回文件。

项目新增后，在[项目导航](../../projects/README.md)补上入口；项目内继续用 README 串联需求、方案、资料和正文。不要为适配库重复保存同一份成稿。

## 官方参考

以下页面于 2026-11-03 核对，说明 Obsidian 的设置与用法；具体界面名称以安装版本为准。

- [管理库](https://help.obsidian.md/manage-vaults)：从现有文件夹打开库。
- [内部链接](https://help.obsidian.md/links)：Markdown 链接、路径和重命名更新。
- [设置](https://help.obsidian.md/settings)：实时预览、新文件位置和链接格式。
- [附件](https://help.obsidian.md/attachments)：附件保存位置。
- [配置文件夹](https://help.obsidian.md/configuration-folder)：`.obsidian/` 的作用。
