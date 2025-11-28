#!/usr/bin/env python3
import os
import subprocess
import json
from pathlib import Path

# File types to process
VIDEO_EXTENSIONS = {".mkv", ".mp4", ".avi", ".mov", ".m4v"}

# Target formats
TARGET_VIDEO_CODEC = "h264"
TARGET_AUDIO_CODECS = {"aac", "ac3", "mp3"}
TARGET_CONTAINER = ".mp4"
MAX_HEIGHT = 1080

# FFmpeg settings
CRF = 20
PRESET = "veryfast"
AUDIO_BITRATE = "192k"

def run_cmd(cmd):
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return proc.stdout, proc.stderr, proc.returncode


def ffprobe_info(file_path: Path):
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        "-show_format",
        str(file_path)
    ]
    out, err, code = run_cmd(cmd)
    if code != 0:
        print(f"[ERROR] ffprobe failed on {file_path}: {err}")
        return None
    
    return json.loads(out)


def is_plex_friendly(file_path: Path, info: dict) -> bool:
    ext = file_path.suffix.lower()
    container_ok = ext in {".mp4", ".mkv"}

    video_streams = [s for s in info.get("streams", []) if s.get("codec_type") == "video"]
    audio_streams = [s for s in info.get("streams", []) if s.get("codec_type") == "audio"]

    if not video_streams:
        return True

    v = video_streams[0]
    v_codec = v.get("codec_name")
    height = v.get("height") or 0

    video_ok = (v_codec == TARGET_VIDEO_CODEC) and (height <= MAX_HEIGHT)

    audio_ok = True
    for a in audio_streams:
        if a.get("codec_name") not in TARGET_AUDIO_CODECS:
            audio_ok = False
            break

    return container_ok and video_ok and audio_ok


def build_ffmpeg_cmd(in_file: Path, out_file: Path):
    return [
        "ffmpeg",
        "-y",
        "-i", str(in_file),

        # Video
        "-c:v", "libx264",
        "-preset", PRESET,
        "-crf", str(CRF),
        "-vf", f"scale='-2:{MAX_HEIGHT}'",

        # Audio
        "-c:a", "aac",
        "-b:a", AUDIO_BITRATE,

        "-movflags", "+faststart",

        str(out_file)
    ]


def process_file(src: Path, dest: Path):
    print(f"\n[SCAN] {src}")

    info = ffprobe_info(src)
    if info is None:
        return

    if is_plex_friendly(src, info):
        print("  -> Already Plex friendly. Skipping.")
        return

    dest_parent = dest.parent
    dest_parent.mkdir(parents=True, exist_ok=True)

    print(f"  -> Needs optimization")
    print(f"  -> Output file: {dest}")

    cmd = build_ffmpeg_cmd(src, dest)
    print("  -> Running ffmpeg...")
    print("     " + " ".join(cmd))

    _, err, code = run_cmd(cmd)
    if code != 0:
        print(f"[ERROR] ffmpeg failed: {err}")
        if dest.exists():
            dest.unlink()
        return

    print("  -> Done.")


def main():
    print("=== Plex Media Optimizer ===")

    # Prompt for source
    src_input = input("Enter SOURCE directory (e.g. Z:\\Movies): ").strip('"')
    src_root = Path(src_input)
    if not src_root.exists():
        print(f"[FATAL] Source path does not exist: {src_root}")
        return

    # Prompt for destination
    dest_input = input("Enter DESTINATION directory (optimized output): ").strip('"')
    dest_root = Path(dest_input)
    dest_root.mkdir(parents=True, exist_ok=True)

    print(f"\nSource:      {src_root}")
    print(f"Destination: {dest_root}")
    confirm = input("\nProceed? (y/n): ").lower()
    if confirm not in ("y", "yes"):
        print("Cancelled.")
        return

    print("\nStarting optimization...\n")

    for dirpath, _, filenames in os.walk(src_root):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in VIDEO_EXTENSIONS:
                continue

            src_file = Path(dirpath) / filename

            relative_path = src_file.relative_to(src_root)
            dest_file = dest_root / relative_path
            dest_file = dest_file.with_suffix(TARGET_CONTAINER)

            process_file(src_file, dest_file)

    print("\n=== Done! ===")


if __name__ == "__main__":
    main()
