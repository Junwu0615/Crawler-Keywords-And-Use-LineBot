# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
import requests

class BaseLogic:
    def __init__(self):
        pass

    def get_source(self, url) -> requests.Response:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        res = requests.get(url, cookies={'over18': '1'}, headers=headers)
        return res