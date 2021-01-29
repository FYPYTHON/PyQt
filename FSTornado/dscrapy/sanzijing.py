#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 13:53
# @Author  : 1823218990@qq.com
# @File    : sanzijing.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("../")
from database.tbl_poetry import TblPoetry
url = 'https://sanzijing.bmcx.com/'
def main():
    html_base = requests.get(url)
    soup = BeautifulSoup(html_base.text, 'lxml')
    # print(soup)
    m_content = soup.find("div", {"class": "szj_nr"})
    lis = m_content.find_all("li")
    sanzijing = []
    count = 1
    for li in lis:
        # print(li)
        spans = li.find_all("span", {"class": ""})
        ps = li.find_all("p", {"class": ""})
        try:
            gene_dict(spans, ps, count)
            count += 1
        except Exception as e:
            print(e)
            print(spans, ps)
            break
        # return


def gene_dict(spans, ps, count):
    szj = dict()
    content = spans[0].text + "," + spans[1].text + "。\n" + spans[2].text + "," + spans[3].text + "。"
    szj["content"] = content
    szj["title"] = u"节选 "+ str(count) + "·" + spans[0].text
    szj["poet"] = ""
    if len(ps) == 2:
        describe = ps[0].text + '\n' + ps[1].text
    else:
        describe = ''
        for p in ps:
            describe += p.text + '\n'

    szj["describe"] = describe
    szj["category"] = u""
    szj["agg"] = u"三字经"
    # print(szj)
    add_szj_to_db(szj)



def mydb():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    from sqlalchemy.ext.declarative import declarative_base
    import pymysql
    pymysql.install_as_MySQLdb()

    ModelBase = declarative_base()
    import platform
    if platform.system() == "Windows":
        engine = create_engine('sqlite:///D:/project/notes/FSTornado/wfs.db?check_same_thread=False', echo=False)
    else:
        engine = create_engine('sqlite:////opt/midware/FSTornado/wfs.db?check_same_thread=False', echo=False)
    session_factory = sessionmaker(bind=engine)
    db_session = scoped_session(session_factory)
    return db_session


def add_szj_to_db(szj):
    db = mydb()
    exist = db.query(TblPoetry).filter(TblPoetry.agg == szj['agg'], TblPoetry.title == szj['title']).first()
    if exist:
        print("is exist", exist.id)
    else:
        # tbl = TblPoetry(szj)
        # db.add(tbl)
        # db.commit()
        tbl = TblPoetry()
        for k,v in szj.items():
            tbl.__setattr__(k, v)
        db.add(tbl)
        db.commit()
        # print(tbl.describe)



if __name__ == '__main__':
    main()