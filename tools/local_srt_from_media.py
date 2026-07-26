#!/usr/bin/env python3
"""
Generate local SRT subtitle files from audio/video files.

This is a local alternative to editor/VIP subtitle export features:
it does not call Jianying/CapCut, and does not send media to a cloud API.
It uses faster-whisper for speech recognition and writes standard .srt files.

Install dependency:
  python -m pip install -U faster-whisper

Examples:
  python tools/local_srt_from_media.py input.mp4
  python tools/local_srt_from_media.py input.mp4 -o subtitles --model medium --language zh
  python tools/local_srt_from_media.py "D:/videos" --recursive --model large-v3
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path
from typing import Iterable, Iterator


MEDIA_EXTENSIONS = {
    ".aac",
    ".avi",
    ".flac",
    ".m4a",
    ".mkv",
    ".mov",
    ".mp3",
    ".mp4",
    ".ogg",
    ".wav",
    ".webm",
    ".wma",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate local .srt subtitles from audio/video files."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="Audio/video file paths, or directories when --recursive is used.",
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        type=Path,
        help="Output directory. Default: next to each input file.",
    )
    parser.add_argument(
        "--model",
        default="small",
        help=(
            "faster-whisper model size/name. Common values: tiny, base, small, "
            "medium, large-v3. Default: small."
        ),
    )
    parser.add_argument(
        "--language",
        default="zh",
        help="Recognition language code. Use zh for Chinese, en for English, or auto.",
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cpu", "cuda"],
        help="Inference device. Default: auto.",
    )
    parser.add_argument(
        "--compute-type",
        default="auto",
        help=(
            "faster-whisper compute type, for example auto, int8, float16, "
            "int8_float16. Default: auto."
        ),
    )
    parser.add_argument(
        "--beam-size",
        type=int,
        default=5,
        help="Beam size for decoding. Higher may improve accuracy but is slower.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recursively scan directory inputs for common media files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .srt files.",
    )
    parser.add_argument(
        "--no-vad",
        action="store_true",
        help="Disable VAD filtering. VAD usually helps skip long silence.",
    )
    parser.add_argument(
        "--initial-prompt",
        help="Optional prompt for names/terms, for example: 原神，芙宁娜，枫丹，水神。",
    )
    parser.add_argument(
        "--allow-duplicate-openmp",
        action="store_true",
        help=(
            "Work around libiomp5md.dll conflicts in some Anaconda/Windows "
            "environments by setting KMP_DUPLICATE_LIB_OK=TRUE before loading "
            "the speech model."
        ),
    )
    return parser


def require_faster_whisper() -> None:
    if importlib.util.find_spec("faster_whisper") is None:
        print(
            "Missing dependency: faster-whisper\n"
            "Install it with: python -m pip install -U faster-whisper",
            file=sys.stderr,
        )
        raise SystemExit(2)


def iter_media_files(inputs: Iterable[Path], recursive: bool) -> Iterator[Path]:
    for input_path in inputs:
        path = input_path.expanduser()
        if path.is_file():
            if path.suffix.lower() in MEDIA_EXTENSIONS:
                yield path
            else:
                print(f"Skip unsupported file type: {path}", file=sys.stderr)
            continue

        if path.is_dir():
            if not recursive:
                print(f"Skip directory without --recursive: {path}", file=sys.stderr)
                continue

            pattern = "**/*"
            for child in sorted(path.glob(pattern)):
                if child.is_file() and child.suffix.lower() in MEDIA_EXTENSIONS:
                    yield child
            continue

        print(f"Input not found: {path}", file=sys.stderr)


def output_path_for(input_path: Path, out_dir: Path | None) -> Path:
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        return out_dir / f"{input_path.stem}.srt"
    return input_path.with_suffix(".srt")


def format_timestamp(seconds: float) -> str:
    milliseconds_total = max(0, int(round(seconds * 1000)))
    hours, remainder = divmod(milliseconds_total, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def clean_text(text: str) -> str:
    return " ".join(text.strip().split())


def write_srt(segments: Iterable[object], output_path: Path) -> int:
    count = 0
    with output_path.open("w", encoding="utf-8", newline="\n") as file:
        for index, segment in enumerate(segments, start=1):
            text = clean_text(getattr(segment, "text", ""))
            if not text:
                continue

            start = format_timestamp(float(getattr(segment, "start")))
            end = format_timestamp(float(getattr(segment, "end")))
            count += 1
            file.write(f"{index}\n{start} --> {end}\n{text}\n\n")

    return count


def create_model(model_name: str, device: str, compute_type: str):
    from faster_whisper import WhisperModel

    kwargs: dict[str, str] = {}
    if device != "auto":
        kwargs["device"] = device
    if compute_type != "auto":
        kwargs["compute_type"] = compute_type

    return WhisperModel(model_name, **kwargs)


def transcribe_file(model, input_path: Path, args: argparse.Namespace) -> tuple[object, object]:
    language = None if args.language == "auto" else args.language
    return model.transcribe(
        str(input_path),
        language=language,
        beam_size=args.beam_size,
        vad_filter=not args.no_vad,
        initial_prompt=args.initial_prompt,
    )


def main() -> int:
    args = build_parser().parse_args()
    if args.allow_duplicate_openmp:
        os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

    require_faster_whisper()

    media_files = list(iter_media_files(args.inputs, args.recursive))
    if not media_files:
        print("No supported media files found.", file=sys.stderr)
        return 2

    print(f"Loading model: {args.model}")
    model = create_model(args.model, args.device, args.compute_type)

    failed = 0
    for input_path in media_files:
        srt_path = output_path_for(input_path, args.out_dir)
        if srt_path.exists() and not args.overwrite:
            print(f"Skip existing: {srt_path}")
            continue

        print(f"Transcribing: {input_path}")
        try:
            segments, info = transcribe_file(model, input_path, args)
            count = write_srt(segments, srt_path)
        except Exception as exc:  # noqa: BLE001 - CLI should report and continue batch work.
            failed += 1
            print(f"Failed: {input_path}\n  {exc}", file=sys.stderr)
            continue

        detected_language = getattr(info, "language", "unknown")
        duration = getattr(info, "duration", 0)
        print(f"Wrote: {srt_path} ({count} captions, language={detected_language}, duration={duration:.1f}s)")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
