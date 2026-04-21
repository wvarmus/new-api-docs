@echo off
setlocal

cd /d "%~dp0"

set "NPM_CMD=E:\node\npm.cmd"
if not exist "%NPM_CMD%" set "NPM_CMD=npm"

echo.
echo Starting Mintlify docs...
echo Local:   http://localhost:3000/
echo Network: http://192.168.50.124:3000/
echo Logs:    %~dp0mint-dev.out.log
echo Logs:    %~dp0mint-dev.err.log
echo.

"%NPM_CMD%" run dev -- --no-open 1> mint-dev.out.log 2> mint-dev.err.log

echo.
echo The preview process has stopped.
pause
