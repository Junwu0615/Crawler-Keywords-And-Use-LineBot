<a href='https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Crawler-Keywords-And-Use-LineBot.svg'> 
<a href='https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/Junwu0615/dc62dfdf2b0e2710dd9a47cebee51ffa/raw/Crawler-Keywords-And-Use-LineBot_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Platform-LineBot-blue.svg?style=plastic)](https://developers.line.biz/zh-hant/) 
[![](https://img.shields.io/badge/Platform-Ngrok-blue.svg?style=plastic)](https://ngrok.com/) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot) 
[![](https://img.shields.io/badge/Language-Python-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-BeautifulSoup-green.svg?style=plastic)](https://pypi.org/project/beautifulsoup4/) 
[![](https://img.shields.io/badge/Package-Requests-green.svg?style=plastic)](https://pypi.org/project/requests/) 
[![](https://img.shields.io/badge/Package-Flask-green.svg?style=plastic)](https://pypi.org/project/Flask/) 
[![](https://img.shields.io/badge/Package-LineBot_SDK-green.svg?style=plastic)](https://pypi.org/project/line-bot-sdk/) 

## A.　研究動機
生活中若有個方便的聊天機器人，那將會樂趣無窮，有句話是這麼說 : 科技始終來自於人性。

## B.　預計功能擴充
- [ ] AI 生成圖片
- [ ] 串接 ChatGPT
- [ ] 104/1111 找工作，關鍵字: 職稱 | 資本額 | 底薪 | 查頁數 | 連結
- [ ] 找房子，關鍵字: 位子 | 房租費
- [ ] 斜槓開發者的專案列表
- [ ] LINE Bot 功能詳列
- [ ] 批踢踢 : 某版有哪些文章，關鍵字: 某版 | 查頁數 | 連結
- [ ] 批踢踢 : 有哪些看板
- [x] 批踢踢 : 關鍵字搜尋文章 > 2023/12/19 已更新功能

## C.　成果展示
### I.　加入 LINE BOT　|　ID : [@002neirm](https://lin.ee/6bkSNWG)
<img width='300' height='400' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/img/line_03.jpg"/>

### II.　批踢踢爬蟲 : 關鍵字搜尋文章
- 情境 : 今天我想在「批踢踢」中的「工作版」找一篇文章，下的關鍵字是「台積電」，並依此搜尋「2」頁內容。
- 在 Line 輸入 `PTT,Tech_Job版,台積電,2`
- ![PTT關鍵字搜尋文章](/img/result_00.gif)

## D.　註冊環境帳號
### I.　申請 [LINE Developer](https://developers.line.biz/zh-hant/) 帳號
1. 註冊或登入帳號。
1. 建立 Provider，接著輸入名稱，並點擊 Create 。
1. 於方才建立好的 Provider 中，建立 Channel，並選擇「Message API」。
1. 路徑 : 進入Channel -> Messaging API 頁籤 -> 頁面最底下取得 `Channel access token` (於流程 F. 使用)。
- <img width='500' height='180' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/img/line_00.jpg"/>

### II.　進入 [LINE 官方帳號](https://tw.linebiz.com/login/)
1. LINE官方帳號管理頁面，點擊「登入管理頁面」。
1. 可看到剛建立的 Channel，自動變成了一個官方帳號。
1. 路徑 : 設定 -> Message API，取得 `Channel secret` (於流程 F. 使用)。
- <img width='500' height='230' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/img/line_01.jpg"/>

### III.　申請 [NGROK](https://ngrok.com/) 帳號
1. 根據個人環境條件，進行下載並解壓縮。
- <img width='500' height='300' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/img/ngrok_00.jpg"/>
2. 取得 AuthToken。
- <img width='500' height='150' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/img/ngrok_01.jpg"/>
3. 打開 ngrok.exe，並將 AuthToken 貼上 `ngrok config add-authtoken <your authtoken>` (於流程 F. 使用)。</br>
#將複製的 AuthToken 取代其內容 `<your authtoken>` 。

## E.　邏輯說明
- 於 LINE Bot 用關鍵字的方式下指令。
- 透過 LINE Bot 的 Webhook URL 方式傳輸至 NGROK。
- NGROK 平台會作為一個接口的橋樑，因為本地開發環境無法直接對外連結。
- 因此 NGROK 收到 Line 訊息後，接著本地程式即可接受 POST 資訊。
- 主程式透過 Switch 方式來判斷關鍵字需要什麼服務，並進行一系列的程式運作。
- 最後將運行結果，以 LINE Bot 的 Reply Token 回傳回去。

## F.　程式運作流程
1. 將主程式打開，將下列參數修改成你複製的內容。具體請參考 `流程 D.`。
    ```ruby
    #LINE超參數
    access_token = 'your channel access token'
    secret = 'your channel secret'
    ```
2. 開啟 Cmd 輸入
    - 安裝套件 : `pip install -r kit_list.txt`
    - 啟動主程式 : `python Crawler_Keywords_And_Use_LineBot.py`
3. 開啟 ngrok.exe 輸入 : `ngrok http 5000`</br>
#Python 套件 Flask 的 port 為 5000。
    - `Forwarding` 後面的網址複製起來，ex: https://xxxx.ngrok-free.app
    - 到 [LINE Developer](https://developers.line.biz/zh-hant/) 中 Channel 的 `Messaging API`，找到標籤 `Webhook URL` 將網址更新上去。
4. 打開 line 聊天機器人輸入對話即可。具體請參考 `流程 C.`。

## G.　參考資源
- [Steam 教育學習網 | LINE BOT 教學](https://steam.oxxostudio.tw/)
- [作者 leVirve | 爬蟲教學 CrawlerTutorial](https://github.com/leVirve/CrawlerTutorial?tab=readme-ov-file#%E6%92%B0%E5%AF%AB%E8%87%AA%E5%B7%B1%E7%9A%84-api---%E6%8A%8A-ptt-%E5%85%A8%E5%8C%85%E4%BA%86)
- [作者 伊果 | 用爬蟲在 PTT 上監聽關鍵字並寄通知信](https://igouist.github.io/post/2019/12/ptt-crawler-and-listener/)
