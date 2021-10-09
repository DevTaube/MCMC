@echo off
echo ========================================
echo Press any key to start.
echo ========================================
pause > nul
echo Uninstalling JoyCon-Python...
echo ========================================
python -m pip uninstall joycon-python -y
echo ========================================
echo Uninstalling HidAPI...
echo ========================================
python -m pip uninstall hidapi -y
echo ========================================
echo Uninstalling PYGLM...
echo ========================================
python -m pip uninstall pyglm -y
echo ========================================
echo Uninstalling YAML for Python...
echo ========================================
python -m pip uninstall pyyaml -y
echo ========================================
echo Uninstalling PyAutoGUI...
echo ========================================
python -m pip uninstall pyautogui -y
echo ========================================
echo Uninstall complete.
echo Press any key to exit.
echo ========================================
pause > nul