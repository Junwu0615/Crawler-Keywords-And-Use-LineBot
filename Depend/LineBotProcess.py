# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
import json
from tqdm import tqdm
from flask import request
from datetime import datetime
from collections import deque
from rich.console import Console
from linebot import LineBotApi, WebhookHandler

from Depend.PttFormat import PttFormat
from Depend.BaseLogic import BaseLogic

class LineBotProcess(BaseLogic):
    def __init__(self):
        self.deque_article = deque([])
        self.console = Console()
        self.ptt = PttFormat(self)

    @staticmethod
    def initial_body() -> tuple:
        body = request.get_data(as_text=True)
        loader = json.loads(body)
        # handler.handle(body, request.headers['X-Line-Signature'])
        reply_token = loader['events'][0]['replyToken']
        event_type = loader['events'][0]['message']['type']
        return body, loader, reply_token, event_type

    @staticmethod
    def token_settings() -> tuple:
        linebot_api, handler = None, None
        for _ in [i for i in open('Depend/token.txt', 'r')]:
            idx = _.split(',')
            if idx[0] == 'access_token':
                linebot_api = LineBotApi(idx[1].replace('\n', ''))
            elif idx[0] == 'secret':
                handler = WebhookHandler(idx[1].replace('\n', ''))
            else:
                print('*** [token_settings] Other Error ***')

        return linebot_api, handler

    def switch(self, msg):
        msg = msg.split(',')
        event_type = msg[0].lower()
        match event_type:
            case 'ptt':
                event_task = msg[1].replace('版', '')
                kw = msg[2].lower()  # 關鍵字
                max_pages = int(msg[3]) # 最大搜尋頁數
                page, self.deque_article = 1, deque([])
                base, idx = self.ptt.get_url(event_task)
                if idx is None:
                    return base
                else:
                    desc = f'[{datetime.now()}] 開始執行 | 監聽關鍵字: {kw} | 搜尋進度'
                    self.deque_article.appendleft(f'已找到您所追蹤的關鍵字「{kw}」的文章： \n')
                    for page in tqdm(range(1, max_pages+1), position=0, desc=desc):
                        self.ptt.search(url=PttFormat.ptt_generate_url(base, idx), kw=kw)
                        page += 1
                        idx -= 1
                    if len(self.deque_article) == 0: return '在該版搜尋了' + str(max_pages) + '頁都未找到符合關鍵字的文章 !'
                    else: return ''.join([i for i in self.deque_article])

            case _:
                return 'ERROR! 格式不符合規定。'