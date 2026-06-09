@echo off
REM 启动浏览器并开启调试端口（保留已有 Profile 和登录状态）
REM 端口和路径从 config.yaml 读取，需要 Python + PyYAML
REM 使用前确保已关闭所有浏览器窗口

set PYTHONIOENCODING=utf-8
set SCRIPT_DIR=%~dp0

python -c "import yaml, os; c=yaml.safe_load(open('%SCRIPT_DIR%config.yaml',encoding='utf-8')); ch=c.get('chrome',{}); port=ch.get('cdp_url','http://localhost:9222').split(':')[-1].rstrip('/'); exe=ch.get('chrome_path',''); udd=os.path.expandvars(ch.get('user_data_dir','')); print(f'{exe}|{port}|{udd}')" > "%TEMP%\pah_browser.cfg"

set /p CONFIG=<"%TEMP%\pah_browser.cfg"
del "%TEMP%\pah_browser.cfg"

for /f "tokens=1,2,3 delims=|" %%a in ("%CONFIG%") do (
    set BROWSER=%%a
    set PORT=%%b
    set USER_DATA=%%c
)

if not exist "%BROWSER%" (
    echo [ERROR] Browser not found at "%BROWSER%"
    echo Please update chrome_path in config.yaml
    pause
    exit /b 1
)

echo Starting browser with remote debugging on port %PORT% ...
echo Please log in to your institution portal if needed.
echo.
start "" "%BROWSER%" --remote-debugging-port=%PORT% --user-data-dir="%USER_DATA%"
