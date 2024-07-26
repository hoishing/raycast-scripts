"""
utility functions for image processing
"""

import subprocess
import sys


# exit if ImageMagick is not installed
def exit_if_not_install(converter: str) -> None:
    """converter: "magick" or "ffmpeg" """
    try:
        subprocess.run([converter, "-version"], capture_output=True, text=True)
    except FileNotFoundError:
        print(f"{converter} is not installed")
        sys.exit(1)


# check if a file is supported by ImageMagick
def is_format_supported(path: str) -> bool:
    process = subprocess.run(
        ["magick", "identify", path], capture_output=True, text=True
    )
    return process.returncode == 0


# exit if no file selected in Finder
def get_finder_items() -> list[str]:
    items = (
        subprocess.run(
            ["osascript", "get-finder-items.applescript"],
            capture_output=True,
            text=True,
        )
        .stdout.strip()
        .split("\n")
    )

    # remove empty items
    items = [item for item in items if item]

    if not items:
        print("No files selected in Finder")
        sys.exit(1)
    return items


# get image width and height, in format of WxH
def get_image_size(path: str) -> str:
    process = subprocess.run(
        ["magick", "identify", "-format", "%wx%h", path],
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        print("An error occurred while getting image size")
        sys.exit(1)
    return process.stdout.strip()
