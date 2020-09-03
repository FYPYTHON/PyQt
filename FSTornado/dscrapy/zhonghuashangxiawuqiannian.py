#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 9:17
# @Author  : 1823218990@qq.com
# @File    : zhonghuashangxiawuqiannian.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
from dscrapy.scrapygushiwen import fmtprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

ModelBase = declarative_base()
engine = create_engine('sqlite:///../wfs.db?check_same_thread=False', echo=False)
session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)



agg = u"中华上下五千年"
category = u"文章"
author = u'皮皮作文网'
root_url = 'https://mip.ppzuowen.com/book/zhonghuashangxiawuqiannian/'




def post_poem(params):
    # print("post...")
    from database.tbl_alticle import TblAlticle
    exist = db_session.query(TblAlticle).filter(TblAlticle.author == params.get("author")
                                                , TblAlticle.agg == agg
                                                , TblAlticle.title == params.get("title")).first()
    if exist is not None:
        print("exist ...", params.get("title"))
        exist.initjson(params)
    else:
        print("add...", params.get("title"))
        ta = TblAlticle()
        ta.initjson(params)
        db_session.add(ta)
    db_session.commit()
    import time
    time.sleep(1)



def get_all_index():
    html = requests.get(root_url)
    encoding = html.encoding
    res = html.text.encode(encoding).decode(requests.utils.get_encodings_from_content(html.text)[0])

    soup = BeautifulSoup(res, 'lxml')

    divs = soup.find('div', {"class": "index_list"})

    alinks = divs.find_all('a', {"target": "_blank"})
    urls = []
    for a in alinks:
        # print(a.text)
        urls.append(a['href'])
    print(len(urls))
    # print(urls[1])
    get_content(urls)
    return urls


def get_content(urls):
    cxt = []
    for url in urls:
        html = requests.get(url)
        encoding = html.encoding
        res = html.text.encode(encoding).decode(requests.utils.get_encodings_from_content(html.text)[0])
        soup = BeautifulSoup(res, 'lxml')
        divs = soup.find("div", {"class": 'articleContent'})
        print(url)
        title = soup.find("div", {"class": "kind"}).find("h1", {"class": "h11"}).text

        describe = ''
        content = ""
        if divs is not None:
            ps = divs.find_all('p')

            for p in ps:
                content += "\t" + p.text + "\n"
            # print(content)
            cxt.append(content)

        article = dict(
            title=title,
            describe=describe,
            content=content,
            agg=agg,
            category=category,
            author=author
        )
        post_poem(article)

        if len(cxt) >= 2:
            # break
            pass


if __name__ == '__main__':
    get_all_index()

