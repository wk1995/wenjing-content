# Model Name Map

last_verified: 2026-07-29

Use the active provider's live documentation before using an ID in code. Names below identify a surface; they do not imply portability.

| Name | Surface | Guidance |
| --- | --- | --- |
| Seedance 2.0 | ByteDance model family | Safe general product name. Do not infer a specific API route. |
| `seedance2` | Runway | Listed on Runway's model page for text, image, or video input. |
| `seedance2_fast` | Runway | Listed on Runway's model page; verify cost and request fields live. |
| `seedance2_mini` | Runway | Listed on Runway's model page; verify access and limits live. |
| `bytedance/seedance-2.0/text-to-video` | fal | Listed as fal's standard text-to-video endpoint. |
| `bytedance/seedance-2.0/image-to-video` | fal | Listed as fal's image-to-video endpoint. |
| `bytedance/seedance-2.0/reference-to-video` | fal | Listed as fal's reference-to-video endpoint. |
| `/fast/` variants of those fal routes | fal | Listed as lower-latency/cost variants; recheck current pricing and capabilities. |
| Volcengine, BytePlus, or other wrapper IDs | Provider-specific | Obtain the exact value from the live official/provider documentation or console. This runtime copy deliberately does not preserve stale IDs. |

`Seedance 2.0 Pro`, `Seedance V2`, and similar labels are ambiguous shorthand. Ask for the provider or normalize only after a live source confirms the intended model. Do not confuse Seedance video with similarly named Seed/Doubao language models or Seedream image models.
