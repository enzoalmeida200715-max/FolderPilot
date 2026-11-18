@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 -m folderpilot gui
) else (
    python -m folderpilot gui
)
if errorlevel 1 (
    echo.
    echo Nao foi possivel abrir o FolderPilot.
    echo Instala Python 3.11 ou superior de https://www.python.org/downloads/
    echo Consulta COMECA_AQUI.md para mais ajuda.
    pause
)
