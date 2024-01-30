# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
from rich.table import Table
from bs4 import BeautifulSoup
from requests_html import HTML
from Depend.BaseLogic import BaseLogic

class PttFormat(BaseLogic):
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def ptt_entries(doc):
        html = HTML(html=doc)
        post_entries = html.find('div.r-ent')
        return post_entries

    @staticmethod
    def ptt_meta(entry) -> dict:
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

    @staticmethod
    def ptt_generate_url(base, idx) -> str:
        return base + str(idx) + '.html'

    def get_url(self, event_task) -> tuple:
        url = 'https://www.ptt.cc/bbs/' + event_task + '/index.html'
        res = self.get_source(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        tags = soup.find_all('a', class_='btn wide')
        if tags != []:
            temp = [tag['href'] for tag in tags]
            idx = int(temp[1].split('/index')[-1].replace('.html', '')) + 1
            base = url.split('/index')[0] + '/index'
            return base, idx
        else:
            return soup.find_all('title')[0].text, None

    def search(self, url, kw):
        res = self.get_source(url)
        post_entries = PttFormat.ptt_entries(res.text)
        table = Table(show_header=True, width=120)
        table.add_column('PoP', width=0)
        table.add_column("", width=0)
        table.add_column('Title', width=15)
        table.add_column('Author', width=3)
        table.add_column('Date', width=1)
        table.add_column('URL', width=15)
        for entry in post_entries:
            meta = PttFormat.ptt_meta(entry)
            if kw in meta['title'].lower() and not '截止' in meta['title'] and not '已滿' in meta['title']:
                message = f"{meta['title']} https://www.ptt.cc{meta['link']}\n\n"
                self.obj.deque_article.append(message)
            table.add_row(meta['push'], "", meta['title'], meta['author'], meta['date'], meta['link'])
        # self.obj.console.print(table)