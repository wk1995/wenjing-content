# Seedance 2.0 API and Platform Status

last_verified: 2026-07-29

This is a source-dated routing note, not a static API contract. Recheck the active provider's current documentation or console before implementation.

## Confirmed from current primary sources

- ByteDance's [model page](https://seed.bytedance.com/en/seedance2_0) describes Seedance 2.0 as a multimodal audio-video model accepting text, image, audio, and video inputs.
- ByteDance's [launch post](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch) describes multimodal reference use, editing, extension, 15-second multi-shot output, and input limits of up to 9 images, 3 videos, and 3 audio clips. Those are product claims, not a promise that every provider exposes the same controls.
- Runway's current [model list](https://docs.dev.runwayml.com/guides/models/) lists `seedance2`, `seedance2_fast`, and `seedance2_mini` with text, image, or video input.
- fal's current [Seedance page](https://fal.ai/models/bytedance/seedance-2.0/text-to-video) lists text-to-video, image-to-video, and reference-to-video endpoints, including Fast variants. It also lists 720p audio at $0.3034/second, 720p Fast audio at $0.2419/second, and 1080p audio at $0.682/second as reviewed on 2026-07-29.

## Do not infer

- The Volcengine and BytePlus values in earlier research snapshots are not current implementation values. Verify the authorized console or live official documentation for IDs, pricing, regional availability, and request fields.
- A provider/router exposing a Seedance-branded endpoint does not prove parity with ByteDance, Volcengine, BytePlus, Runway, or fal.
- Product references do not establish consent for real people, brands, voices, or copyrighted material.

## Answer pattern

For platform facts, name the provider, source date, evidence type, and the exact item that still requires a live check. For example: `As of 2026-07-29, Runway's public model list includes seedance2, seedance2_fast, and seedance2_mini; verify the current Runway reference and account before relying on a field, price, or regional entitlement.`
