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
powershell -Command "(New-Object -ComObject Wscript.Shell).Popup('Сделано котиками из Cats Codding Batch',0,'Cats Code [INFO]',0)"
powershell -Command "(New-Object -ComObject Wscript.Shell).Popup('Перед запуском этого скрипта игру необходимо запустить хотя бы один раз.',0,'Cats Code [Внимание]',48)"

cls
cd /d "%USERPROFILE%"
set "indicator_file=AppData\Roaming\Minecraft Education Edition\games\com.mojang\minecraftpe\options.txt"
set "file_to_modify=AppData\Roaming\Minecraft Education Edition\games\com.mojang\minecraftpe\options.txt"
echo Made in Russian PODVAl
echo Используйте только Англискии ники без пробелов, в ином случае может пройзойти сбои.
echo Пустой ник = имя пользователя компьютера!
echo.
set /p username=Введите ваш ник для Minecraft Education Edition: 

if exist "%indicator_file%" (
    (
        echo mp_username:%username%
        more +1 "%file_to_modify%"
    ) > "%file_to_modify%.tmp"
    move /y "%file_to_modify%.tmp" "%file_to_modify%" > nul
	cls
	color 2
	echo.
    echo Ваш ник в Minecraft Education Edition, Успешно был изменен на '%username%'
	echo.
) else (
	cls
	color 4
	echo Ошибка:
    echo Перед запуском этого скрипта игру необходимо запустить хотя бы один раз.
	echo Пожалуйста, запустите игру и попробуйте еще раз.
	echo.
) 
echo Закрытие через 5 секунд!
>nul timeout/nobreak 5

