#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 14:29
# @Author  : 1823218990@qq.com
# @File    : hd_jsum.py
# @Software: PyCharm

from tornado.web import authenticated
from tornado.log import app_log as weblog
from common.global_func import get_user_info, DATE_FORMAT
from common.common_base import DatetimeManage
from common.msg_def import WEEK_DAY
from handlers.basehd import BaseHandler, check_token, check_authenticated
from database.tbl_jijin import TblJijin
from database.tbl_sum import TblSum
from datetime import datetime, timedelta
from sqlalchemy import distinct
import json

from handlers.view.hd_jijin import get_gid


def getDailyUpDownInfo(self, cdate):
    sumdata = self.mysqldb().query(TblSum).filter(TblSum.jdate == cdate)
    totol = sumdata.count()
    if totol < 1:
        return None
    sumdata = sumdata.all()
    up = len([i.jper for i in sumdata if i.jper != '--' and float(i.jper) > 0])
    down = len([i.jper for i in sumdata if i.jper != '--' and float(i.jper) < 0])
    mid = totol - up - down
    print(totol, up, down, mid)
    return cdate, totol, up, down, mid


def getRangeUpDownInfo(self, days):
    data = []
    for day in range(days):
        cdate = (datetime.now() - timedelta(days=day)).strftime(DATE_FORMAT)
        onedata = getDailyUpDownInfo(self, cdate)
        if onedata:
            data.append(onedata)
    return data


class JSumHandler(BaseHandler):
    def get(self):
        cday = self.get_argument("cday", '0')
        crange = self.get_argument("range", "yes")
        if not cday.isdigit():
            return self.write(json.dumps({"error_code":1, "msg":"cday is str", "data": []}))
        cday = int(cday)
        if crange == "yes":
            data = getRangeUpDownInfo(self, cday)
            pass
        else:
            cdate = (datetime.now() - timedelta(days=cday)).strftime(DATE_FORMAT)
            data = getDailyUpDownInfo(self, cdate)
        return self.write(json.dumps({"error_code":0, "msg":"", "data": data}))