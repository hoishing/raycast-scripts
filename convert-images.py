#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Convert / Compress Images
# @raycast.mode silent

# Optional parameters:
# @raycast.icon img/convert-images.svg
# @raycast.argument1 {"type": "text", "placeholder": "type: png", "optional": true}
# @raycast.argument2 {"type": "text", "placeholder": "quality/compression: 70", "optional": true}

# Documentation:
# @raycast.description Convert selected images in Finder to specific format and quality with ImageMagick
# png compression: higher compression takes longer, smaller file size
# other image quality: 0-100, higher quality takes longer, larger file size
# @raycast.author Kelvin Ng
# @raycast.authorURL https://hoishing.github.io


from utils import (
    exit_if_not_install,
    is_format_supported,
    get_finder_items,
)

import sys, subprocess

# check if imagemagick is installed
exit_if_not_install("magick")

# get selected files from Finder
finder_items = get_finder_items()

# type of the output image
img_type = sys.argv[1] if sys.argv[1] != "" else "png"

# quality of the output image
quality = sys.argv[2] if sys.argv[2] != "" else "75"

# convert images to specific format and quality with imagemagick
for item in finder_items:
    # continue if format is not supported by ImageMagick
    if not is_format_supported(item):
        print("⚠️ Unsupported file format: " + item)
        continue

    # change extension to img_type
    converted_img = item.rsplit(".", 1)[0] + "." + img_type

    cmd = ["magick", item, "-quality", quality, converted_img]
    process = subprocess.run(cmd, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"⚠️ error converting {item}")
        sys.exit(1)

    org_basename = item.split("/")[-1]
    converted_basename = converted_img.split("/")[-1]
    print(f"✅ '{org_basename}' -> '{converted_basename}', quality: {quality}")
