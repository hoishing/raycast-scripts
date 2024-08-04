#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title gif → mov
# @raycast.mode silent

# Optional parameters:
# @raycast.icon img/convert-images.svg

# Documentation:
# @raycast.description Convert gif to Quicktime mov using ffmpeg
# @raycast.author Kelvin Ng
# @raycast.authorURL https://hoishing.github.io


import pathlib
import subprocess
import sys
from image_utils import exit_if_not_install, get_finder_items

# check if ffmpeg is installed
exit_if_not_install("ffmpeg")

# get the selected files from Finder
items = get_finder_items()

# convert each gif to mov using ffmpeg
for item in items:
    item_path = pathlib.Path(item)  # Ensure item is a Path object

    if item_path.suffix.lower() != ".gif":
        print(f"⚠️ skipping non-gif file: {item_path.name}")
        continue

    # change the extension to .mov using pathlib
    output_file = item_path.with_suffix(".mov")

    # ffmpeg command
    cmd = [
        "ffmpeg",
        "-i",
        item,
        "-vf",
        "pad=width=iw:height=ceil(ih/2)*2",  # ensure height is divisible by 2
        "-c:v",
        "libx264",
        "-pix_fmt",  # for quicktime compatibility
        "yuv420p",
        "-y",
        str(output_file),
    ]

    # execute conversion
    process = subprocess.run(cmd, capture_output=True, text=True)

    if process.returncode != 0:
        print(f"error converting {item}")
        sys.exit(1)

    print(f"✅ converted '{item_path.name}' to mov")
