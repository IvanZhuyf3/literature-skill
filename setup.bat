@echo off
REM Paper-at-Home: 首次安装依赖
REM 全部 global install，无需 venv

set PYTHONIOENCODING=utf-8

echo Installing dependencies (global)...
pip install requests pyyaml rich playwright pyautogui
playwright install chromium

echo.
echo Setup complete! Use run.bat to start.
pause
