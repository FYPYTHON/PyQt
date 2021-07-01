#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 23:02
# @Author  : 1823218990@qq.com
# @File    : jjgz
# @Software: Pycharm

import requests
from bs4 import BeautifulSoup

def get_history(jid):
    jurl = 'http://fundf10.eastmoney.com/jjjz_{}.html'.format(jid)
    s = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    headers['Upgrade-Insecure-Requests'] = "1"
    html = s.get(jurl, headers=headers)
    res = html.text
    soup = BeautifulSoup(res, 'lxml')
    # //*[@id="jztable"]/table
    # print(soup)
    tbody = soup.find('table', {"class": "w782 comm lsjz"})
    # print(tbody)
    if tbody is not None:
        trs = tbody.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            jdate = tds[0]
            jvalue = tds[1]
            print(jdate, jvalue)
    # print(html.cookies)
    ck = html.cookies
    ck_json = requests.utils.dict_from_cookiejar(ck)
    # ck_json = dict()
    # rck = "qgqp_b_id=d0ada305fb3a07ba970c0bab89c7d6b6; st_si=28917450144567; st_pvi=91264286346522; st_sp=2021-05-07%2020%3A14%3A49; st_inirUrl=http%3A%2F%2Ffund.eastmoney.com%2Ffund.html; st_sn=1; st_psi=20210622214006169-112200305283-5417210808; st_asi=delete"
    # for item in rck.split(";"):
    #     key, value = item.strip().split("=")
    #     ck_json[key] = value
    # ck_json['ASL'] = '18754,0000u,b4a2299f'
    # ck_json['ADVC'] = '39915bb755ee67'
    # ck_json['searchbar_code'] = '161725'
    # ck_json['ASP.NET_SessionId'] = 'i0tgzzffblurlfebkw1vaath'

    hed = html.headers
    # hed = dict()
    hed['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    hed['Upgrade-Insecure-Requests'] = "1"
    hed["Referer"] = "http://fundf10.eastmoney.com/"
    hed["Host"] = "api.fund.eastmoney.com"
    # hed["Accept"] = "*/*"
    print(ck_json)
    print(hed)
    zurl = "http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery1830018839118575611158_1624369206219&fundCode=001717&pageIndex=2&pageSize=20&startDate=&endDate=&_=1624369220274"
    cb = s.get(zurl, cookies=ck_json, headers=hed, timeout=4)
    print(cb.text)
    # cb = s.get(zurl)
    # print(cb.text)

def get_jquery(jid):
    jurl = 'http://fundf10.eastmoney.com/jjjz_{}.html'.format(jid)
    s = requests.Session()
    html = s.get(jurl)
    cookies = requests.utils.dict_from_cookiejar(html.cookies)
    print(cookies)
    res = html.text
    soup = BeautifulSoup(res, 'lxml')
    print(soup)
    # s.get("http://fundact.eastmoney.com/banner/hqb_hq.html?spm=001001.sbb")
    # s.get("http://fundact.eastmoney.com/banner/hot_em.html?spm=001001.rw")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    # cookies = {}
    res = s.get("http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18305789194531974211_1624370689631&fundCode=001717&pageIndex=1&pageSize=20&startDate=&endDate=&_=1624370689667"
                , headers=headers
                , cookies=cookies
                )
    print(res.text)
    # print(soup)


if __name__ == '__main__':
    # get_history("001717")
    get_jquery("001717")