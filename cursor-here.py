#!/usr/bin/env python3

# @raycast.schemaVersion 1
# @raycast.title Cursor here
# @raycast.mode silent
# @raycast.icon img/cursor.jpg
#
# @raycast.description Opens current folder in Cursor
# @raycast.author Kelvin Ng
# @raycast.authorURL https://github.com/hoishing/raycast-scripts


import subprocess
from utils import get_folder

subprocess.run(["/opt/homebrew/bin/cursor", get_folder()])
