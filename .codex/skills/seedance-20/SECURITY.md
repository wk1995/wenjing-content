# Security notes

This directory is a workspace runtime skill package: Markdown guidance, JSON examples, schemas, and one local media helper. It stores no credentials and has no telemetry.

## Runtime boundary

- The upstream evaluator, CI configuration, tests, release workflow, and visual assets are intentionally excluded from this copy.
- `scripts/extract_last_frame.py` operates only on a local path supplied by the user; inspect it before use and do not treat its output as an observation unless the client can inspect the media.
- `scripts/validate_runtime.py` uses only the Python standard library and performs local structural checks.
- No script in this copy contacts a provider or reads an API key.

## Agent safety

Skill text directs an agent but is not a trust boundary. Do not provide credentials, private footage, or client material to an untrusted agent. For platform facts, use the primary-source links in `references/source-registry.md`; never treat a stale local reference as a live entitlement, price, or API contract.

The copyright and filter sub-skills are for safe, original rewrites. They must not be used to evade provider moderation, consent requirements, or rights restrictions.
