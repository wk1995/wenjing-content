# Tardiformatter Operation Reference

## What It Is

`tardiai/tardiformatter` is a static browser app for turning Markdown into WeChat-compatible rich text. It is not a CLI package. The app uses Vue 3, `markdown-it`, Highlight.js, Turndown, IndexedDB, Canvas image compression, and inline CSS.

Repository: https://github.com/tardiai/tardiformatter

Online formatter:

- https://tardiformatter.vibcx.com/
- https://tardiformatter.vercel.app/

## Local Run

Use local mode when the online site is unavailable, when testing forked changes, or when avoiding external hosting.

```bash
git clone https://github.com/tardiai/tardiformatter.git
cd tardiformatter
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Rendering Pipeline

The main flow is:

```text
Markdown input
-> preprocessMarkdown()
-> markdown-it render
-> process img:// links from IndexedDB
-> group consecutive images
-> apply selected theme as inline styles
-> preview
-> copyToClipboard()
-> convert image grids to tables
-> convert images to Base64 when possible
-> write text/html and text/plain to clipboard
```

This means Codex should prepare clean Markdown and rely on the browser app for the final rich-text conversion.

## Image Handling

- Pasted or dragged images are compressed in the browser with Canvas, defaulting to max 1920x1920 and quality 0.85.
- Compressed images are saved in browser IndexedDB under the app's image store.
- The editor inserts short `img://...` links for locally stored images.
- Preview resolves `img://...` links to object URLs.
- Copy attempts to convert images to Base64 for WeChat paste compatibility.
- GIF and SVG are kept in their original format.

Practical rule: keep committed Wenjing Markdown on normal paths or URLs. Use browser paste/drag only during final WeChat layout.

## Style Keys

Styles observed in `styles.js`:

| Key | Display name | Best use |
| --- | --- | --- |
| `wechat-default` | 默认公众号风格 | General reliable publishing |
| `latepost-depth` | 晚点风格 | Business analysis and deep reporting |
| `wechat-ft` | 金融时报 | Finance, markets, professional commentary |
| `wechat-anthropic` | Claude | AI, technical essays, polished analysis |
| `wechat-tech` | 技术风格 | Developer tutorials and code-heavy posts |
| `wechat-elegant` | 优雅简约 | Clean general articles |
| `wechat-deepread` | 深度阅读 | Longform analysis |
| `wechat-nyt` | 纽约时报 | News/editorial tone |
| `wechat-jonyive` | Jony Ive | Product/design commentary |
| `wechat-medium` | Medium 长文 | Essay-style writing |
| `wechat-apple` | Apple 极简 | Product narratives and minimalist presentation |
| `kenya-emptiness` | 原研哉·空 | Design/art concept articles |
| `hische-editorial` | Hische·编辑部 | Editorial visual style |
| `ando-concrete` | 安藤·清水 | Architecture/design mood |
| `gaudi-organic` | 高迪·有机 | Organic visual theme |
| `guardian` | Guardian 卫报 | News and public-interest reporting |
| `nikkei` | Nikkei 日経 | Asia business and economics |
| `lemonde` | Le Monde 世界报 | International affairs and commentary |

## Troubleshooting

- If preview is fine but WeChat paste changes layout, paste again after using the app's dedicated copy button; it performs WeChat-specific conversion.
- If image grids break in WeChat, check that the copy step converted grids to tables.
- If images disappear, prefer pasting or dragging image files into tardiformatter before copying to WeChat, or replace them from the WeChat media library after paste.
- If emphasis around Chinese punctuation renders oddly, inspect the preview; the app patches `markdown-it` delimiter scanning for CJK and punctuation cases, but unusual nesting can still be fragile.
- If clipboard copy fails, run the app over HTTP/HTTPS in a modern browser and grant clipboard permission.
