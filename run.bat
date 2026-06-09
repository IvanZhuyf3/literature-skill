@echo off
REM Paper-at-Home: 启动脚本
REM 依赖已 global install，无需 venv

set PYTHONIOENCODING=utf-8
python main.py %*
