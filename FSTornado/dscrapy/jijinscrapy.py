#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 13:02
# @Author  : 1823218990@qq.com
# @File    : jijinscrapy.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
url = "https://m.1234567.com.cn/index.html?page=jjxq&code=001717"

one = 'http://fundf10.eastmoney.com/jjjz_001717.html'

def get_jijin_by_id(jid):
    html = requests.get(url)
    print(html.encoding)
    res = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])

    soup = BeautifulSoup(res, 'lxml')
    # print(html.text)
    soup.p.encode("utf-8")
    print(soup.prettify())

def get_other():
    html = requests.get(one)
    print(html.encoding)
    # res = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
    res = html.text
    soup = BeautifulSoup(res, 'lxml')
    # print(html.text)
    soup.p.encode("utf-8")
    print(soup.prettify())


if __name__ == '__main__':
    # get_jijin_by_id("001717")
    get_other()
    #1 3.2730 - 3.3117
    #0 3.2715 - 3.3450
