# Runtime compatibility

This package is vendored inside `wenjing-content` as a workspace-local Codex skill. It is not a universal installer and does not claim support for every agent client.

## Included runtime material

| Material | Purpose |
| --- | --- |
| `SKILL.md` and `skills/*/SKILL.md` | Root routing and specialized guidance |
| `references/` | Progressive-disclosure reference material |
| `examples/`, `schemas/`, `validation/` | Optional structured planning examples |
| `agents/openai.yaml` | Codex UI metadata |
| `scripts/extract_last_frame.py` | Optional local helper for a supplied video path |
| `scripts/validate_runtime.py` | Dependency-free package-boundary validation |

## Boundaries

- This copy is loaded from `.codex/skills/seedance-20/`; do not run an installer or write it into a user-level skills directory as part of ordinary content work.
- The package is not proof that every listed video provider is available to the current client or account.
- Before changing factual provider guidance, consult the dated primary-source links in `source-registry.md` and preserve the verification date in the output.
