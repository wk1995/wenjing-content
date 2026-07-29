# Surface Prompt Profiles

Use this reference to keep platform behavior surface-specific. Do not hardcode duration, prompt length, reference counts, tag syntax, edit support, extension support, audio behavior, regions, pricing, or authorization requirements as universal Seedance facts.

## Profile Fields

For the active surface, resolve:

- exact reference-tag convention;
- verified duration range;
- prompt budget;
- supported reference roles;
- timeline syntax;
- edit or extension availability;
- audio behavior;
- known constraints;
- source and verification date.

If the surface is unknown, state that the profile is conservative and avoid unsupported numbers.

## Conservative Generic Profile

Use only when no surface is known:

- plan one compact generation-sized clip at a time;
- keep prompt concise;
- preserve exact user-supplied tags;
- avoid asserting native extend, prompt limits, or reference counts;
- ask for the actual clip or final frame before continuation;
- prefer role-bound references over unsupported feature claims.

## Verified Profile: fal Seedance API

Verified 2026-07-29 from the official fal Seedance page:

- Reference tokens are bracketed: `[Image1]`–`[Image9]`, `[Video1]`–`[Video3]`, and `[Audio1]`–`[Audio3]`.
- Use those exact tokens in fal prompt prose. The `@Image1` syntax used by other interfaces and examples is not a fal substitute.
- Recheck the active endpoint documentation before submission because endpoints, field names, limits, and prices remain volatile.

## Volatile Claim Rule

For current model names, pricing, upload limits, reference counts, regions, endpoint names, or authorization requirements, load source-gated references and verify with dated primary sources before making operational claims.
