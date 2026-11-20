"""Inspect local Telegram Bot API story assets."""
import json
import shutil
import subprocess


def inspect(path):
    if not shutil.which("ffprobe"):
        raise ValueError("install FFmpeg for ffprobe")
    if not path.exists():
        raise ValueError("asset path does not exist")
    files = sorted(p for p in path.iterdir() if p.is_file()) if path.is_dir() else [path]
    if not files:
        raise ValueError("no assets found")
    findings = []
    for file in files:
        probe = subprocess.run(["ffprobe", "-v", "error", "-protocol_whitelist", "file", "-show_streams", "-show_format", "-of", "json", str(file.resolve())], capture_output=True, timeout=30)
        data = json.loads(probe.stdout or b"{}")
        video = next((s for s in data.get("streams", []) if s["codec_type"] == "video"), {})
        fmt = data.get("format", {})
        kind = fmt.get("format_name", "").split(",")
        photo = any(name in ("jpeg_pipe", "png_pipe", "image2") for name in kind)
        size = (1080, 1920) if photo else (720, 1280)
        errors = []
        if probe.returncode or not video:
            errors.append("unreadable or missing visual stream")
        else:
            if (video.get("width"), video.get("height")) != size:
                errors.append(f"resize to {size[0]}x{size[1]}")
            if file.stat().st_size > (10 if photo else 30) * 1000000:
                errors.append("reduce file size")
            if not photo and ("mp4" not in kind or video.get("codec_name") != "hevc"):
                errors.append("export H.265 in an MP4 container")
            if not photo and float(fmt.get("duration", 0)) > 60:
                errors.append("trim to 60 seconds")
        findings.extend(f"{file.name}: {e}" for e in errors)
    return findings

if __name__ == "__main__":
    import argparse
    import json
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        findings = inspect(args.path)
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        parser.exit(2, f"{error}\n")
    result = {"findings": findings}
    print(json.dumps(result, ensure_ascii=False) if args.json else "\n".join(findings) or "OK: checked rules passed")
    sys.exit(bool(findings))
