@echo off
echo Installing requirements
pip install -r requirements\ismayeel-requirements.txt > nul
echo Launching
python Red_and_white.py > nul
