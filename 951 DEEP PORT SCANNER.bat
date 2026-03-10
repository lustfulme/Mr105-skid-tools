@echo off
title 951 PORT SCANNER
color 05
chcp 65001 >nul

:: Check if Nmap is installed
where nmap >nul 2>nul
if errorlevel 1 (
    echo Error: Nmap not found. Please install Nmap and try again.
    pause
    exit /b
)

:: Setup Logs Folder
set "outdir=%~dp0logs"
if not exist "%outdir%" mkdir "%outdir%"

:: Main Menu
:menu
cls
echo 🧠 ===================================== 🧠
echo             951 PORT SCANNER
echo 🧠 ===================================== 🧠
echo.
echo [1] 🔍 Full Nmap Deep Scan (All 65535 Ports)
echo [2] 📋 Show Only Open Ports Scan
echo [3] ❌ Exit
echo =========================================
echo.
set /p choice=👉 Select an option (1-3): 

if "%choice%"=="1" goto fullscan
if "%choice%"=="2" goto openscan
if "%choice%"=="3" exit
goto menu

:fullscan
cls
echo 🔥 951 FULL SCANNER 🔥
set /p target=🌐 Enter IP or Domain to scan: 
call :get_timestamp
:: Sanitize the target for filename
set "safe_target=%target:.=_%"
set "safe_target=%safe_target::=_%"
set "logfile=%outdir%\FullScan_%safe_target%_%timestamp%.txt"

echo 🔧 Running deep scan: nmap -p- -sS -sV -O --osscan-guess --traceroute --script vuln,default,discovery,safe,http-enum,ftp-anon,ftp-bounce,dns-brute,telnet-brute,ssh2-enum-algos -T4 --open --reason --max-retries 3 --host-timeout 30m --min-rate 1000 %target%
echo Logging to: %logfile%
echo ------------------------------------- >> "%logfile%"
echo 🔎 Target: %target% >> "%logfile%"
echo 🔧 Command: nmap -p- -sS -sV -O --osscan-guess --traceroute --script vuln,default,discovery,safe,http-enum,ftp-anon,ftp-bounce,dns-brute,telnet-brute,ssh2-enum-algos -T4 --open --reason --max-retries 3 --host-timeout 30m --min-rate 1000 %target% >> "%logfile%"
echo ------------------------------------- >> "%logfile%"

nmap -p- -sS -sV -O --osscan-guess --traceroute --script vuln,default,discovery,safe,http-enum,ftp-anon,ftp-bounce,dns-brute,telnet-brute,ssh2-enum-algos -T4 --open --reason --max-retries 3 --host-timeout 30m --min-rate 1000 %target% >> "%logfile%"

echo.
echo ✅ Full Deep Scan Complete!
echo 📁 Saved log: %logfile%
pause
goto menu

:openscan
cls
echo 🧪 OPEN PORTS ONLY
set /p target=🌐 Enter IP or Domain to scan: 
call :get_timestamp
:: Sanitize the target for filename
set "safe_target=%target:.=_%"
set "safe_target=%safe_target::=_%"
set "logfile=%outdir%\OpenPorts_%safe_target%_%timestamp%.txt"

echo 🔧 Running: nmap --open -p- -T4 %target%
echo Logging to: %logfile%
echo ------------------------------------- >> "%logfile%"
echo 🔎 Target: %target% >> "%logfile%"
echo 🔧 Command: nmap --open -p- -T4 %target% >> "%logfile%"
echo ------------------------------------- >> "%logfile%"

nmap --open -p- -T4 %target% >> "%logfile%"

echo.
echo ✅ Open Port Scan Complete!
echo 📁 Saved log: %logfile%
pause
goto menu

:get_timestamp
:: Makes a safe timestamp string: YYYYMMDD_HHMMSS
for /f "tokens=2 delims==" %%I in ('"wmic os get localdatetime /value"') do set datetime=%%I
set "timestamp=%datetime:~0,4%%datetime:~4,2%%datetime:~6,2%_%datetime:~8,2%%datetime:~10,2%%datetime:~12,2%"
exit /b
