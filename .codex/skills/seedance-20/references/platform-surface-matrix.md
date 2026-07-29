# Platform Surface Matrix

last_verified: 2026-07-29

Seedance capability claims must be scoped to the product surface. A model-level capability can be gated, renamed, priced differently, or unavailable in a particular account or region.

| Surface | Evidence | Current safe guidance |
| --- | --- | --- |
| ByteDance Seed model page | Official product page | Use for broad multimodal capability framing only. |
| ByteDance Seed launch post | Official launch announcement | Use for the stated reference counts, editing/extension, and 15-second multi-shot product claims; do not convert them into universal API limits. |
| Runway | Official model list | `seedance2`, `seedance2_fast`, and `seedance2_mini` are listed for text, image, or video input. Verify the live API reference for all operational details. |
| fal | Official model page | Text/image/reference-to-video endpoints and Fast variants are publicly listed. Recheck price, duration, resolution, and policy before a production request. |
| Volcengine Ark / BytePlus ModelArk | Official docs and account consoles | Use only after live verification of IDs, entitlement, fields, price, and regional availability. The public documentation may redirect or render values client-side. |
| Other providers and routers | Provider-owned docs | Treat as independent implementations. Never reuse one provider's request shape, billing, or rights terms on another. |

For production guidance, include the surface name, source date, evidence type, and what remains unverified. For real-person references, authorization and provider policy outrank technical support.
