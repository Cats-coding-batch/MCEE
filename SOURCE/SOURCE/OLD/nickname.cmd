@echo off
setlocal enabledelayedexpansion
reg query "HKU\S-1-5-19\Environment" >nul 2>&1
if not %errorlevel% EQU 0 (
    cls
    powershell.exe -windowstyle hidden -noprofile "Start-Process '%~dpnx0' -Verb RunAs"
    exit
)

chcp 1251>NULL
cls
@echo off
powershell -Command "(New-Object -ComObject Wscript.Shell).Popup('������� �������� �� Cats Codding Batch',0,'Cats Code [INFO]',0)"
powershell -Command "(New-Object -ComObject Wscript.Shell).Popup('����� �������� ����� ������� ���� ���������� ��������� ���� �� ���� ���.',0,'Cats Code [��������]',48)"

cls
cd /d "%USERPROFILE%"
set "indicator_file=AppData\Roaming\Minecraft Education Edition\games\com.mojang\minecraftpe\options.txt"
set "file_to_modify=AppData\Roaming\Minecraft Education Edition\games\com.mojang\minecraftpe\options.txt"
echo Made in Russian PODVAl
echo ����������� ������ ��������� ���� ��� ��������, � ���� ������ ����� ��������� ����.
echo ������ ��� = ��� ������������ ����������!
echo.
set /p username=������� ��� ��� ��� Minecraft Education Edition: 

if exist "%indicator_file%" (
    (
        echo mp_username:%username%
        more +1 "%file_to_modify%"
    ) > "%file_to_modify%.tmp"
    move /y "%file_to_modify%.tmp" "%file_to_modify%" > nul
	cls
	color 2
	echo.
    echo ��� ��� � Minecraft Education Edition, ������� ��� ������� �� '%username%'
	echo.
) else (
	cls
	color 4
	echo ������:
    echo ����� �������� ����� ������� ���� ���������� ��������� ���� �� ���� ���.
	echo ����������, ��������� ���� � ���������� ��� ���.
	echo.
) 
echo �������� ����� 5 ������!
>nul timeout/nobreak 5

