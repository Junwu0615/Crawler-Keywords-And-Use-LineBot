<a href='https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Crawler-Keywords-And-Use-LineBot.svg'> 
<a href='https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/dc62dfdf2b0e2710dd9a47cebee51ffa/raw/Crawler-Keywords-And-Use-LineBot_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Platform-Line_Bot-blue.svg?style=plastic)](https://developers.line.biz/zh-hant/) 
[![](https://img.shields.io/badge/Platform-Ngrok-blue.svg?style=plastic)](https://ngrok.com/) 
[![](https://img.shields.io/badge/Project-Web_Crawler-blue.svg?style=plastic)](https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-BeautifulSoup_4.12.2-green.svg?style=plastic)](https://pypi.org/project/beautifulsoup4/) 
[![](https://img.shields.io/badge/Package-Requests_2.31.0-green.svg?style=plastic)](https://pypi.org/project/requests/) 
[![](https://img.shields.io/badge/Package-Flask_3.0.0-green.svg?style=plastic)](https://pypi.org/project/Flask/) 
[![](https://img.shields.io/badge/Package-LineBot_SDK_3.5.1-green.svg?style=plastic)](https://pypi.org/project/line-bot-sdk/) 

<br>

## A.　研究動機
生活中若有個自定義的聊天機器人，將會便利無窮，有句話是這麼說 : 科技始終來自於人性。

<br>

## B.　未來更新
| 事件 | 敘述 | 更新時間 |
| :--: | :-- | :--: |
| 專案上架 | Crawler-Keywords-And-Use-LineBot | 2023/12/19 |
| 批踢踢 : 有哪些看板 | 關鍵字: 看板 \| 回饋: 文字 | - |
| 批踢踢 : 某版有哪些文章 | 關鍵字: 看版 / 頁數 \| 回饋: 連結 | - |
| LINE Bot 功能詳列 | 關鍵字: 功能 \| 回饋: 文字 | - |
| 斜槓開發者的專案列表 | 關鍵字: 開發者專案 \| 回饋: 文字 | - |
| 找房子 | 關鍵字: 位置 / 月租 \| 回饋: 連結 | - |
| 104/1111 找工作 | 關鍵字: 職稱 / 資本額 / 底薪 / 頁數 \| 回饋: 連結 | - |
| 串接 ChatGPT | 關鍵字:  ChatGPT \| 回饋: 文字 | - |
| AI 生成圖片 | 關鍵字: 圖片特徵 \| 回饋: 圖片 | - |

<br>

## C.　成果展示
### I.　加入 LINE BOT
<img width='300' height='400' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/sample/line_03.jpg"/>

### II.　批踢踢爬蟲 : 關鍵字搜尋文章
- 情境 : 今天我想在「批踢踢」中的「工作版」找一篇文章，下的關鍵字是「台積電」，並依此搜尋「10」頁內容。
- 在 Line 輸入 `PTT,Tech_Job版,台積電,10`
- ![PTT關鍵字搜尋文章](/sample/result_00.gif)

<br>

## D.　註冊環境帳號
### I.　申請 [LINE Developer](https://developers.line.biz/zh-hant/) 帳號
1. 註冊或登入帳號。
1. 建立 Provider，接著輸入名稱，並點擊 Create 。
1. 於方才建立好的 Provider 中，建立 Channel，並選擇「Message API」。
1. 路徑 : 進入Channel > Messaging API 頁籤 > 頁面最底下取得 `Channel access token` (於流程 F. 使用)。
- <img width='500' height='180' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/sample/line_00.jpg"/>

### II.　進入 [LINE 官方帳號](https://tw.linebiz.com/login/)
1. LINE官方帳號管理頁面，點擊「登入管理頁面」。
1. 可看到剛建立的 Channel，自動變成了一個官方帳號。
1. 路徑 : 設定 > Message API，取得 `Channel secret` (於流程 F. 使用)。
- <img width='500' height='230' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/sample/line_01.jpg"/>

### III.　申請 [NGROK](https://ngrok.com/) 帳號
1. 根據個人環境條件，進行下載並解壓縮。
- <img width='500' height='300' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/sample/ngrok_00.jpg"/>
2. 取得 AuthToken。
- <img width='500' height='150' src="https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot/blob/main/sample/ngrok_01.jpg"/>
3. 打開 ngrok.exe，並將 AuthToken 貼上 `ngrok config add-authtoken <your authtoken>` (於流程 F. 使用)。</br>
#將複製的 AuthToken 取代其內容 `<your authtoken>` 。

<br>

## E.　邏輯說明
1. 於 LINE Bot 用關鍵字的方式下指令。
1. 透過 LINE Bot 的 Webhook URL 方式傳輸至 NGROK。
1. NGROK 平台會作為一個接口的橋樑，因為本地開發環境無法直接對外連結。
1. 因此 NGROK 收到 Line 訊息後，接著本地程式即可接受 POST 資訊。
1. 主程式透過 Switch 方式來判斷關鍵字需要什麼服務，並進行一系列的程式運作。
1. 最後將運行結果，以 LINE Bot 的 Reply Token 回傳回去。

<br>

## F.　如何使用
### STEP.1　CLONE
```python
git clone https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot.git
```
### STEP.2　變更檔名並修改內容
#### 將 package `token_.txt` -> `token.txt` 修改內容。具體請參考 `流程 D.`。
```python
access_token,[Fill In Your Access Token]
secret,[Fill In Your Secret]
```
### STEP.3　開啟 cmd 輸入
```python
pip install -r requirements.txt
```
```python
python Entry.py
```
### STEP.4　開啟 ngrok.exe 輸入
```python
# Python 套件 Flask 的 port 為 5000
ngrok http 5000
```
- `Forwarding` 後面的網址複製起來，ex: https://xxxx.ngrok-free.app
- 到 [LINE Developer](https://developers.line.biz/zh-hant/) 中 Channel 的 `Messaging API`，找到標籤 `Webhook URL` 將網址更新上去。
### STEP.5　打開 line 聊天機器人輸入關鍵字即可。具體請參考 `流程 C.`。

<br>

## G.　參考資源
- [Steam 教育學習網 | LINE BOT 教學](https://steam.oxxostudio.tw/)
- [作者 leVirve | 爬蟲教學 CrawlerTutorial](https://github.com/leVirve/CrawlerTutorial?tab=readme-ov-file#%E6%92%B0%E5%AF%AB%E8%87%AA%E5%B7%B1%E7%9A%84-api---%E6%8A%8A-ptt-%E5%85%A8%E5%8C%85%E4%BA%86)
- [作者 伊果 | 用爬蟲在 PTT 上監聽關鍵字並寄通知信](https://igouist.github.io/post/2019/12/ptt-crawler-and-listener/)