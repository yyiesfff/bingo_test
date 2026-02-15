# 🔥 Firebase 設定指南

## 1. 前往 Firebase 控制台
- 訪問: https://console.firebase.google.com
- 點擊「建立新專案」

## 2. 建立新專案
- **專案名稱**: `bingo-game-sync`
- 選擇或建立 Google Cloud 專案
- 開啟 Google Analytics（可選）

## 3. 建立 Web 應用
- 在專案概覽頁面，點擊「</> 」圖示建立 Web 應用
- **應用暱稱**: `Bingo Game`
- 複製 Firebase 配置（很重要！）

## 4. 設定 Realtime Database
- 左側選單 → **建立資料庫**
- 選擇地區（距離你最近的地區）
- **安全性規則** - 選擇「以測試模式啟動」
- 點擊「啟用」

## 5. 配置 Database 規則
進入「規則」分頁，貼上以下規則（允許多人協作）：

```json
{
  "rules": {
    "games": {
      "$sessionId": {
        ".read": true,
        ".write": true,
        ".indexOn": ["updatedAt"]
      }
    }
  }
}
```

## 6. 將 Firebase 配置貼到 index.html
找到代碼中的 `firebaseConfig` 物件（約第 430 行），替換成你的實際配置：

```javascript
const firebaseConfig = {
    apiKey: "你的_API_KEY",
    authDomain: "你的_PROJECT.firebaseapp.com",
    databaseURL: "https://你的_PROJECT-default-rtdb.firebaseio.com",
    projectId: "你的_PROJECT_ID",
    storageBucket: "你的_PROJECT.appspot.com",
    messagingSenderId: "你的_MESSAGING_SENDER_ID",
    appId: "1:你的_APP_ID:web:你的_WEB_HASH"
};
```

## 7. 測試同步
1. 在瀏覽器開啟遊戲: http://localhost:8000 (或你的伺服器)
2. 輸入玩家 1 名稱，點擊「進入遊戲」
3. **複製遊戲會話 ID**（可在 localStorage 查看 `bingo_session_id`）
4. 在另一個瀏覽器/設備上開啟遊戲
5. 輸入玩家 2 名稱
6. 抽球號 - 所有玩家的棋盤應該會自動同步！ 🎉

## 常見問題

### Q: 如何讓玩家加入現有遊戲？
A: 目前設計是自動加入最新遊戲會話。未來可以加入「輸入會話 ID」的功能。

### Q: Firebase 配額是多少？
A: 免費方案支持 100 個同時連線，對於家庭遊戲足夠。

### Q: 如何保護 Database 不被濫用？
A: 建議使用 Firebase Authentication，或在生產環境加入 IP 白名單。

