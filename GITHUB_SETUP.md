# 🚀 GitHub Repository Setup Guide

This guide will help you set up your Pkr_Notes project as a GitHub repository.

## 📋 Prerequisites

- [Git](https://git-scm.com/downloads) installed on your system
- [GitHub](https://github.com) account
- Basic knowledge of Git commands

## 🎯 Step-by-Step Setup

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name**: `Pkr_Notes`
   - **Description**: `YOLOv8-based Pakistani Rupee banknote detection system`
   - **Visibility**: Choose Public or Private
   - **Initialize with**: Leave unchecked (we'll push existing code)
5. Click **"Create repository"**

### 2. Setup Local Repository

#### Option A: Using Setup Scripts (Recommended)

**Windows (Command Prompt):**
```cmd
setup_github.bat
```

**Windows (PowerShell):**
```powershell
.\setup_github.ps1
```

#### Option B: Manual Setup

```bash
# Initialize git repository
git init

# Add essential files
git add README.md LICENSE requirements.txt setup.py detect_pkr.py test_detection.py .gitignore QUICKSTART.md

# Add documentation and examples
git add docs/ examples/ .github/

# Add configuration files
git add data.yaml

# Add notebook
git add Pkr_notes.ipynb

# Create initial commit
git commit -m "Initial commit: Pkr_Notes YOLOv8 banknote detection project"
```

### 3. Connect to GitHub

```bash
# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Pkr_Notes.git

# Verify remote
git remote -v
```

### 4. Push to GitHub

```bash
# Push to main branch
git push -u origin main

# If you get an error about the branch name, try:
git branch -M main
git push -u origin main
```

## 🔧 Repository Structure

After setup, your repository will contain:

```
Pkr_Notes/
├── 📁 .github/              # GitHub Actions workflows
├── 📁 docs/                 # Project documentation
├── 📁 examples/             # Usage examples
├── 📁 test/                 # Test images and labels
├── 📁 train/                # Training images and labels
├── 📁 valid/                # Validation images and labels
├── 📁 runs/                 # Training outputs (excluded by .gitignore)
├── 📄 README.md             # Project overview
├── 📄 QUICKSTART.md         # Quick start guide
├── 📄 LICENSE               # MIT License
├── 📄 requirements.txt      # Python dependencies
├── 📄 setup.py              # Installation script
├── 📄 detect_pkr.py         # Main detection script
├── 📄 test_detection.py     # Unit tests
├── 📄 data.yaml             # Dataset configuration
├── 📄 Pkr_notes.ipynb      # Training notebook
└── 📄 .gitignore            # Git ignore rules
```

## ⚠️ Important Notes

### Excluded Files
The following files are excluded by `.gitignore`:
- **Model files** (`.pt`, `.pth`) - Too large for Git
- **Training outputs** (`runs/` folder) - Generated during training
- **Cache files** (`.cache`, `__pycache__`) - Temporary files
- **Environment files** (`.env`, `venv/`) - Local configurations

### Large Files
If you want to include model files, consider:
1. **Git LFS** (Large File Storage)
2. **Separate releases** on GitHub
3. **External hosting** (Google Drive, AWS S3)

## 🚀 Post-Setup Steps

### 1. Enable GitHub Features

- **Issues**: Enable for bug reports and feature requests
- **Discussions**: Enable for community discussions
- **Wiki**: Enable for detailed documentation
- **Actions**: Enable for CI/CD (already configured)

### 2. Configure Repository Settings

- **Description**: Add detailed project description
- **Topics**: Add relevant tags (yolo, computer-vision, banknote-detection)
- **Social Preview**: Upload a project logo/image
- **Branch Protection**: Protect main branch if working with others

### 3. Create Release

1. Go to **Releases** section
2. Click **"Create a new release"**
3. Tag version: `v1.0.0`
4. Title: `Initial Release`
5. Description: Copy from README.md
6. Upload model files as assets

## 🔄 Ongoing Maintenance

### Daily Workflow

```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

### Branch Management

```bash
# Create feature branch
git checkout -b feature/new-feature

# Work on feature
# ... make changes ...

# Commit and push feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature

# Create Pull Request on GitHub
# Merge to main branch
```

## 🆘 Troubleshooting

### Common Issues

#### 1. Authentication Error
```bash
# Use Personal Access Token or SSH key
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/Pkr_Notes.git
```

#### 2. Large File Error
```bash
# Remove large files from git history
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch large_file.pt' --prune-empty --tag-name-filter cat -- --all
```

#### 3. Branch Name Issues
```bash
# Rename branch to main
git branch -M main
git push -u origin main
```

## 📚 Additional Resources

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Guides](https://guides.github.com/)
- [Git LFS](https://git-lfs.github.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

## 🎉 Congratulations!

Your Pkr_Notes project is now a professional GitHub repository! 

**Next steps:**
1. Share your repository with the community
2. Accept contributions from other developers
3. Build a community around your project
4. Consider publishing to PyPI for easy installation

---

**Need help?** Open an issue on your GitHub repository or check the [GitHub documentation](https://docs.github.com/).
