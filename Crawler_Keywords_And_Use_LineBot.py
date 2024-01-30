import rich
import json
import requests
import datetime as dt
from rich.table import Table
from bs4 import BeautifulSoup
from requests_html import HTML
from flask import Flask, request
from linebot.models import TextSendMessage
from linebot import LineBotApi, WebhookHandler

# LINE Parameter
access_token = 'your channel access token'
secret = 'your channel secret'
line_bot_api = LineBotApi(access_token); handler = WebhookHandler(secret); 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
cookies = {'over18':'1'}; KEYWORD = ''; t = dt.datetime; 

def fetch(url):
    return requests.get(url, cookies=cookies, headers=headers)

def parse_article_entries(doc):
    html = HTML( html = doc ); post_entries = html.find('div.r-ent'); 
    return post_entries

def parse_article_meta(entry):
    meta = {'title': entry.find('div.title', first=True).text,
            'push': entry.find('div.nrec', first=True).text,
            'date': entry.find('div.date', first=True).text}
    try:
        meta['author'] = entry.find('div.author', first=True).text
        meta['link'] = entry.find('div.title > a', first=True).attrs['href']
    except AttributeError:
        meta['author'] = '[Deleted]'
        meta['link'] = '[Deleted]'
    return meta

def print_meta(meta):
    table.add_row(meta['push'], "", meta['title'], meta['author'], meta['date'], meta['link'])
    return table

def ptt_alert(url, keyword):
    resp = fetch(url); post_entries = parse_article_entries(resp.text); 
    print('[%s] 連線成功，開始搜尋目標「%s」\n' %(t.now(), keyword))
    global table
    table = Table(show_header=True, width=120)
    table.add_column("PoP", width=0); table.add_column("", width=0); 
    table.add_column("Title", width=15); table.add_column("Author", width=3); 
    table.add_column("Date", width=1); table.add_column("URL", width=15); 
    for entry in post_entries:
        meta = parse_article_meta(entry)
        if keyword in meta['title'].lower() and not "截止" in meta['title'] and not "已滿" in meta['title']: list_article.append(f"已找到您所追蹤的關鍵字「{keyword}」的文章： {meta['title']} https://www.ptt.cc{meta['link']}\n\n")
        table = print_meta(meta)
    rich.print(table)        
    return list_article

def ptt_get_url(url):
    web = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(web.text, "html.parser") 
    tags = soup.find_all('a', class_="btn wide")
    list_ = []
    for tag in tags: list_.append(tag['href'])
    temp = int(list_[1].split('/')[-1].split('index')[-1].split('.html')[0])+1
    URL = url[:-5] + str(temp) + ".html"
    return [URL,temp]

def switch(msg):
    msg = msg.split(',')
    match msg[0][:3]:
        case "PTT":
            global list_article
            url = "https://www.ptt.cc/bbs/" + msg[1][:-1] + "/index.html"
            list_article = []; KEYWORD = msg[2].lower(); URLandTemp = ptt_get_url(url); 
            temp = URLandTemp[1]; page_c = 0; 
            while True:
                print('[%s] 開始執行監聽' %t.now())
                rp = ptt_alert(URLandTemp[0], KEYWORD)
                page_c += 1; temp -= 1; 
                URLandTemp[0] = url[:-5] + str(temp) + ".html"
                print("搜尋進度: {}/{}".format(page_c, msg[3]))
                if page_c == int(msg[3]):
                    if rp == []: return "在該版搜尋了"+ str(msg[3]) +"頁都未找到符合關鍵字的文章 !"
                    reply = ''
                    for i in rp: reply = reply + i
                    return reply
        case _: return 'ERROR! 格式不符合規定。'

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
    else: reply = 'ERROR! 格式不符合規定。'
    return "end"

if __name__ == "__main__":
    app.run()