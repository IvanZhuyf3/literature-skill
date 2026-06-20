#!/bin/bash
# Cron entry point: run track_all.py with correct venv Python
PYTHONIOENCODING=utf-8 exec "C:/Users/Ivanz/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe" \
  "$(dirname "$0")/track_all.py"
