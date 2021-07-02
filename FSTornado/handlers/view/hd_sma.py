#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 17:05
# @Author  : wangguoqiang@kedacom.com
# @File    : hd_sma.py
# @Software: PyCharm

from tornado.log import app_log as weblog
from handlers.basehd import BaseHandler, check_only, check_authenticated
from database.tbl_jijin import TblJijin
from handlers.view.hd_jijin import get_gid
import json
import sys
sys.path.append("/opt/midware/sharelib/lib/python3.5/site-packages")


class SMAHandler(BaseHandler):
    @check_only
    @check_authenticated
    def get(self):
        # sec == dgj
        jid = self.get_argument("jid", "161725")
        if jid is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"未知错误"}))
        wmin = int(self.get_argument("wmin", "7"))  # 30
        wmax = int(self.get_argument("wmax", "30")) # 180
        weblog.info("args: {} {} {}".format(jid, wmin, wmax))
        d, v, s1, s2, pos = self.get_data(jid, wmin, wmax)
        jids = get_gid(self)
        return self.render("sma.html", data={"date": d, "value": v, "sma1": s1, "sma2": s2, "position": pos,
                                             "jid": jid}, jids=jids)
        # return self.write(json.dumps({"date": d, "value": v, "sma1": s1, "sma2": s2, "position": pos}))

    def get_data(self, jid, wmin, wmax):
        data = self.mysqldb().query(TblJijin.jdate, TblJijin.jvalue).filter(TblJijin.jid == jid).order_by(TblJijin.jdate.asc())
        count = data.count()
        weblog.info("data len:{}".format(count))
        data = data.all()
        jdates = []
        jvalues = []
        for item in data:
            jdates.append(item.jdate)
            jvalues.append(item.jvalue)
        try:
            from pandas import DataFrame, Series
            import numpy as np
        except Exception as e:
            weblog.error("{}".format(e))
            return [[] for _ in range(5)]
        s = Series(jvalues, index=jdates)
        pdd = DataFrame(s,
                           # index=jdates,
                           columns=["jj"]
                           )
        # weblog.info("{} {}".format(s, pdd))
        pdd['ori'] = pdd['jj']
        pdd['SMA1'] = pdd['jj'].rolling(window=wmin, min_periods=1).mean()
        pdd['SMA2'] = pdd['jj'].rolling(window=wmax, min_periods=1).mean()
        pdd['position'] = np.where(pdd['SMA1'] > pdd['SMA2'], 1, -1)
        return jdates, jvalues, pdd['SMA1'].tolist(), pdd['SMA2'].tolist(), pdd['position'].tolist()
