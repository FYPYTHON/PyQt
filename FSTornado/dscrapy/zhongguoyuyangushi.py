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

# agg = u"中国寓言故事"
agg = u"少儿故事"
category = u"故事"
author = u'皮皮作文网'
root_url = ['https://mip.ppzuowen.com/book/zhongguoyuyangushi/',
            'https://mip.ppzuowen.com/book/shaoergushi/',
            'https://mip.ppzuowen.com/book/gongzhugushi/', 'https://mip.ppzuowen.com/book/wangzigushi/',
            'https://mip.ppzuowen.com/book/yaomoguiguaigushi/', 'https://mip.ppzuowen.com/book/zheligushi/',
            'https://mip.ppzuowen.com/book/dongwugushi/', 'https://mip.ppzuowen.com/book/muaigushi/',
            'https://mip.ppzuowen.com/book/fuaigushi/', 'https://mip.ppzuowen.com/book/zhongguominjiangushi/',
            'https://mip.ppzuowen.com/book/shuiqian/', 'https://mip.ppzuowen.com/book/baobaoshuiqiangushidaquanji/',
            'https://mip.ppzuowen.com/book/aiguogushi/', 'https://mip.ppzuowen.com/book/yingxionggushi/',
            'https://mip.ppzuowen.com/book/2suishuiqiangushi/', 'https://mip.ppzuowen.com/book/4suishuiqiangushi/',
            'https://mip.ppzuowen.com/book/5suishuiqiangushi/', 'https://mip.ppzuowen.com/book/7suiertonggushi/',
            'https://mip.ppzuowen.com/book/youergushi/', 'https://mip.ppzuowen.com/book/shaoershuiqiangushi/',
            'https://mip.ppzuowen.com/book/ertongminjiangushi/', 'https://mip.ppzuowen.com/book/ertongyizhigushi/',
            'https://mip.ppzuowen.com/book/ertongxiaohuagushi/', 'https://mip.ppzuowen.com/book/ertonglizhigushi/',
            'https://mip.ppzuowen.com/book/xilashenhuaxiaogushi/', 'https://mip.ppzuowen.com/book/alaboshenhuagushi/',
            'https://mip.ppzuowen.com/book/yindianshenhuagushi/', 'https://mip.ppzuowen.com/book/aijishenhuagushi/',
            'https://mip.ppzuowen.com/book/feizhoushenhuagushi/', 'https://mip.ppzuowen.com/book/beioushenhuagushi/',
            'https://mip.ppzuowen.com/book/eluosishenhuagushi/', 'https://mip.ppzuowen.com/book/linhandalishigushiji/',
            'https://mip.ppzuowen.com/book/sanzijinggushidaquan/', 'https://mip.ppzuowen.com/book/yiqianlingyiyegushi/',
            'https://mip.ppzuowen.com/book/shiershengxiaodegushi/', 'https://mip.ppzuowen.com/book/hulijingdegushi/',
            'https://mip.ppzuowen.com/book/sanguosanshiliujigushi/',
            'https://mip.ppzuowen.com/book/zhongguoxiaoxueshenglishigushi/',
            'https://mip.ppzuowen.com/book/xinlingjitangxiaogushi/', 'https://mip.ppzuowen.com/book/gaoerjidegushi/',
            'https://mip.ppzuowen.com/book/hongjunchangzhengdegushi/', 'https://mip.ppzuowen.com/book/yuefeidegushi/',
            'https://mip.ppzuowen.com/book/zhouenlaidegushi/', 'https://mip.ppzuowen.com/book/lieningdegushi/',
            'https://mip.ppzuowen.com/book/quyuandegushi/', 'https://mip.ppzuowen.com/book/zhugeliangdegushi/',
            'https://mip.ppzuowen.com/book/huiguniangdegushi/', 'https://mip.ppzuowen.com/book/xiaohongmaodegushi/',
            'https://mip.ppzuowen.com/book/aidegushi/', 'https://mip.ppzuowen.com/book/shengjingshenhuagushi/',
            'https://mip.ppzuowen.com/book/luomashenhuagushi/', 'https://mip.ppzuowen.com/book/kongzidegushi/',
            'https://mip.ppzuowen.com/book/shaoergushi/bingxueqiyuandegushi/',
            'https://mip.ppzuowen.com/book/shaoergushi/baixuegongzhudegushi/'
            ]

index = 2


def post_alticle(params):
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


def get_all_index(index=index):
    html = requests.get(root_url[index])
    encoding = html.encoding
    res = html.text.encode(encoding).decode(requests.utils.get_encodings_from_content(html.text)[0])

    soup = BeautifulSoup(res, 'lxml')

    divs = soup.find('div', {"class": "index_list"})

    alinks = divs.find_all('a', {"target": "_blank"})

    category = soup.find("h1", {"class": "htitle111"}).text
    urls = []
    for a in alinks:
        # print(a.text)
        urls.append(a['href'])
    print(len(urls))
    # print(urls[1])
    # print(urls)
    print(category)
    get_content(urls, category)
    return urls


def get_content(urls, category=category):
    cxt = []
    for url in urls:
        html = requests.get(url)
        encoding = html.encoding
        res = html.text.encode(encoding).decode(requests.utils.get_encodings_from_content(html.text)[0])
        soup = BeautifulSoup(res, 'lxml')
        divs = soup.find("div", {"class": 'articleContent'})
        # print(url, category)
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
        post_alticle(article)

        if len(cxt) >= 2:
            print(len(cxt), len(urls), index)
            # break
            pass


if __name__ == '__main__':
    for i in range(21, 54):
        get_all_index(i)
