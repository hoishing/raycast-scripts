#!/usr/bin/env python3

# @raycast.schemaVersion 1
# @raycast.title vscode here
# @raycast.mode silent
# @raycast.icon img/vscode.svg
#
# Documentation:
# @raycast.description Opens current topmost directory in VSCode
# @raycast.author Kelvin Ng
# @raycast.authorURL https://github.com/hoishing/raycast-scripts

import subprocess
from utils import get_folder


subprocess.run(["/opt/homebrew/bin/code", get_folder()])
