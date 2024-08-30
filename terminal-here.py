#!/usr/bin/env python3

# @raycast.schemaVersion 1
# @raycast.title Terminal Here
# @raycast.mode silent
# @raycast.icon img/terminal.svg
#
# @raycast.description Open current directory of Finder in Terminal
# @raycast.author Kelvin Ng
# @raycast.authorURL https://github.com/hoishing/raycast-scripts

import subprocess
from utils import get_folder


subprocess.run(["open", "-a", "warp", get_folder()])
