@echo off
chcp 65001 > nul
echo [1/2] Python 패키지를 설치합니다...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo [2/2] 완료되었습니다.
echo.
echo 주의: OCR을 사용하려면 Tesseract OCR도 별도 설치해야 합니다.
echo README_처음_사용법.md 파일을 확인하세요.
pause
