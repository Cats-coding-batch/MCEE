@echo off
setlocal enabledelayedexpansion
reg query "HKU\S-1-5-19\Environment" >nul 2>&1
if not %errorlevel% EQU 0 (
    cls
    powershell.exe -windowstyle hidden -noprofile "Start-Process '%~dpnx0' -Verb RunAs"
    exit
)
cd /d "%~dp0"
chcp 1251>NULL
cls
cd..
cd BYPASS
start bpy.exe
cd..
cd MCEE
start Minecraft.Windows.exe
exit