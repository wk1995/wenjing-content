# Seedance 2.0 Skill provenance

This directory is a vendored runtime copy and deliberately contains no Git history. This document is the traceability record for the exact source revision.

| Role | GitHub repository | Pinned commit |
| --- | --- | --- |
| Distribution repository used for this copy | [wk1995/seedance-2.0](https://github.com/wk1995/seedance-2.0) | [`6c51262377b96592b9f87a8c8b0219e6335378f7`](https://github.com/wk1995/seedance-2.0/commit/6c51262377b96592b9f87a8c8b0219e6335378f7) |
| Upstream source project | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | [`6c51262377b96592b9f87a8c8b0219e6335378f7`](https://github.com/Emily2040/seedance-2.0/commit/6c51262377b96592b9f87a8c8b0219e6335378f7) |

Refreshed on 2026-07-29 from the distribution repository at the pinned commit above. GitHub identifies `Emily2040/seedance-2.0` as the source project of `wk1995/seedance-2.0`; the stated commit exists in both repositories. On that date, both default branches resolved to `6c51262377b96592b9f87a8c8b0219e6335378f7`.

## Runtime packaging

This workspace intentionally vendors a runtime subset rather than the complete upstream development repository. It retains the skill instructions, active references, structured examples, schemas, and the local frame extractor. It excludes CI, tests, the credential-reading evaluator, release documentation, and README-only image assets. Run `python3 scripts/validate_runtime.py --strict` here; run upstream's full release validation only in a complete checkout of the pinned source revision.

## Update rule

Never update this skill from a moving branch such as `main`. Fetch a specific commit, then update all four provenance fields in `SKILL.md` and the two links in this file together. Retain the upstream MIT license and its attribution when redistributing the copy.
