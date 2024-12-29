# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
from flask import Flask
from linebot.models import TextSendMessage
from package.linebot import LineBotProcess

lbp = LineBotProcess()
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    linebot_api, handler = LineBotProcess.token_settings()
    body, loader, reply_token, event_type = LineBotProcess.initial_body()

    if event_type == 'text':
        reply = lbp.switch(loader['events'][0]['message']['text'])
    else:
        reply = f'ERROR 格式不符合規定 -> {event_type}'

    linebot_api.reply_message(reply_token, TextSendMessage(reply))
    return 'end'

if __name__ == '__main__':
    app.run()