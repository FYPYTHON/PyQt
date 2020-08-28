#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 9:20
# @Author  : 1823218990@qq.com
# @File    : scrapygushiwen.py
# @Software: PyCharm
import re
import requests
from bs4 import BeautifulSoup
from dscrapy.getmore import get_describe_detail
url_root = "https://m.gushiwen.org"
url_gsc = "https://m.gushiwen.org/gushi/tangshi.aspx"

urls = []


def fmtprint(jres):
    import json
    try:
        jres = eval(jres)
    except:
        pass
    jsonf = json.dumps(jres, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    # jsone = json.dumps(jres, sort_keys=True, indent=4, separators=(',', ':'))
    print(jsonf)


def post_poem(url, params):
    url = 'http://{}/study'.format(url)
    headers = {"User-Agent": "Mobile"}
    params = params
    # result = requests.get(url, headers=headers, params=params)
    result = requests.post(url, headers=headers, data=params)
    fmtprint(result.content)


def put_poem(url, params):
    url = 'http://{}/study'.format(url)
    headers = {"User-Agent": "Mobile"}
    params = params
    # result = requests.get(url, headers=headers, params=params)
    result = requests.put(url, headers=headers, data=params)
    fmtprint(result.content)

def main():
    html_base = requests.get(url_gsc)
    soup = BeautifulSoup(html_base.text, 'lxml')
    spans = soup.find_all("span")
    for item in spans:
        a = item.find("a")
        if a is not None and "href" in a.__dict__['attrs'].keys():
            urls.append(a['href'])
        # break
    # print(urls)
    # print(len(urls))
    parse_detail(urls)

def parse_detail(urls):
    poem_list = list()
    for url in urls:
        poem = dict()
        full_url = url_root + url
        html_detail = requests.get(full_url)
        soup = BeautifulSoup(html_detail.text, 'lxml')
        # print(soup)
        content = soup.find("div", {"class": "contson"}).getText()
        poem["content"] = content
        title = soup.find("h1").text
        poem["title"] = title
        p = soup.find("p", {"class": "source"}).find_all("a")
        # print(p.find_all("a"))
        category = p[0].text
        poet = p[1].text
        # print(category, poet)
        poem["category"] = category
        poem["poet"] = poet
        poem["agg"] = u"唐诗三百首"

        # # p_detail = soup.find("p", {"text": u"译文"})
        # p_detail = soup.find_all("p")[1:6]
        # zs = p_detail[1].text
        # yw = p_detail[0].text
        # describe = zs[0:2] + "\n" + zs[2:] + "\n"
        # describe += yw[0:2] + "\n" + yw[2:] + "\n"
        # describe += p_detail[2].text + "\n"
        # describe += p_detail[3].text + "\n"
        # # describe += p_detail[4].text + "\n"
        # # describe += p_detail[5].text

        # poem["describe"] = describe.replace(u"\u3000", u'    ')
        # print(full_url)
        poem["describe"] = get_describe_detail(full_url)
        poem_list.append(poem)

        # print(poem['describe'])
        import time
        time.sleep(2)
        # post to db
        # post_poem("127.0.0.1:9080", poem)   # add
        put_poem("127.0.0.1:9080", poem)      # modify
    print(len(poem_list))
    with open("poem.json", 'w') as f:
        import json
        json.dump(poem_list, f)


if __name__ == "__main__":
    main()

