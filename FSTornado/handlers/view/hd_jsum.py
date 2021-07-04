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
from handlers.basehd import BaseHandler, check_token, check_authenticated, check_only
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
    # weblog.info("{} {} {} {}".format(totol, up, down, mid))
    return cdate, totol, up, down, mid


def getRangeUpDownInfo(self, days):
    data = []
    for day in range(days):
        cdate = (datetime.now() - timedelta(days=day)).strftime(DATE_FORMAT)
        onedata = getDailyUpDownInfo(self, cdate)
        if onedata:
            data.append(onedata)
    data.reverse()
    return data


class JSumHandler(BaseHandler):
    # def get(self):
    #     cday = self.get_argument("cday", '0')
    #     crange = self.get_argument("range", "yes")
    #     if not cday.isdigit():
    #         return self.write(json.dumps({"error_code":1, "msg":"cday is str", "data": []}))
    #     cday = int(cday)
    #     if crange == "yes":
    #         data = getRangeUpDownInfo(self, cday)
    #         pass
    #     else:
    #         cdate = (datetime.now() - timedelta(days=cday)).strftime(DATE_FORMAT)
    #         data = getDailyUpDownInfo(self, cdate)
    #     return self.write(json.dumps({"error_code": 0, "msg": "", "data": data}))
    def gene_echart_data(self, data):
        sdate = []
        sup = []
        sdown = []
        max = 0
        if data is None:
            weblog.info("sum data is None.")
            return {"sdate": sdate, "sup": sup, "sdown": sdown, "smax": max, "curup": 0, "curdate": ""}
        for i in data:
            sdate.append(i[0])
            sup.append(round(i[2]/i[1], 2))
            sdown.append(round(i[3]/i[1], 2))
            # max = i[1] if i[1] > max else max
            max = 1
        curup = sup[-1] if len(sup) > 0 else 0
        curdate = sdate[-1] if len(sdate) > 0 else ""
        weblog.info("{} {} up:{} : curup:{} {}".format(len(sup), max, sup, curdate, curup))
        return {"sdate": sdate, "sup": sup, "sdown": sdown, "smax": max, "curup": curup * 100, "curdate": curdate}

    @check_token
    def get(self):
        pass
        # cdate = (datetime.now() - timedelta(days=30)).strftime(DATE_FORMAT)
        days = self.get_argument("days", '30')
        if days.isdigit():
            days = int(days)
        else:
            weblog.error("days: {}".format(days))
            days = 30
        data = getRangeUpDownInfo(self, days)
        return self.write(json.dumps({"error_code": 0, "msg": "", "data": self.gene_echart_data(data)}))


class SumShowHandler(BaseHandler):

    def get_updown(self):
        from database.tbl_sum import TblSum
        # nowdate = datetime.now().strftime("%Y-%m-%d")
        weekday = datetime.now().weekday()
        if weekday == 5:
            nowdate = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        elif weekday == 6:
            nowdate = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        else:
            nowdate = datetime.now().strftime("%Y-%m-%d")
        data = self.mysqldb().query(TblSum.jid, TblSum.jper).filter(TblSum.jdate == nowdate).order_by(TblSum.jper.desc()).all()
        up = 0
        down = 0
        jid = []
        jper = []
        for dt in data:
            jid.append(dt.jid)
            jper.append(dt.jper)
            if float(dt.jper) > 0: up += 1
            if float(dt.jper) < 0: down += 1
        return {"jids": jid, "jpers": jper, "up": up, "down": down}

    def gene_echart_data(self, data):
        sdate = []
        sup = []
        sdown = []
        max = 0
        if data is None:
            weblog.info("sum data is None.")
            return {"sdate": sdate, "sup": sup, "sdown": sdown, "smax": max, "curup": 0, "curdate": ""}
        for i in data:
            sdate.append(i[0])
            sup.append(round(i[2]/i[1], 2))
            sdown.append(round(i[3]/i[1], 2))
            # max = i[1] if i[1] > max else max
            max = 1
        curup = sup[-1] if len(sup) > 0 else 0
        curdate = sdate[-1] if len(sdate) > 0 else ""
        weblog.info("{} {} up:{} : curup:{} {}".format(len(sup), max, sup, curdate, curup))
        return {"sdate": sdate, "sup": sup, "sdown": sdown, "smax": max, "curup": curup * 100, "curdate": curdate}

    @check_authenticated
    # @check_only
    def get(self):
        pass
        # cdate = (datetime.now() - timedelta(days=30)).strftime(DATE_FORMAT)
        days = self.get_argument("days", '30')
        fmt = self.get_argument("format", "html")
        if days.isdigit():
            days = int(days)
        else:
            weblog.error("days: {}".format(days))
            days = 30
        data = getRangeUpDownInfo(self, days)
        if fmt == "json":
            return self.write(json.dumps({"data": self.gene_echart_data(data), "nowdata": self.get_updown()},
                                         indent=4, ensure_ascii=False))
        return self.render("sum.html", data=self.gene_echart_data(data), nowdata=self.get_updown())
