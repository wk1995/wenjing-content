# Third-party provenance

## Local skill

- Path: `.codex/skills/wenjing-anti-ai-writing/`
- Purpose: Chinese WeChat and self-media editing workflow that reduces formulaic AI-sounding prose while preserving facts and author voice.

## Consulted upstream sources

| Repository | Fixed revision | License | Local use and modification boundary |
| --- | --- | --- | --- |
| [yanyintingyou/stop-slop-cn-en](https://github.com/yanyintingyou/stop-slop-cn-en) | `6a4f1521cc2ad255fe7dd5271f8e47a30be0237d` | MIT | Consulted for Chinese/English anti-slop positioning and WeChat-specific applicability. This skill contains an independently written, shorter Chinese workflow and checklist; no upstream skill text or packaged files are copied. |
| [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | `ae1ecbebf09f45b67d2cd1e1c902c4b240e770fc` | MIT | Consulted for the audit/edit/rewrite mode split, targeted-edit principle, and second-pass review. This skill re-expresses those workflow ideas for this repository and does not include upstream code, corpus, detector, or word lists. |

## Runtime boundary

- This is a Markdown-only local skill. It contains no executable code, network calls, credentials, corpora, or external-service dependency.
- It is a writing-quality workflow, not a tool for evading AI-authorship detectors or making unverifiable claims.
