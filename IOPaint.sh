#!/bin/bash

# @raycast.schemaVersion 1
# @raycast.title IOPaint
# @raycast.mode compact
# @raycast.icon img/iopaint.svg
# @raycast.description Opens the IOPaint app.

cd ~/proj/io-paint
.venv/bin/iopaint start --config iopaint-config.json
