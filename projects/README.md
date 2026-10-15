# 项目目录

所有具体内容项目都放在 `projects/` 下。一个项目对应一个独立文件夹，项目内可以包含多个平台版本。

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
├── juejin/
│   └── article.md
├── channels/
│   └── script.md
├── csdn/
│   └── article.md
├── cnblogs/
│   └── article.md
├── segmentfault/
│   └── article.md
├── infoq/
│   └── article.md
└── oschina/
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

