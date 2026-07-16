---
name: wenjing-douyin-script
description: Douyin short-video script workflow for Wenjing content projects. Use when the user asks for 抖音脚本, 短视频脚本, 种草视频, 带货脚本, 千川素材, 竞品视频拆解, 爆款拆解, 视频分镜, 口播稿, or Chinese social commerce video scripts.
---

# 文镜抖音脚本

Use this skill to create Douyin short-video scripts, competitor breakdowns, and shot-by-shot storyboards for Wenjing content projects.

## Workflow

1. Collect product and campaign facts: product name, category, selling points, target audience, price, target duration, video type, CTA, and compliance boundaries.
2. If competitor videos are provided, analyze them before writing. Focus on the first 3 seconds, visual hook, copy hook, pacing, product proof, CTA, and compliance risks.
3. If no competitor videos are provided, state that the result is based on general category patterns and ask for videos only when the missing data blocks the task.
4. Generate a reusable formula: hook type, opening sentence pattern, shot rhythm, proof path, selling point order, and CTA.
5. Write the full spoken script and storyboard.
6. Audit for oral delivery, hook strength, timing, platform compliance, and AI-flavored phrasing.

## References

Read these files only when needed:

- `references/analysis-framework.md`: use for competitor video breakdowns and formula extraction.
- `references/script-output.md`: use when generating full scripts and shot tables.
- `references/compliance-checklist.md`: use before finalizing commerce, beauty, health, finance, education, or ad-delivery scripts.

## Video Types

- 种草视频: friend-like recommendation, stronger scene and experience, softer CTA, default 30 seconds.
- 千川投放素材: denser information, direct selling points, harder CTA, default 15 seconds.

## First 3 Seconds

Design the opening as two synchronized hooks:

- Copy hook: pain, data, contradiction, scenario, curiosity, or benefit.
- Visual hook: product stack, abrupt change, action impact, text pop-up, POV scene, unusual result, or high-density first frame.

The first frame must be describable as a paused image that still gives the viewer a reason to keep watching.

## Output

Return in this order unless the user requests a different format:

1. 爆款公式摘要
2. 完整脚本 with estimated timing
3. 分镜表
4. 审校修改清单
5. 合规风险提示

Use this shot table:

```text
| 镜号 | 时长 | 景别 | 画面内容 | 旁白/字幕 | 拍摄建议 |
```
