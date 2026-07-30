#!/usr/bin/env python3
"""Build a review draft for the Furina PV from approved local media only.

Copy ``jianying-media-manifest.example.json`` to ``jianying-media-manifest.json``,
replace every placeholder with an absolute approved-media path, then run this
script with ``--dry-run`` followed by a normal run. Existing drafts are protected
unless ``--replace`` is passed deliberately.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

# The upstream Skill writes status emoji. Windows PowerShell may default to GBK,
# which would otherwise turn a successful draft save into UnicodeEncodeError.
for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="replace")


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PROJECT_ROOT.parents[1]
SKILL_ROOT = WORKSPACE_ROOT / ".codex" / "skills" / "jianying-editor-pinned"
DEFAULT_MANIFEST = Path(__file__).with_name("jianying-media-manifest.json")
EXPECTED_DURATION = 224.839
VIDEO_TRACKS = ("V1_Main", "V2_Ambience", "V3_Effects")
AUDIO_TRACKS = ("A1_BGM", "A2_Voice", "A3_SFX")
SUBTITLE_TRACK = "V4_Subtitles"


def seconds(value: float) -> str:
    return f"{value:.3f}s"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument(
        "--drafts-root",
        type=Path,
        help="Optional absolute Jianying draft root. Defaults to Jianying's detected draft folder.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate paths, timing, and track assignments without creating a draft.",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Deliberately replace an existing draft of the same name.",
    )
    return parser.parse_args()


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        example = path.with_name("jianying-media-manifest.example.json")
        raise FileNotFoundError(
            f"Manifest not found: {path}\nCopy {example.name} to {path.name} and fill approved paths."
        )
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Manifest root must be a JSON object.")
    return data


def approved_path(value: Any, label: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty absolute path.")
    path = Path(value)
    if not path.is_absolute():
        raise ValueError(f"{label} must be absolute: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"{label} not found: {path}")
    return path


def as_number(value: Any, label: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{label} must be a number of seconds.")
    if value < 0:
        raise ValueError(f"{label} cannot be negative.")
    return float(value)


def validate_manifest(data: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not isinstance(data.get("draft_name"), str) or not data["draft_name"].strip():
        raise ValueError("draft_name is required.")
    canvas = data.get("canvas")
    if not isinstance(canvas, dict) or not all(isinstance(canvas.get(k), int) for k in ("width", "height")):
        raise ValueError("canvas must contain integer width and height.")
    if canvas["width"] <= 0 or canvas["height"] <= 0:
        raise ValueError("canvas dimensions must be positive.")

    approved_path(data.get("bgm_path"), "bgm_path")
    subtitle = data.get("subtitle_srt", "video/芙宁娜PV字幕文件.srt")
    subtitle_path = Path(subtitle)
    if not subtitle_path.is_absolute():
        subtitle_path = PROJECT_ROOT / subtitle_path
    if not subtitle_path.is_file():
        raise FileNotFoundError(f"subtitle_srt not found: {subtitle_path}")

    clips = data.get("clips")
    if not isinstance(clips, list) or not clips:
        raise ValueError("clips must be a non-empty array.")
    seen_slots: set[str] = set()
    for clip in clips:
        if not isinstance(clip, dict):
            raise ValueError("Every clips item must be an object.")
        slot = clip.get("slot")
        if not isinstance(slot, str) or not slot:
            raise ValueError("Each clip needs a non-empty slot.")
        if slot in seen_slots:
            raise ValueError(f"Duplicate clip slot: {slot}")
        seen_slots.add(slot)
        if clip.get("track") not in VIDEO_TRACKS:
            raise ValueError(f"Clip {slot} has unsupported video track: {clip.get('track')}")
        approved_path(clip.get("path"), f"clip {slot} path")
        start = as_number(clip.get("start"), f"clip {slot} start")
        duration = as_number(clip.get("duration"), f"clip {slot} duration")
        as_number(clip.get("source_start", 0), f"clip {slot} source_start")
        if duration <= 0 or start + duration > EXPECTED_DURATION + 0.001:
            raise ValueError(f"Clip {slot} falls outside the {EXPECTED_DURATION:.3f}s master timeline.")

    overlays = data.get("audio_overlays", [])
    if not isinstance(overlays, list):
        raise ValueError("audio_overlays must be an array.")
    for index, overlay in enumerate(overlays, start=1):
        if not isinstance(overlay, dict) or overlay.get("track") not in AUDIO_TRACKS[1:]:
            raise ValueError(f"audio_overlays[{index}] must use A2_Voice or A3_SFX.")
        approved_path(overlay.get("path"), f"audio_overlays[{index}] path")
        start = as_number(overlay.get("start"), f"audio_overlays[{index}] start")
        duration = as_number(overlay.get("duration"), f"audio_overlays[{index}] duration")
        if duration <= 0 or start + duration > EXPECTED_DURATION + 0.001:
            raise ValueError(f"audio_overlays[{index}] falls outside the master timeline.")
    return clips, overlays


def build_draft(data: dict[str, Any], clips: list[dict[str, Any]], overlays: list[dict[str, Any]], drafts_root: Path | None, replace: bool) -> None:
    if not SKILL_ROOT.is_dir():
        raise FileNotFoundError(f"Jianying Skill not installed at {SKILL_ROOT}")
    os.environ.setdefault("JY_SKILL_ROOT", str(SKILL_ROOT))
    scripts_path = SKILL_ROOT / "scripts"
    if str(scripts_path) not in sys.path:
        sys.path.insert(0, str(scripts_path))

    from jy_wrapper import JyProject, draft  # noqa: PLC0415

    canvas = data["canvas"]
    project = JyProject(
        data["draft_name"],
        width=canvas["width"],
        height=canvas["height"],
        drafts_root=str(drafts_root) if drafts_root else None,
        overwrite=replace,
    )
    for track in VIDEO_TRACKS:
        project._ensure_track(draft.TrackType.video, track)
    for track in AUDIO_TRACKS:
        project._ensure_track(draft.TrackType.audio, track)

    bgm = project.add_audio_safe(str(Path(data["bgm_path"])), "0s", seconds(EXPECTED_DURATION), "A1_BGM")
    if bgm is None:
        raise RuntimeError("Could not add BGM; inspect the source file and Jianying runtime.")

    for clip in sorted(clips, key=lambda item: (float(item["start"]), item["slot"])):
        segment = project.add_media_safe(
            str(Path(clip["path"])),
            seconds(float(clip["start"])),
            seconds(float(clip["duration"])),
            clip["track"],
            source_start=seconds(float(clip.get("source_start", 0))),
        )
        if segment is None:
            raise RuntimeError(f"Could not add clip {clip['slot']}: {clip['path']}")

    for overlay in overlays:
        segment = project.add_audio_safe(
            str(Path(overlay["path"])),
            seconds(float(overlay["start"])),
            seconds(float(overlay["duration"])),
            overlay["track"],
        )
        if segment is None:
            raise RuntimeError(f"Could not add audio overlay: {overlay['path']}")

    subtitle = Path(data.get("subtitle_srt", "video/芙宁娜PV字幕文件.srt"))
    subtitle_path = subtitle if subtitle.is_absolute() else PROJECT_ROOT / subtitle
    project.script.import_srt(str(subtitle_path), SUBTITLE_TRACK)
    result = project.save()
    print(json.dumps(result, ensure_ascii=False))
    print("Manual review required: subtitle safe area; 2:31-2:45 BGM ducking; native effects; final export.")


def main() -> None:
    args = parse_args()
    manifest = load_manifest(args.manifest)
    clips, overlays = validate_manifest(manifest)
    print(f"Validated {len(clips)} video clips and {len(overlays)} audio overlays for {EXPECTED_DURATION:.3f}s.")
    if args.dry_run:
        print("Dry run passed; no Jianying draft was created.")
        return
    if args.drafts_root and not args.drafts_root.is_absolute():
        raise ValueError("--drafts-root must be an absolute path.")
    build_draft(manifest, clips, overlays, args.drafts_root, args.replace)


if __name__ == "__main__":
    main()
