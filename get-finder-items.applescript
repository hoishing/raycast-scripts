#!/usr/bin/osascript

tell application "Finder"
    set selectedItems to selection
    set itemList to ""
    repeat with anItem in selectedItems
        set itemList to itemList & POSIX path of (anItem as alias) & "\n"
    end repeat
    return itemList
end tell