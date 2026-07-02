@echo off
chcp 65001 > nul
python -m pip install pyinstaller
pyinstaller --onefile --windowed --name ROADM_Report_Auto auto_report.py
echo.
echo EXE 파일 위치: dist\ROADM_Report_Auto.exe
pause
