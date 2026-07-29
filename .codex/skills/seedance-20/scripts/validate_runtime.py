#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


REQUIRED = (
    "LICENSE",
    "PROVENANCE.md",
    "README.md",
    "SECURITY.md",
    "SKILL.md",
    "agents/openai.yaml",
    "references/source-registry.md",
    "references/api-status.md",
    "references/model-name-map.md",
    "references/platform-surface-matrix.md",
    "scripts/extract_last_frame.py",
)
SOURCE_ONLY = (
    ".github",
    "docs",
    "evals",
    "data",
    "assets",
    "CHANGELOG.md",
    "V6_SEQUENCE_PROMPT_COMPILER_MANIFEST.md",
    "requirements-validation.lock",
    "scripts/eval_run.py",
    "scripts/validate_skills.py",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the vendored Seedance runtime package.")
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing runtime file: {rel}")
    for rel in SOURCE_ONLY:
        if (root / rel).exists():
            errors.append(f"source-only material must not ship in the runtime copy: {rel}")

    registry = root / "references/source-registry.md"
    if registry.exists():
        match = re.search(r"^last_verified:\s*(\d{4}-\d{2}-\d{2})$", registry.read_text(encoding="utf-8"), re.M)
        if not match:
            errors.append("source registry must declare last_verified: YYYY-MM-DD")
        else:
            verified = date.fromisoformat(match.group(1))
            age = (date.today() - verified).days
            if age > 30:
                errors.append(f"source registry is {age} days old; recheck volatile sources before release")

    if errors:
        print("Runtime validation errors:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Runtime validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
