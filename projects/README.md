# 项目目录

所有具体内容项目都放在 `projects/` 下。一个项目对应一个独立文件夹，项目内可以包含多个平台版本。

## 项目导航

- [SSH 分层学习手册](2026-11-ssh-learning/README.md)
- [复制 API Key 时，文案被悄悄换掉](2026-10-clipboard-key-swap/README.md)
- [AI 端侧基础项目](2026-07-ai-on-device-foundation/README.md)
- [《最后的借口》× 芙宁娜角色 PV](%E6%9C%80%E5%90%8E%E7%9A%84%E5%80%9F%E5%8F%A3+%E8%8A%99%E5%AE%81%E5%A8%9Cpv/README.md)

[返回仓库首页](../README.md) · [Obsidian 使用说明](../docs/workflows/obsidian.md)

## 命名

推荐格式：

```text
YYYY-MM-topic-slug
```

示例：

```text
projects/2026-07-edge-ai-intro/
projects/2026-07-local-llm-guide/
```

## 推荐结构

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
└── juejin/
    └── article.md
```

## 归属规则

- `README.md`：项目简介、结构、状态和平台列表。
- `brief.md`：原始需求和内容边界。
- `plan.md`：项目方案、平台拆分、排期和风险。
- `sources.md`：项目资料来源和可引用事实。
- `research/topic-research.md`：选题调研、竞品内容、受众洞察和角度判断。
- `shared/`：跨平台共用的大纲、核心观点、案例和图表说明。
- `assets/`：项目共用素材。大视频和临时下载文件不要提交。
- `{platform}/`：该平台的具体内容文件。

## 创建新项目

从 `templates/project/` 复制项目级模板，再从 `templates/platforms/` 复制需要的平台模板。

