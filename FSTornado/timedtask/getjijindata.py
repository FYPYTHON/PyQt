#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 9:21
# @Author  : 1823218990@qq.com
# @File    : getjijindata.py
# @Software: PyCharm
from threading import Timer

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from database.db_config import db_session
from database.tbl_jijin import TblJijin
from tornado.log import app_log as weblog
jids = ['001717', '161810', '340009', '290011', '290004', '290007', '001718', "001725", "161826", "001668", "161725"]
FDATE = "%Y-%m-%d"


def add_data(jid, jdate, jvalue):
    tjj = db_session.query(TblJijin).filter(TblJijin.jid == jid, TblJijin.jdate == jdate).first()
    if tjj is None:
        tjj = TblJijin()
        tjj.jid = jid
        tjj.jdate = jdate
        tjj.jvalue = jvalue
        db_session.add(tjj)
        weblog.info("{} {} {} add db.".format(jid, jdate, jvalue))
    else:
        tjj.jid = jid
        tjj.jdate = jdate
        tjj.jvalue = jvalue
        weblog.info("{} {} {} exist then update.".format(jid, jdate, jvalue))
    try:
        db_session.commit()
    except Exception as e:
        weblog.error("{} {} {} add fail. {}".format(jid, jdate, jvalue, e))


def get_date():
    today = datetime.today().date()
    # today = datetime.strptime("2020-09-19", FDATE)
    weekday = today.weekday()
    if weekday == 0:
        today = today - timedelta(days=3)
    if 0 < weekday <= 4:
        today = today - timedelta(days=1)
    while weekday > 4:
        today = today - timedelta(days=1)
        weekday = today.weekday()
    # print(today, weekday)
    strdata = today.strftime(FDATE)
    # strdata = "2020-11-06"
    # print(strdata)
    return strdata


def get_one(jid):
    jurl = 'http://fundf10.eastmoney.com/jjjz_{}.html'.format(jid)
    # print(jurl)
    html = requests.get(jurl)
    # print(html)
    # res = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
    res = html.text
    soup = BeautifulSoup(res, 'lxml')
    # print(html.text)
    div = soup.find('div', {"class": "col-right"})
    # print(div)
    b = div.find("b", {"class": "red lar bold"})
    if b is None:
        b = div.find("b", {"class": "grn lar bold"})
    # print(b)
    jdata = b.text.strip("\r\n").strip(" ").split(" ")[0]

    jdate = get_date()
    jvalue = jdata
    # print(jid, jdate, jvalue)
    # add data to db
    add_data(jid, jdate, jvalue)


def gene_jijin_data():
    weblog.info("gene_jijin_data start")
    for jid in jids:
        try:
            if datetime.today().hour > 16:
                continue
            get_one(jid)
        except Exception as e:
            weblog.error("{} {}".format(jid, e))

    jjd = Timer(12 * 60 * 60, gene_jijin_data)
    jjd.start()


if __name__ == '__main__':
    gene_jijin_data()
    # get_date()
    # get_one(jids[1])
