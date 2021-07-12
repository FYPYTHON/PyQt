#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 21:38
# @Author  : 1823218990@qq.com
# @File    : init_jj
# @Software: Pycharm
import sys
sys.path.append("/opt/midware/FSTornado/python3_fs/lib/python3.5/site-packages")
from database.db_config import db_session
from database.tbl_jijin import TblJijin
from database.tbl_sum import TblSum


def init_from_selenium(jid):

    # jid = "002190"
    filename = "{}.txt".format(jid)
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            jdate, jvalue, jper = line.strip("\n").split(" ")
            add_to_db(jid, jdate, jvalue, jper)


def add_to_db(jid, jdate, jvalue, jper):

    jj = TblJijin()
    jj.jid = jid
    jj.jdate = jdate
    jj.jvalue = jvalue
    jsum = TblSum()
    jsum.jid = jid
    jsum.jdate = jdate
    jsum.jper = jper
    try:
        jsum.jinc = 1 if float(jper) > 0 else 0 if int(jper) == 0 else -1
    except Exception as e:
        jsum.jinc = 0
    try:
        db_session.add(jj)
        db_session.add(jsum)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
    db_session.close()


if __name__ == '__main__':
    init_from_selenium("001980")
