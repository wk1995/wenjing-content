#!/usr/bin/env python3
"""
Generate local SRT subtitle files from audio/video files.

This is a local alternative to editor/VIP subtitle export features:
it does not call Jianying/CapCut, and does not send media to a cloud API.
It uses faster-whisper for speech recognition and writes standard .srt files.

Install dependency:
  python -m pip install -U faster-whisper

Examples:
  python "projects/最后的借口+芙宁娜pv/tools/local_srt_from_media.py" input.mp4
  python "projects/最后的借口+芙宁娜pv/tools/local_srt_from_media.py" input.mp4 -o subtitles --model medium --language zh
  python "projects/最后的借口+芙宁娜pv/tools/local_srt_from_media.py" "D:/videos" --recursive --model large-v3
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
        default="cpu",
        choices=["auto", "cpu", "cuda"],
        help="Inference device. Default: cpu.",
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
        "--condition-on-previous-text",
        action="store_true",
        help=(
            "Let the model use previous decoded text as context. This can help "
            "long speech, but may cause repeated hallucinations in songs/PVs."
        ),
    )
    parser.add_argument(
        "--repetition-penalty",
        type=float,
        default=1.2,
        help="Penalty for repeated text during decoding. Default: 1.2.",
    )
    parser.add_argument(
        "--no-repeat-ngram-size",
        type=int,
        default=3,
        help="Prevent repeated n-grams of this size during decoding. Use 0 to disable.",
    )
    parser.add_argument(
        "--hallucination-silence-threshold",
        type=float,
        default=2.0,
        help="Threshold used by faster-whisper to skip likely hallucinations after silence.",
    )
    parser.add_argument(
        "--max-consecutive-same-text",
        type=int,
        default=2,
        help="Skip identical captions repeated more than this many times in a row. Use 0 to disable.",
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


def normalize_caption_text(text: str) -> str:
    return "".join(text.split()).lower()


def write_srt(segments: Iterable[object], output_path: Path, max_consecutive_same_text: int = 2) -> int:
    tmp_path = output_path.with_name(f".{output_path.name}.tmp")
    count = 0
    previous_normalized_text = ""
    repeated_count = 0

    try:
        with tmp_path.open("w", encoding="utf-8", newline="\n") as file:
            for segment in segments:
                text = clean_text(getattr(segment, "text", ""))
                if not text:
                    continue
                normalized_text = normalize_caption_text(text)
                if normalized_text == previous_normalized_text:
                    repeated_count += 1
                else:
                    previous_normalized_text = normalized_text
                    repeated_count = 1

                if max_consecutive_same_text > 0 and repeated_count > max_consecutive_same_text:
                    continue

                start = format_timestamp(float(getattr(segment, "start")))
                end = format_timestamp(float(getattr(segment, "end")))
                count += 1
                file.write(f"{count}\n{start} --> {end}\n{text}\n\n")

        tmp_path.replace(output_path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise

    return count


def create_model(model_name: str, device: str, compute_type: str):
    from faster_whisper import WhisperModel

    kwargs: dict[str, str] = {}
    if device != "auto":
        kwargs["device"] = device
    if compute_type != "auto":
        kwargs["compute_type"] = compute_type

    return WhisperModel(model_name, **kwargs)


def is_cuda_runtime_error(exc: Exception) -> bool:
    message = str(exc).lower()
    markers = [
        "cublas",
        "cudnn",
        "cuda",
        "could not load library",
        "is not found or cannot be loaded",
    ]
    return any(marker in message for marker in markers)


def create_model_with_auto_fallback(model_name: str, device: str, compute_type: str):
    try:
        return create_model(model_name, device, compute_type)
    except Exception as exc:
        if device != "auto" or not is_cuda_runtime_error(exc):
            raise

        print(
            "CUDA runtime is unavailable, falling back to CPU int8. "
            "To force CPU directly, set --device cpu.",
            file=sys.stderr,
        )
        return create_model(model_name, "cpu", "int8")


def transcribe_file(model, input_path: Path, args: argparse.Namespace) -> tuple[object, object]:
    language = None if args.language == "auto" else args.language
    return model.transcribe(
        str(input_path),
        language=language,
        beam_size=args.beam_size,
        condition_on_previous_text=args.condition_on_previous_text,
        repetition_penalty=args.repetition_penalty,
        no_repeat_ngram_size=args.no_repeat_ngram_size,
        hallucination_silence_threshold=args.hallucination_silence_threshold,
        vad_filter=not args.no_vad,
        initial_prompt=args.initial_prompt,
    )


def transcribe_to_srt(model, input_path: Path, srt_path: Path, args: argparse.Namespace) -> tuple[int, object]:
    segments, info = transcribe_file(model, input_path, args)
    count = write_srt(segments, srt_path, args.max_consecutive_same_text)
    return count, info


def warn_if_few_captions(count: int, duration: float, args: argparse.Namespace) -> None:
    if duration < 60 or count >= 5:
        return

    suggestions = []
    if not args.no_vad:
        suggestions.append("try --no-vad for PV/music videos")
    if args.model in {"tiny", "base", "small"}:
        suggestions.append("try --model medium or --model large-v3")

    suggestions.append("speech ASR may miss sung vocals under loud music")
    print(
        "Warning: only "
        f"{count} captions were generated for a {duration:.1f}s file; "
        + "; ".join(suggestions)
        + ".",
        file=sys.stderr,
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

    print(f"Loading model: {args.model} (device={args.device}, compute_type={args.compute_type})")
    model = create_model_with_auto_fallback(args.model, args.device, args.compute_type)

    failed = 0
    for input_path in media_files:
        srt_path = output_path_for(input_path, args.out_dir)
        if srt_path.exists() and not args.overwrite:
            if srt_path.stat().st_size == 0:
                print(f"Remove empty existing SRT: {srt_path}")
                srt_path.unlink()
            else:
                print(f"Skip existing: {srt_path}")
                continue

        print(f"Transcribing: {input_path}")
        try:
            count, info = transcribe_to_srt(model, input_path, srt_path, args)
        except Exception as exc:  # noqa: BLE001 - CLI should report and continue batch work.
            if args.device == "auto" and is_cuda_runtime_error(exc):
                print(
                    "CUDA runtime failed during transcription, retrying with CPU int8.",
                    file=sys.stderr,
                )
                try:
                    model = create_model(args.model, "cpu", "int8")
                    count, info = transcribe_to_srt(model, input_path, srt_path, args)
                except Exception as retry_exc:  # noqa: BLE001 - CLI should report and continue batch work.
                    failed += 1
                    print(f"Failed: {input_path}\n  {retry_exc}", file=sys.stderr)
                    continue
            else:
                failed += 1
                print(f"Failed: {input_path}\n  {exc}", file=sys.stderr)
                continue

        detected_language = getattr(info, "language", "unknown")
        duration = getattr(info, "duration", 0)
        print(f"Wrote: {srt_path} ({count} captions, language={detected_language}, duration={duration:.1f}s)")
        warn_if_few_captions(count, duration, args)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
