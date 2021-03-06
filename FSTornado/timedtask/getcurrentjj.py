#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 9:55
# @Author  : 1823218990@qq.com
# @File    : getcurrentjj
# @Software: Pycharm
from threading import Timer
import time
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# from tornado.log import app_log as weblog
from timedtask.getjijindata import FDATE, add_data, jids, add_sum

weblog = logging.getLogger("tornado.jj")


def get_current_data(jid):
    jurl = 'https://m.dayfund.cn/fundinfo/{}.html#jump=search'.format(jid)
    html = requests.get(jurl)
    # res = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
    res = html.text
    soup = BeautifulSoup(res, 'lxml')
    try:
        span_v = soup.find("span", {"id": "fvr_val"}).text
        span_d = soup.find("span", {"id": "fvr_dt"}).text
    except Exception as e:
        time.sleep(0.5)
        jurl = 'https://m.dayfund.cn/fundinfo/{}.html#jump=search'.format(jid)
        html = requests.get(jurl)
        # res = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
        res = html.text
        soup = BeautifulSoup(res, 'lxml')
        span_v = soup.find("span", {"id": "fvr_val"})
        span_d = soup.find("span", {"id": "fvr_dt"})
        span_v = span_v.text
        span_d = span_d.text

    jvalue = span_v.split(",")[0]
    jdate = span_d.split(" ")[0]
    # weblog.info("{} {} {} current data ready to add db".format(jid, jdate, jvalue))
    if jvalue == '' or len(jvalue) < 1:
        weblog.error("{} is not invalid. not to add db".format(jvalue))
        return

    today = datetime.today().date()

    if today.strftime(FDATE) != jdate:
        weblog.error("{} {} {} is not the same".format(jid, today, jdate))
        return None
    add_data(jid, jdate, jvalue)
    add_sum(jid, jdate, jvalue)


def get_current_num(jid):
    jurl = 'http://fund.eastmoney.com/{}.html?spm=aladin'.format(jid)
    # print(jurl)
    html = requests.get(jurl)
    # print(html)
    # res = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
    res = html.text
    soup = BeautifulSoup(res, 'lxml')
    # print(html.text)
    jjdate = soup.find("div", {"class": "dataOfFund"})
    jjdate1 = jjdate.find("dl", {"class": "dataItem01"})
    dstr = jjdate1.find("span", {"id": "gz_gztime"}).text
    if dstr:
        sdate = dstr.strip("(|)").split(" ")
        # print(jid, sdate[0])
    else:
        sdate = None

    dd = soup.find('dd', {"class": "dataNums"})
    # print(dd)
    d1 = dd.find("dl", {"class": "floatleft"})
    # print(d1)
    if d1 is not None:
        b = d1.find("span", {"id": "gz_gsz"})
        value = b.text
        # print(value)
    else:
        value = None
    weblog.info("{} {} {} current to add db".format(jid, sdate[0], value))
    # print(jid, sdate[0], value)
    add_current_data(jid, sdate[0], value)
    return jid, sdate[0], value


def add_current_data(jid, jdate, jvalue):
    if jdate is None or jvalue is None:
        # weblog.error("jdate or jvalue is None. ".format(jdate, jvalue))
        return None

    if jvalue == "--" or jdate == "--":
        # weblog.error("{} {}is not invlade".format(jdate, jvalue))
        return None

    today = datetime.today().date()
    today.strftime(FDATE)

    if today != jdate:
        weblog.error("{} {}is not the same".format(today, jdate))
        return None

    # weblog.info("{} {} {} , to add db.".format(jid, jdate, jvalue))
    # add_data(jid, jdate, jvalue)


def gene_jijin_current():
    if datetime.today().hour < 16 and (datetime.today().hour >= 9):
        weblog.info("gene_jijin_current start")
        for jid in jids:
            try:
                if datetime.today().hour > 15 or (datetime.today().hour < 9):
                    continue
                # get_current_num(jid)
                get_current_data(jid)
            except Exception as e:
                weblog.error("{} {}".format(jid, e))

    jjd = Timer(1 * 60 * 10, gene_jijin_current)
    jjd.start()


if __name__ == '__main__':
    # j0, j1, j2 = get_current_num("161826")
    # add_current_data(j0, j1, j2)
    gene_jijin_current()
    # get_current_data("001717")