#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title yazi
# @raycast.mode silent

# Optional parameters:
# @raycast.icon img/yazi.png

# Documentation:
# @raycast.description Open Yazi

-- Check if yazi is already running (using pgrep for more accurate process checking)
set isYaziRunning to do shell script "pgrep -x yazi || echo 0"

if isYaziRunning is "0" then
    tell application "Ghostty"
        activate
        delay 0.3
        
        -- Send the command
        tell application "System Events"
            keystroke "y"
            keystroke return
        end tell
    end tell
else
    tell application "Ghostty"
        activate
    end tell
end if    
