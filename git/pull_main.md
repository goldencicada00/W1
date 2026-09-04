# 在 main 這台電腦修改檔案
## flow:
1. 先抓 GitHub 最新內容 
  ```
  git pull
  ```
2. 接著正常修改檔案，例如改：
    ```
    W1/code/tool/audio_filter.py
    ```
    
    修改完先看：
    ```
    git status
    ```
    然後：
    ```
    git add .
    ```
    建立修改標籤：
    ```
    git commit -m "修改 audio filter"
    ```
    最後：
    ```
    git push
    ```

## flow 概述
```
開始工作
   ↓
git pull
   ↓
修改檔案
   ↓
git status
   ↓
git add .
   ↓
git commit -m "這次修改內容"
   ↓
git push
```
