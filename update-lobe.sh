#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title update lobehub
# @raycast.mode silent
# @raycast.packageName finder

# Optional parameters:
# @raycast.icon img/lobe-128.webp

# Documentation:
# @raycast.description Update Lobehub through SSH

#!/bin/bash

# Define the remote server and the command to execute
REMOTE_HOST="oracle" # Replace with your actual hostname or IP
REMOTE_DIR="lobehub"
SCRIPT_NAME="update.sh"

# Construct the SSH command
SSH_COMMAND="cd $REMOTE_DIR && ./$SCRIPT_NAME"

# Execute the SSH command
ssh ${REMOTE_HOST} "${SSH_COMMAND}"

# Check if the SSH command was successful
if [ $? -eq 0 ]; then
  echo "Script executed successfully on the remote server."
else
  echo "Failed to execute the script on the remote server."
fi
