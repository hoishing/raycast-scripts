#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Favicon Cache Clear
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🧹

# Documentation:
# @raycast.description Remove favicon cache in Safari and return to the previous page
# @raycast.author Kelvin Ng
# @raycast.authorURL https://hoishing.github.io

# Get the current URL from Safari
current_url=$(osascript -e 'tell application "Safari" to get URL of current tab of window 1')

# Quit Safari
osascript -e 'tell application "Safari" to quit'

# Remove the Favicon Cache folder
rm -rf ~/Library/Safari/Favicon\ Cache

# Start Safari and bring it to the front
osascript -e 'tell application "Safari" to activate'

# Wait for Safari to start (adjust the sleep time if needed)
sleep 1

# Go to the recorded URL
osascript -e "tell application \"Safari\" to open location \"$current_url\""

echo "Safari cache cleared and returned to previous page."
