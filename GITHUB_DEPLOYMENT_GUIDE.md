# GitHub 部署指南 / GitHub Deployment Guide

## 手動創建 GitHub 倉庫 / Manual GitHub Repository Creation

由於 API 權限限制，請按照以下步驟手動創建 GitHub 倉庫：

### 步驟 1: 創建 GitHub 倉庫
1. 登入您的 GitHub 帳戶
2. 點擊右上角的 "+" 按鈕，選擇 "New repository"
3. 填寫倉庫資訊：
   - **Repository name**: `financial-chatbot-bcg`
   - **Description**: `A Python-based financial chatbot that answers predefined queries about Tesla, Apple, and Microsoft financial data. Features command-line, web, and standalone HTML interfaces.`
   - **Visibility**: Public (推薦，這樣可以使用 GitHub Pages)
   - **Initialize**: 不要勾選 "Add a README file"（我們已經有了）

### 步驟 2: 上傳專案檔案
在您的專案目錄中執行以下命令：

```bash
# 初始化 Git 倉庫
git init

# 添加所有檔案
git add .

# 創建初始提交
git commit -m "Initial commit: Financial Chatbot BCG Program"

# 添加遠端倉庫（替換 YOUR_USERNAME 為您的 GitHub 用戶名）
git remote add origin https://github.com/YOUR_USERNAME/financial-chatbot-bcg.git

# 推送到 GitHub
git push -u origin main
```

### 步驟 3: 啟用 GitHub Pages
1. 在您的 GitHub 倉庫頁面，點擊 "Settings" 標籤
2. 在左側選單中找到 "Pages"
3. 在 "Source" 部分選擇 "Deploy from a branch"
4. 選擇 "main" 分支和 "/ (root)" 資料夾
5. 點擊 "Save"

### 步驟 4: 獲取可訪問連結
啟用 GitHub Pages 後，您將獲得以下連結：

1. **主要倉庫連結**: `https://github.com/YOUR_USERNAME/financial-chatbot-bcg`
2. **獨立 HTML 版本**: `https://YOUR_USERNAME.github.io/financial-chatbot-bcg/chatbot_standalone.html`
3. **專案首頁**: `https://YOUR_USERNAME.github.io/financial-chatbot-bcg/`

## 檔案檢查清單 / File Checklist

確保以下檔案都已準備好且為英文版本：

- ✅ `README.md` - 主要專案說明（英文）
- ✅ `CHATBOT_DOCUMENTATION.md` - 詳細技術文檔（英文）
- ✅ `PROJECT_SUMMARY.md` - 專案摘要（英文）
- ✅ `chatbot_standalone.html` - 獨立 HTML 版本（英文介面）
- ✅ `financial_data_processor.py` - 核心數據處理模組
- ✅ `chatbot_cli.py` - 命令列介面
- ✅ `chatbot_web.py` - Flask 網頁應用
- ✅ `test_chatbot.py` - 自動化測試
- ✅ `requirements.txt` - Python 依賴套件
- ✅ `financial_data.csv` - 財務數據
- ✅ `Financial_Analysis.ipynb` - Jupyter 分析筆記本
- ✅ `templates/index.html` - 網頁模板

## 推薦的 Git 命令 / Recommended Git Commands

```bash
# 檢查狀態
git status

# 查看提交歷史
git log --oneline

# 創建新分支（如果需要）
git checkout -b feature/new-feature

# 推送新分支
git push origin feature/new-feature
```

## 故障排除 / Troubleshooting

### 常見問題：

1. **Git 未安裝**
   - 下載並安裝 Git: https://git-scm.com/downloads

2. **權限被拒絕**
   - 確保您有倉庫的寫入權限
   - 檢查 SSH 金鑰或使用 HTTPS 認證

3. **GitHub Pages 未啟用**
   - 確保倉庫是 Public
   - 檢查 Settings > Pages 設定

4. **檔案未顯示**
   - 等待 GitHub Pages 部署完成（可能需要幾分鐘）
   - 檢查檔案路徑是否正確

## 部署後測試 / Post-Deployment Testing

部署完成後，請測試以下功能：

1. **獨立 HTML 版本**：
   - 訪問 `https://YOUR_USERNAME.github.io/financial-chatbot-bcg/chatbot_standalone.html`
   - 測試所有查詢功能
   - 確認介面為英文

2. **專案文檔**：
   - 檢查 README.md 在 GitHub 上的顯示
   - 確認所有連結正常工作
   - 驗證文檔內容為英文

3. **下載測試**：
   - 下載專案 ZIP 檔案
   - 在本地環境測試 Python 版本

## 成功指標 / Success Indicators

✅ GitHub 倉庫成功創建  
✅ 所有檔案成功上傳  
✅ GitHub Pages 成功啟用  
✅ 獨立 HTML 版本可正常訪問  
✅ 所有文檔均為英文  
✅ 專案功能正常運作  

---

**注意**: 請將 `YOUR_USERNAME` 替換為您實際的 GitHub 用戶名。