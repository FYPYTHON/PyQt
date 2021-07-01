#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 15:17
# @Author  : 1823218990@qq.com
# @File    : api_test3.py
# @Software: PyCharm

import sys
sys.path.append("/opt/midware/FSTornado/python3_fs/lib/python3.5/site-packages")
import requests

user = "a123456"
pwd = "123456"


def get_token(url):
    url = 'http://{}/login'.format(url)
    headers = {'User-Agent': "Mobile"}
    parmas = {"loginname": user, "userAccount": user, "password": pwd, "inputCode": "APP"}
    result = requests.post(url, data=parmas, headers=headers)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    print(result.text)
    # print(result.content)
    res = result.content.decode('utf-8')
    jres = eval(res)
    # fmtprint(jres)
    if "token" in jres:
        return jres.get("token")
    return result.text


def get_sma(url):
    headers = {'User-Agent': 'Mobile'}
    token = get_token(url)
    parmas = {'loginname': user, 'token': token, "jid": "161725", "wmin": 7, "wmax": 30}
    url = 'http://{}/app/sma'.format(url)
    res = requests.get(url, headers=headers, data=parmas).text
    print(res)


if __name__ == '__main__':
    url = "127.0.0.1:9016"
    get_sma(url)