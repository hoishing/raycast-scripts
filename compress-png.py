#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Compress PNG
# @raycast.mode silent

# Optional parameters:
# @raycast.icon img/compress.svg

# Documentation:
# @raycast.description Compress selected PNG images in Finder with optipng
# @raycast.author Kelvin Ng
# @raycast.authorURL https://hoishing.github.io


from utils import (
    exit_if_not_install,
    get_finder_items,
)

import sys, subprocess

# check if optipng is installed
exit_if_not_install("optipng")

# get selected files from Finder
finder_items = get_finder_items()

# compress each selected PNG image
for item in finder_items:

    cmd = ["optipng", item]
    process = subprocess.run(cmd, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"⚠️ error compressing {item}")
        sys.exit(1)

    org_basename = item.split("/")[-1]
    print(f"✅ {org_basename}")
