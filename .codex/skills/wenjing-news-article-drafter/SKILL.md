---
name: wenjing-news-article-drafter
description: Research and draft sourced Chinese Markdown articles for Wenjing content projects from a topic, date range, keywords, or source list. Use when the user asks to collect recent news, GitHub repositories, official announcements, papers, product updates, Edge AI updates, AI/tooling trends, weekly digests, topic research, or source-backed articles, then turn them into WeChat, Juejin, or shared project drafts with numbered citations such as [S1].
---

# 文镜资料型文章草稿

Use this skill to turn a topic and time range into a sourced article draft inside the Wenjing content repository.

## Repository Placement

- Put all concrete work under `projects/{project-slug}/`.
- Record source material in `projects/{project-slug}/sources.md`.
- Record topic research in `projects/{project-slug}/research/topic-research.md`.
- Put cross-platform article structure in `projects/{project-slug}/shared/outline.md`.
- Draft WeChat articles in `projects/{project-slug}/wechat/article.md`.
- Draft developer-facing articles in `projects/{project-slug}/juejin/article.md`.
- Do not put project-specific research or article drafts in `templates/`.

## Workflow

1. Identify the topic, date range, target platform, reader, and requested length.
   - If the user says "端侧 AI", "Edge AI", "Android AI", "on-device AI", or similar, treat official Android, Google AI, model, browser, MediaPipe, WebNN, ONNX Runtime, llama.cpp, MLC, and mobile hardware updates as high-priority sources.
   - If the user asks for a weekly/monthly digest, organize sources by time and importance.
   - If there is no project directory yet, create or use `projects/YYYY-MM-topic-slug/` and follow the repository templates.
2. Collect and verify sources before drafting.
   - Prefer official documentation, release notes, GitHub repositories, papers, model cards, company blogs, standards pages, or product pages.
   - Use secondary articles only as discovery leads unless they contain original reporting that is directly relevant.
   - For recent or time-sensitive claims, verify concrete publication dates and record the check date.
3. Fill project research files.
   - Add source rows to `sources.md` using IDs like `S1`, `S2`, `S3`.
   - Add key facts to `sources.md` with the source IDs that support them.
   - Add audience insights, competing/reference content, keyword trails, and viable angles to `research/topic-research.md` when the task includes research or topic planning.
4. Draft the article in Markdown.
   - Keep source annotations in the body as `[S1]`, `[S2]`, etc.
   - Explain what happened, why it matters now, what readers can do, and what remains uncertain.
   - Separate confirmed facts from interpretation.
   - Do not copy long passages from sources.
5. Adapt the draft to the platform.
   - WeChat: use `templates/platforms/wechat/article.md` or `edge-ai-article.md`, with a scene-led opening and mobile-friendly paragraphs.
   - Juejin: use `templates/platforms/juejin/article.md`, with reproducible steps, code/environment notes, and engineering caveats.
   - Shared planning: put reusable structure and phrasing in `shared/outline.md` and `shared/key-points.md`.
6. Keep the article as a draft unless the user explicitly asks to publish or mark it ready.

## Length Presets

- Short: about 800-1200 Chinese characters, usually 3-5 sections.
- Medium: about 1500-2500 Chinese characters, with clear sections and source-backed claims.
- Long: about 3000-5000 Chinese characters, with analysis, project notes, examples, and follow-up observations.
- If the user gives an exact word or character count, prioritize that over these presets.

## Source ID Pattern

Use this pattern in `sources.md` and the article body:

```text
S1: Official docs or announcement
S2: GitHub repository or release
S3: Paper, model card, or standards page
```

In article prose:

```text
Google 在某日期发布了某项能力，核心变化是……[S1]
该项目的 GitHub release 显示，最新版本增加了……[S2]
```

## Article Requirements

- Keep numbered citations in the body and make them match `sources.md`.
- Prefer primary sources for all key claims.
- Treat community discussion as a trend signal, not a confirmed fact.
- Include uncertainty, limits, and what still needs observation.
- Preserve repository front matter and `status: draft` until the user asks otherwise.
- For current facts, use exact dates instead of vague "recently" when possible.

## Validation

Before saying the draft is ready:

- Confirm `sources.md` contains all cited source IDs.
- Search the draft for citation markers such as `[S1]`.
- Confirm every important factual claim has a nearby citation.
- Confirm project-specific files are under `projects/{project-slug}/`.
- If the article contains commands or code, check that they are plausible and note anything untested.
