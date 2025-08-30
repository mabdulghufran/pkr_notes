@echo off
echo Setting up GitHub repository for Pkr_Notes...
echo.

REM Check if git is available
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/downloads
    echo After installation, restart your terminal and run this script again
    pause
    exit /b 1
)

echo Git found. Initializing repository...
git init

echo Adding essential files...
git add README.md LICENSE requirements.txt setup.py detect_pkr.py test_detection.py .gitignore QUICKSTART.md

echo Adding documentation and examples...
git add docs/ examples/ .github/

echo Adding configuration files...
git add data.yaml

echo Adding notebook...
git add Pkr_notes.ipynb

echo Creating initial commit...
git commit -m "Initial commit: Pkr_Notes YOLOv8 banknote detection project"

echo.
echo Repository setup complete!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo 2. Add the remote origin:
echo    git remote add origin https://github.com/YOUR_USERNAME/Pkr_Notes.git
echo 3. Push to GitHub:
echo    git push -u origin main
echo.
echo Note: Large model files (.pt) are excluded by .gitignore
echo You may want to upload them separately or use Git LFS
echo.
pause
