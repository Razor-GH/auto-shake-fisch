@echo off

REM Check Python installation
python --version
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH.
    pause
    exit /B 1
)

REM Update pip
echo Updating pip...
python -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 (
    echo Failed to update pip.
    pause
    exit /B 1
)

REM Install pyautogui
echo Installing pyautogui...
python -m pip install pyautogui
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install pyautogui.
    pause
    exit /B 1
)

REM Install pyautoit
echo Installing pyautoit...
python -m pip install pyautoit
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install pyautoit.
    pause
    exit /B 1
)

REM Install keyboard
echo Installing keyboard...
python -m pip install keyboard
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install keyboard.
    pause
    exit /B 1
)

echo All packages installed successfully.
pause
