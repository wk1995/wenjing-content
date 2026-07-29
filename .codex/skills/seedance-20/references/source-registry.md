# Source Registry

last_verified: 2026-07-29

Use this registry before making factual claims about Seedance 2.0. It records a live review of the sources below on the stated date, not a guarantee of account access or unchanged provider behavior.

## Evidence labels

| Label | Meaning | Required wording |
| --- | --- | --- |
| `confirmed` | Directly visible on a primary source at the verification date. | `Public sources state … as of [date].` |
| `volatile` | Can change by surface, account, region, or release. | `Recheck before giving numbers or promises.` |
| `field-observed` | Practitioner pattern, not platform truth. | `Field observation, not guaranteed platform behavior.` |
| `unverified` | Not confirmed by a primary source. | `Requires testing or owner confirmation.` |
| `internal` | Workspace guidance. | `Use as workflow guidance, not external fact.` |

## Live-reviewed sources

| Topic | Source | Evidence | Verification note | Claim boundary |
| --- | --- | --- | --- | --- |
| Core model capability | ByteDance Seed [model page](https://seed.bytedance.com/en/seedance2_0) and [launch post](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch) | `confirmed` | Reviewed 2026-07-29. The pages describe text, image, audio, and video inputs; multimodal references; editing/extension; and up to 9 images, 3 videos, and 3 audio clips in the launch announcement. | Product-level capability only, not an entitlement or API contract. |
| Runway API model names | [Runway model list](https://docs.dev.runwayml.com/guides/models/) | `confirmed` | Reviewed 2026-07-29. The list includes `seedance2`, `seedance2_fast`, and `seedance2_mini` for text, image, or video input. | Runway-only names and behavior. Recheck pricing, regional availability, and request fields before implementation. |
| fal endpoints, reference syntax, and pricing | [fal Seedance 2.0 API page](https://fal.ai/models/bytedance/seedance-2.0/text-to-video) | `volatile` | Reviewed 2026-07-29. The page lists text-, image-, and reference-to-video endpoints, Fast variants, public per-second prices, and bracketed prompt tokens `[Image1]`, `[Video1]`, and `[Audio1]`. | Use fal's bracketed tokens only on fal; quote values only with this date, the exact endpoint and resolution; recheck immediately before spending or coding. |
| Volcengine / Ark workflow | [Volcengine Ark documentation](https://docs.volcengine.com/docs/82379/1520757?lang=zh) | `volatile` | The public page redirected during the 2026-07-29 review; do not infer current model IDs, entitlement, pricing, or request fields from this runtime copy. | Verify in the live docs and authorized console. |
| BytePlus ModelArk pricing | [BytePlus pricing documentation](https://docs.byteplus.com/en/docs/ModelArk/1544106) | `volatile` | Reviewed 2026-07-29. The publicly fetched page was JavaScript-rendered and did not expose a reliable Seedance price table. | Never quote BytePlus prices or model IDs without a live page or console verification. |
| Other providers and routers | Provider-owned docs or product pages | `unverified` | This runtime copy does not maintain a current provider directory. | Treat every endpoint, model ID, price, moderation rule, and output-rights term as provider-specific and verify it live. |

## Claim rules

- For prices, quotas, model IDs, regions, limits, and account access, use the active provider's official page or console at answer time.
- Preserve the source date, provider, model/endpoint, currency, and relevant resolution or duration whenever quoting a price.
- Do not turn launch examples, community prompts, or a provider wrapper's behavior into universal Seedance guarantees.
- Real-person images, voices, and likenesses require authorization even where a surface technically accepts the asset.
