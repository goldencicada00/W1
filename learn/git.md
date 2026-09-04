# 
Git = 管理你電腦資料夾的「版本紀錄」
GitHub = 把這個 Git 資料夾放到雲端，讓其他電腦也能存取

# 希望 Git 開始管理 資料夾
先在 Terminal / PowerShell / VS Code Terminal 進入該資料夾
1. windows
   `cd "C:\Users\你的名字\Desktop\資料夾"`
1. mac
   `cd ~/Desktop/資料夾`
2. `git --version`  # 版本
3. `git init`  # Initialized empty Git repository
4. 建立 .gitignore
   因為資料夾裡有 Python 程式，建議先避免把 Python 暫存檔、虛擬環境、密碼設定上傳
   在 VS Code 左邊的 W1-W4 上按右鍵 → New File，檔名輸入：
   ```
   .gitignore
   ```
   內容貼上：
   ```
   # Python 暫存檔
   __pycache__/
   *.pyc
   *.pyo
   
   # Python 虛擬環境
   .venv/
   venv/
   
   # Mac 系統檔
   .DS_Store
   
   # Windows 系統檔
   Thumbs.db
   
   # 不要上傳環境變數、密碼
   .env
   ```
   你的 .wav、.py、.txt 不會被這些規則排除，所以仍然可以放 Git
5. 把目前 W1-W4 的資料加入 Git
   回到 Terminal，現在還是在：
   ```
   PS C:\Users\Amy.Cheng\Desktop\W1-W4>
   ```
   輸入：
   ```
   git add .
   ```
   注意最後有一個：
   ```
   .
   ```
   它的意思是：
   ```
   把目前 W1-W4 底下所有「沒有被 .gitignore 排除」的檔案加入 Git。
   ```
   執行完通常不會出現任何訊息，這是正常的
6. 確認:檔案已經進入「準備 commit」的狀態
   輸入：
   ```
   git status
   ```
   這次應該會看到類似：
   ```
   Changes to be committed:
       new file:   W1/code/tool/audio_filter.py
       new file:   W1/code/tool/verify_audio.py
       ...
   ```
   而且通常會顯示成綠色，代表檔案已經進入「準備 commit」的狀態
7. 輸入:`git commit -m "Initial commit"`
8. 若跳出:
   ```
   Author identity unknown
   
   *** Please tell me who you are.
   ```
   則:
   ```
   git config --global user.name "Amy Cheng"
   git config --global user.email "daidaigongzhu080611@gmail.com"
   ```
   再執行上一步
9. 輸入：
   ```
   git branch -M main
   ```
10. 上傳到 GitHub
    1. 到 GitHub 建立一個新的 Repository
      
      登入 GitHub → 右上角 + → New repository。
      
      建議設定：
      
      Repository name: W1-W4
      
      Description: 可以不填
      
      Private: ✅ 建議選 Private
      
      下面這三個先全部不要勾：
      
      ☐ Add a README file
      ☐ Add .gitignore
      ☐ Choose a license
      
      因為你本機已經有 Git repository 和 commit 了。
      
      然後按：
      
      Create repository
12. 
