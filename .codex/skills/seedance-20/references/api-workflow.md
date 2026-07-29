# API Workflow

last_verified: 2026-07-29

Use this reference for implementation planning. It does not provide copy-paste credentials, universal request fields, or a substitute for the active provider's current documentation.

## Surface gate

| Surface | Current source | Must recheck |
| --- | --- | --- |
| ByteDance model pages | Official product and launch pages | Product capability is not API availability. |
| Volcengine Ark | Official docs and authorized console | Model IDs, task schema, entitlement, pricing, region, and reference roles. |
| BytePlus ModelArk | Official docs and authorized console | JavaScript-rendered pages may hide values; verify price, ID, and availability live. |
| Runway | Official [model list](https://docs.dev.runwayml.com/guides/models/) and active API reference | Model-specific fields, duration, upload handling, plans, and regions. |
| fal | Official [Seedance page](https://fal.ai/models/bytedance/seedance-2.0/text-to-video) | Endpoint, price, supported resolution, duration, and account requirements at submission time. |
| Provider/router | Provider-owned docs and console | Everything: endpoint, polling, model ID, billing, file retention, moderation, and rights. |

## Async generation checklist

1. Record provider, source date, model/endpoint, mode, duration, resolution, ratio, prompt version, and reference roles.
2. Submit only with current provider-specific fields and authorized assets.
3. Store the task ID and poll or use the provider's documented wait mechanism.
4. Record the final output URL, errors, moderation result, and observed final frame when available.
5. Reuse only an accepted take or a reviewed final frame as continuation canon.

## Current provider-specific notes

- On Runway, use only the model names and input modes exposed by its current model list; do not transplant Runway fields into other providers.
- On fal, the reviewed page lists standard and Fast text/image/reference-to-video endpoints. Its public pricing is volatile and must be date-stamped in any estimate.
- For Volcengine and BytePlus, this package intentionally withholds current model IDs and pricing because the live pages require a current docs/console verification.
