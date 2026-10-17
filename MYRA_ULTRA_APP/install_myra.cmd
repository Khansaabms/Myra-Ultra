@echo off
rem ============================================================
rem  MYRA — one-click install
rem  1) pip se MYRA install/upgrade
rem  2) Windows startup ON  (PC start/restart par MYRA orb ke saath khud chalu)
rem  3) MYRA abhi background mein chalu (screen par mini orb)
rem ============================================================
title MYRA install
echo.
echo  [1/2] MYRA install ho rahi hai...
python -m pip install --upgrade myra-ai-assistant
if errorlevel 1 (
    echo.
    echo  [X] pip install fail hua. Internet / Python (3.10+) check karo.
    pause
    exit /b 1
)
echo.
echo  [2/2] Startup set ho raha hai aur MYRA chalu ho rahi hai...
python -m myra install
echo.
echo  Done! MYRA ka orb screen par aa jayega. Orb par click karke controls dekho,
echo  double-click karke MYRA kholo. Band karna ho to:  python -m myra uninstall
echo.
pause
