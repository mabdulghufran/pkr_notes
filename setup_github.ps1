# PowerShell script to set up GitHub repository for Pkr_Notes

Write-Host "Setting up GitHub repository for Pkr_Notes..." -ForegroundColor Green
Write-Host ""

# Check if git is available
try {
    $gitVersion = git --version
    Write-Host "Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/downloads" -ForegroundColor Yellow
    Write-Host "After installation, restart your terminal and run this script again" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Initializing repository..." -ForegroundColor Cyan
git init

Write-Host "Adding essential files..." -ForegroundColor Cyan
git add README.md LICENSE requirements.txt setup.py detect_pkr.py test_detection.py .gitignore QUICKSTART.md

Write-Host "Adding documentation and examples..." -ForegroundColor Cyan
git add docs/ examples/ .github/

Write-Host "Adding configuration files..." -ForegroundColor Cyan
git add data.yaml

Write-Host "Adding notebook..." -ForegroundColor Cyan
git add Pkr_notes.ipynb

Write-Host "Creating initial commit..." -ForegroundColor Cyan
git commit -m "Initial commit: Pkr_Notes YOLOv8 banknote detection project"

Write-Host ""
Write-Host "Repository setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a new repository on GitHub" -ForegroundColor White
Write-Host "2. Add the remote origin:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/Pkr_Notes.git" -ForegroundColor Cyan
Write-Host "3. Push to GitHub:" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "Note: Large model files (.pt) are excluded by .gitignore" -ForegroundColor Yellow
Write-Host "You may want to upload them separately or use Git LFS" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to continue"
