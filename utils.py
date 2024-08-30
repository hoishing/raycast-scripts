"""
utility functions for raycast script commands
"""

import subprocess
import sys


def exit_if_not_install(converter: str) -> None:
    """exit if ImageMagick or FFMpegis not installed"""
    try:
        subprocess.run([converter, "-version"], capture_output=True, text=True)
    except FileNotFoundError:
        print(f"{converter} is not installed")
        sys.exit(1)


def is_format_supported(path: str) -> bool:
    """check if a file is supported by ImageMagick"""
    process = subprocess.run(
        ["magick", "identify", path], capture_output=True, text=True
    )
    return process.returncode == 0


def get_finder_items() -> list[str]:
    """get selected files in Finder"""
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


def get_image_size(path: str) -> str:
    """get image width and height, in format of WxH"""
    process = subprocess.run(
        ["magick", "identify", "-format", "%wx%h", path],
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        print("An error occurred while getting image size")
        sys.exit(1)
    return process.stdout.strip()


def get_folder() -> str:
    """get current folder in Finder"""
    folder = subprocess.run(
        ["osascript", "get-folder.applescript"],
        capture_output=True,
        text=True,
    ).stdout.strip()

    if not folder:
        print("No folder selected in Finder")
        sys.exit(1)
    return folder
