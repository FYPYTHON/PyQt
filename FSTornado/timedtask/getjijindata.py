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
# from tornado.log import app_log as weblog
import logging

from database.tbl_sum import TblSum
# 290007 340009
weblog = logging.getLogger("tornado.jj")
jids = ['001717', '161810', '290011', '290004', '001718', "001725", "001702", "161725", "000961",
        '001595', "160221", "002190", "001415", "001751", "001752", "003985", "001839", "001849",
        '001970', "001980"]
FDATE = "%Y-%m-%d"


def add_sum(jid, jdate, jvalue):
    tsum = db_session.query(TblJijin).filter(TblJijin.jid == jid, TblJijin.jdate <= jdate).order_by(
        TblJijin.jdate.desc()).limit(2)
    count = tsum.count()
    if count != 2:
        return None
    inc = 0
    try:
        per = (float(tsum[0].jvalue) - float(tsum[1].jvalue)) / float(tsum[1].jvalue)
        if per > 0: inc = 1
        if per < 0: inc = -1
        per = round(per * 100, 3)
        per = str(per)
    except Exception as e:
        per = "--"
    tas = db_session.query(TblSum).filter(TblSum.jid == jid, TblSum.jdate == jdate).first()
    if tas is None:
        tas = TblSum()
        tas.jdate = jdate
        tas.jid = jid
        tas.jper = per
        tas.jinc = inc
        db_session.add(tas)
        weblog.info("sum: {} {} {} add db.".format(jid, jdate, per))
    else:
        tas.jdate = jdate
        tas.jid = jid
        tas.jper = per
        tas.jinc = inc
        weblog.info("sum: {} {} {} exist then update.".format(jid, jdate, per))
    try:
        db_session.commit()
    except Exception as e:
        weblog.error("sum: {} {} {} add fail. {}".format(jid, jdate, per, e))





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


def get_holidy():
    # coding=utf-8
    import json
    import urllib3
    date = datetime.now().strftime("%Y%m%d")

    http = urllib3.PoolManager()
    server_url = "http://www.easybots.cn/api/holiday.php?d="

    vop_response = http.request('GET', server_url + date)

    vop_data = json.loads(vop_response.data)

    if vop_data[date] == '2':
        return True
    else:
        return False


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
    add_sum(jid, jdate, jvalue)


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
