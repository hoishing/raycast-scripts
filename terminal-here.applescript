#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Terminal Here
# @raycast.mode silent
#
# Optional parameters:
# @raycast.icon img/terminal.svg
#
# Documentation:
# @raycast.description Open current directory of Finder in Terminal
# @raycast.author Kelvin Ng
# @raycast.authorURL https://github.com/hoishing

tell application "Finder"
	# Check if there's a selection; works if there's a window open or not.
	if selection is not {} then
		set i to item 1 of (get selection)
		
		# If it's an alias, set the item to the original item.
		if class of i is alias file then
			set i to original item of i
		end if
		
		# If it's a folder, use its path.
		if class of i is folder then
			set p to i
		else
			# If it's an item, use its container's path.
			set p to container of i
		end if
	else if exists window 1 then
		# If a window exist, use its folder property as the path.
		set p to folder of window 1
	else
		# Fallback to the Desktop, as nothing is open or selected.
		set p to path to desktop folder
	end if
end tell

# do shell script "open -a Terminal " & quoted form of POSIX path of (p as alias)
do shell script "open -a warp " & quoted form of POSIX path of (p as alias)
