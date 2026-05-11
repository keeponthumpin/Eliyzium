@echo off
echo Current directory: %CD%
cd /d "C:/Users/8DOF/Documents/8DOF_GUI/data/madmom"
echo Changed directory to: %CD%
set "PIP_DISABLE_PIP_VERSION_CHECK=1"
if not exist venv_madmonTD (
    echo Creating Python venv at: C:/Users/8DOF/Documents/8DOF_GUI/data/madmom\venv_madmonTD
    "C:/Users/8DOF/AppData/Local/Programs/Python/Python39/python.exe" -m venv venv_madmonTD
) else (
    echo Virtual environment already exists at: C:/Users/8DOF/Documents/8DOF_GUI/data/madmom\venv_madmonTD
)

echo Attempting to activate virtual environment...
call "venv_madmonTD\\Scripts\\activate.bat"

rem Check if the virtual environment was activated successfully
if "%VIRTUAL_ENV%" == "" (
    echo Failed to activate virtual environment. Please check the path and ensure the venv exists.
    echo Path to venv: "C:/Users/8DOF/Documents/8DOF_GUI/data/madmom\\venv"
    echo VIRTUAL_ENV: "%VIRTUAL_ENV%"
    pause /b 1
) else (
    echo Virtual environment activated.
)
echo Starting DNB BeatDetection
python.exe "C:/Users/8DOF/Desktop/ElysiumV2/Elysium-git/Eliyzium/scripts/DBNBeatTrackerOSC.py" --osc_serverip 127.0.0.1 --osc_serverport 7088 online --device 0
pause