#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Cursor here
# @raycast.mode silent
# @raycast.packageName VS Code
#
# Optional parameters:
# @raycast.icon img/cursor.jpg
#
# Documentation:
# @raycast.description Opens current folder in Cursor
# @raycast.author Kelvin Ng
# @raycast.authorURL https://github.com/hoishing/raycast-scripts


import subprocess, sys
from utils import get_folder


subprocess.run(["/usr/local/bin/cursor", get_folder()])
