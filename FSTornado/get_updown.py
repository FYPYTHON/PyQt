#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 10:16
# @Author  : 182318990@qq.com
# @File    : get_updown.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

ModelBase = declarative_base()
engine = create_engine('sqlite:////opt/midware/FSTornado/wfs.db?check_same_thread=False', echo=False)
session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)

import sys
sys.path.append("/opt/midware/FSTornado")
from datetime import datetime

def get_updown(strdate=None):
    from database.tbl_sum import TblSum
    if strdate is None:
        nowdate = datetime.now().strftime("%Y-%m-%d")
    else:
        nowdate = strdate
    data = db_session.query(TblSum.jid, TblSum.jper).filter(TblSum.jdate == nowdate).all()
    print("\t", datetime.now())
    for dt in data:
        print(dt.jid, dt.jper)
    print("--" * 10)
    db_session.close()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        arg1 = sys.argv[1]
    else:
        arg1 = None
    print("search date:", arg1)
    get_updown(arg1)