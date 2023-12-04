#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Rename Files
# @raycast.mode silent

# Optional parameters:
# @raycast.icon img/rename-files.svg
# @raycast.argument1 {"type": "text", "placeholder": "prefix"}


# Documentation:
# @raycast.description Rename selected images in Finder with specific prefix and 2 digits suffix.
# @raycast.author Kelvin Ng
# @raycast.authorURL https://hoishing.github.io

import sys
from image_utils import get_finder_items
from pathlib import Path

prefix = sys.argv[1]

# get selected files from Finder
selected_files = get_finder_items()

# rename files
for index, file in enumerate(selected_files):
    org_file = Path(file)
    stem = f"{prefix}-{index+1:02}"
    new_file = org_file.with_stem(stem)
    org_file.rename(new_file)

    print(f"✅ Renamed {org_file.name} to {new_file.name}")
