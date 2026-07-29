# Seedance 2.0 runtime skill

This is the trimmed, commit-pinned runtime copy used by the `wenjing-content` workspace. It contains the root skill, sub-skills, active references, structured examples, schemas, and the optional local final-frame extractor.

It deliberately does **not** contain the upstream repository's CI workflow, network-capable evaluator, test suite, release documentation, visual-gallery assets, or source-only validation scripts. Those files belong to upstream development and must not be presented as runnable validation for this workspace copy.

## Provenance and updates

The exact upstream and distribution repositories, plus the immutable commit, are recorded in [PROVENANCE.md](PROVENANCE.md). On 2026-07-29, both repositories' default branch resolved to that same commit.

To refresh this runtime copy:

1. Fetch a specific upstream commit, never a moving branch.
2. Validate the complete upstream checkout there.
3. Copy only runtime material, then update `PROVENANCE.md` and the four provenance fields in `SKILL.md` together.
4. Recheck volatile platform sources before changing factual API, model-ID, pricing, or availability guidance.

## Local validation

Run the dependency-free runtime check from this directory:

```bash
python3 scripts/validate_runtime.py --strict
```

The check verifies the runtime boundary, required skill files, and that the source registry is not older than 30 days. It makes no network calls and never reads credentials.

For model capabilities and platform-specific workflow guidance, start with [SKILL.md](SKILL.md). Use the cited live sources in `references/source-registry.md` before quoting volatile values.
