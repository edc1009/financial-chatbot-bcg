@echo off
echo ========================================
echo Financial Chatbot - GitHub Deployment
echo ========================================
echo.

echo Step 1: Initializing Git repository...
git init

echo Step 2: Adding all files...
git add .

echo Step 3: Creating initial commit...
git commit -m "Initial commit: Financial Chatbot BCG Program - Complete implementation with CLI, Web, and Standalone interfaces"

echo.
echo ========================================
echo IMPORTANT: Manual Steps Required
echo ========================================
echo.
echo 1. Create a new repository on GitHub:
echo    - Go to https://github.com/new
echo    - Repository name: financial-chatbot-bcg
echo    - Description: A Python-based financial chatbot that answers predefined queries about Tesla, Apple, and Microsoft financial data
echo    - Make it Public (for GitHub Pages)
echo    - Do NOT initialize with README
echo.
echo 2. After creating the repository, run these commands:
echo    git remote add origin https://github.com/YOUR_USERNAME/financial-chatbot-bcg.git
echo    git push -u origin main
echo.
echo 3. Enable GitHub Pages:
echo    - Go to repository Settings ^> Pages
echo    - Source: Deploy from a branch
echo    - Branch: main, folder: / (root)
echo.
echo 4. Your live links will be:
echo    - Repository: https://github.com/YOUR_USERNAME/financial-chatbot-bcg
echo    - Live Demo: https://YOUR_USERNAME.github.io/financial-chatbot-bcg/chatbot_standalone.html
echo.
echo Replace YOUR_USERNAME with your actual GitHub username
echo.
echo ========================================
echo Deployment preparation complete!
echo ========================================
pause