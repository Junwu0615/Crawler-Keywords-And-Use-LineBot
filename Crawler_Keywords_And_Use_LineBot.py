#爬蟲相關套件
import requests
from requests_html import HTML
from bs4 import BeautifulSoup
#表格相關套件
import rich
from rich.table import Table
#計時器相關套件
import datetime as dt
#LINEBOT相關套件
import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage

#LINE超參數
access_token = 'your channel access token'
secret = 'your channel secret'
line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(secret)
#反爬蟲設定
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
cookies = {'over18':'1'}
#其他參數
KEYWORD = ''
t = dt.datetime #顯示時間

def fetch(url):
    #傳入網址，向 PTT 回答已經滿 18 歲，回傳網頁內容
    response = requests.get(url, cookies=cookies, headers=headers)
    return response

def parse_article_entries(doc):
    #傳入網頁內容，利用 requests_html 取出 div.r-ent 的元素內容並回傳
    html = HTML( html = doc )
    post_entries = html.find('div.r-ent')
    return post_entries

def parse_article_meta(entry):
    #將<r-ent>元素的內容格式化成 dict 再回傳
    meta = {
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
        'date': entry.find('div.date', first=True).text
    }
    try:
        #正常的文章可以取得作者和連結
        meta['author'] = entry.find('div.author', first=True).text
        meta['link'] = entry.find('div.title > a', first=True).attrs['href']
    except AttributeError:
        #被刪除的文章我們就不要了
        meta['author'] = '[Deleted]'
        meta['link'] = '[Deleted]'
    return meta

def print_meta(meta):
    #將資料餵入表格，使輸出整齊一點
    '''
    data = ('{push:<3s}{date:<5s} {author:<15s}{title:<40s}'\
        .format(push = meta['push'], date = meta['date'], author = meta['author'], title = meta['title']))
    '''
    table.add_row(meta['push'], "", meta['title'], meta['author'], meta['date'], meta['link'])
    return table


# 程式本體
def ptt_alert(url, keyword):
    resp = fetch(url) # 取得網頁內容
    post_entries = parse_article_entries(resp.text) #取得各列標題
    print('[%s] 連線成功，開始搜尋目標「%s」\n' %(t.now(), keyword))
    
    #建立表格物件，供print_meta函式使用
    global table
    table = Table(show_header=True, width=120)
    table.add_column("PoP", width=0)
    table.add_column("", width=0)
    table.add_column("Title", width=15)
    table.add_column("Author", width=3)
    table.add_column("Date", width=1)
    table.add_column("URL", width=15)

    for entry in post_entries:
        meta = parse_article_meta(entry)
        #如果找到關鍵字，用LINEBOT寄通知
        if keyword in meta['title'].lower() and not "截止" in meta['title'] and not "已滿" in meta['title']:
            reply = ("已找到您所追蹤的關鍵字「{}」的文章： {} https://www.ptt.cc{}\n\n".format(keyword, meta['title'], meta['link']))
            list_article.append(reply)

        table = print_meta(meta)
        
    rich.print(table)        
    return list_article

def ptt_get_url(url):
    web = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(web.text, "html.parser") 
    tags = soup.find_all('a', class_="btn wide")
    list_ = []
    for tag in tags:
        list_.append(tag['href'])
        
    temp = int(list_[1].split('/')[-1].split('index')[-1].split('.html')[0])+1
    URL = url[:-5] + str(temp) + ".html"
    return [URL,temp]

def switch(msg): #msg(LINE輸入) = PTT BuyTogether版,disneyplus,1
    msg = msg.split(',')
    match msg[0][:3]:
        case "PTT":
            global list_article
            list_article = []
            url = "https://www.ptt.cc/bbs/" + msg[1][:-1] + "/index.html" #目標網址
            KEYWORD = msg[2].lower() #關鍵字
            URLandTemp = ptt_get_url(url)
            temp = URLandTemp[1]
            page_c = 0
            while True:
                print('[%s] 開始執行監聽' %t.now())
                rp = ptt_alert(URLandTemp[0], KEYWORD) #開始主流程
                
                page_c += 1
                temp -= 1
                URLandTemp[0] = url[:-5] + str(temp) + ".html"
                print("搜尋進度: {}/{}".format(page_c, msg[3]))
                if page_c == int(msg[3]):
                    if rp == []:
                        reply = "在該版搜尋了"+ str(msg[3]) +"頁都未找到符合關鍵字的文章 !"
                        return reply
                    reply = ''
                    for i in rp:
                        reply = reply + i
                    return reply

        case _:
            reply = 'ERROR! 格式不符合規定。'
            return reply

#主程式
app = Flask(__name__)
@app.route("/", methods=['POST'])
def main():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    signature = request.headers['X-Line-Signature']
    handler.handle(body, signature)
    tk = json_data['events'][0]['replyToken']
    type = json_data['events'][0]['message']['type']
    if type == 'text':
            msg = json_data['events'][0]['message']['text']
            reply = switch(msg)
            line_bot_api.reply_message(tk,TextSendMessage(reply))
    else:
        reply = 'ERROR! 格式不符合規定。'

    return "end"

if __name__ == "__main__":
    app.run()
