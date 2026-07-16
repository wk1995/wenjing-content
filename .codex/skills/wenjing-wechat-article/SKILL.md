---
name: wenjing-wechat-article
description: WeChat public account article workflow for Wenjing content projects. Use when the user asks to write, plan, rewrite, polish, title, or format a 微信公众号文章, 微信文章, 自媒体长文, 爆款文章, 教程文章, or long-form Chinese content for official account publishing.
---

# 文镜公众号文章

Use this skill to produce publication-ready WeChat public account articles for the Wenjing repository.

## Workflow

1. Clarify the brief if essential information is missing: topic, reader, goal, angle, word count, references, and call to action.
2. Search or verify current facts when the topic depends on recent products, policies, prices, events, tools, or public claims.
3. Build a short outline before drafting: opening hook, reader problem, core argument, method or examples, summary, CTA.
4. Draft in Chinese with a clear story or tension in the opening. Prefer 1000-1500 Chinese characters unless the user asks otherwise.
5. Generate 3-5 title options after the draft, not before the argument is clear.
6. Add formatting suggestions for WeChat: paragraph breaks, bold emphasis, image positions, quote-worthy lines, and ending prompt.

## Article Pattern

Use this structure by default:

```text
标题

开头：故事、结果、冲突、反常识或问题

问题：读者正在遇到什么具体困境

解释：为什么这个问题值得重视

方法：步骤、清单、案例或操作建议

升华：把方法上升为观点或判断

结尾：总结 + 行动引导
```

## Title Rules

Make titles specific and reader-facing.

- Include pain, result, number, conflict, curiosity, or concrete benefit.
- Avoid empty clickbait that the article cannot deliver.
- For professional topics, keep the title credible rather than noisy.
- Provide a recommended title and alternatives with different angles.

## Style Rules

- Write like a sharp human editor, not a product manual.
- Use concrete scenes and examples before abstract conclusions.
- Keep paragraphs short enough for mobile reading.
- Avoid generic AI phrasing such as "在当今时代", "值得注意的是", "综上所述".
- If making claims from external information, identify the source or explain that it is an inference.

## Output

Return in this order:

1. 推荐标题
2. 备选标题
3. 正文
4. 排版建议
5. 配图建议
