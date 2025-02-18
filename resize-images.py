#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title resize images
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon img/resize-images.svg
# @raycast.argument1 { "type": "text", "placeholder": "% (default 50)", "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "px (default 1200)", "optional": true }

# Documentation:
# @raycast.description resizes images selected in Finder
# @raycast.author Kelvin Ng
# @raycast.authorURL https://hoishing.github.io

import sys
import subprocess
from utils import (
    exit_if_not_install,
    is_format_supported,
    get_finder_items,
    get_image_size,
)

exit_if_not_install("magick")

# get selected files from Finder
finder_items = get_finder_items()

# image width in percentage
width = f"{sys.argv[1]}%" if sys.argv[1] != "" else "50%"

# image width in pixels, ignore percentage if specified
if sys.argv[2] != "":
    width = f"{sys.argv[2]}x"

# resize images with imagemagick to the specified width in percentage
for item in finder_items:
    # continue if format is not supported by ImageMagick
    if not is_format_supported(item):
        print("⚠️ Unsupported file format: " + item)
        continue

    # size before resizing
    size_before = get_image_size(item)

    cmd = ["magick", "convert", item, "-resize", width, item]
    process = subprocess.run(cmd, capture_output=True, text=True)
    if process.returncode != 0:
        print("⚠️ An error occurred while resizing images")
        sys.exit(1)

    # size after resizing
    size_after = get_image_size(item)

    basename = item.split("/")[-1]
    print(f"✅ Resized '{basename}' from {size_before} to {size_after}")
