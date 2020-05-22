# coding=utf-8
"""
created: 2020/05/06
"""
from tornado.web import authenticated
from tornado.log import app_log as weblog
from common.global_func import get_user_info, DATE_FORMAT
from handlers.basehd import BaseHandler
from database.tbl_jijin import TblJijin
from datetime import datetime, timedelta
from sqlalchemy import distinct
import json


class JiJinHandler(BaseHandler):
    pass

    # @authenticated
    def get(self):
        gid = self.get_argument("jid", None)
        weblog.info("{} gid: {}".format(self._request_summary(), gid))
        gids = self.get_gid()
        if gid is None:
            if len(gids) > 0:
                gid = gids[0]
            else:
                gid = None
        jdata = self.get_gid_all_data(gid)
        return self.render("view.html", jdata=jdata, jids=gids)

    def get_gid_all_data(self, jid):
        two_weeks_before = datetime.now() + timedelta(days=-14)
        str_date = two_weeks_before.strftime(DATE_FORMAT)
        result = self.mysqldb().query(TblJijin.jdate, TblJijin.jvalue).filter(TblJijin.jid == jid
                                                                              ,TblJijin.jdate >= str_date).order_by(
            TblJijin.jdate.asc()
        ).all()
        jdata = dict()
        jdate = []
        jvalue = []
        for res in result:
            jdate.append(res.jdate)
            jvalue.append(res.jvalue)
        jdata["jdate"] = jdate
        jdata["jvalue"] = jvalue
        jdata["jmax"] = max(jvalue)
        jdata["jmin"] = min(jvalue)
        return jdata

    @authenticated
    def post(self):
        jid = self.get_argument("jid")
        jdate = self.get_argument("jdate")
        jvalue = self.get_argument("jvalue")
        if not self.strtime_check(jdate):
            weblog.error("{} is error".format(jdate))
        isexit = self.mysqldb().query(TblJijin).filter(TblJijin.jid == jid, TblJijin.jdate == jdate).first()
        if isexit:
            isexit.value = jvalue
            try:
                self.mysqldb().commit()
                return self.write(json.dumps({"msg": "{}数据已存在,已更新".format(jdate), "error_code": 1}))
            except Exception as e:
                weblog.error("{}".format(e))
                return self.write(json.dumps({"msg": "{}数据已存在,更新失败".format(jdate), "error_code": 1}))
        tbl_jijin = TblJijin()
        tbl_jijin.jdate = jdate
        tbl_jijin.jid = jid
        tbl_jijin.jvalue = jvalue
        try:
            self.mysqldb().add(tbl_jijin)
            self.mysqldb().commit()
            return self.write(json.dumps({"msg": "jdata添加成功", "error_code": 0}))
        except Exception as e:
            weblog.error("{}".format(e))
            return self.write(json.dumps({"msg": "jdata添加失败", "error_code": 1}))

    def strtime_check(self, strtime):
        try:
            dtime = datetime.strptime(strtime, DATE_FORMAT)
            return True
        except Exception as e:
            weblog.error("{}".format(e))
            return False

    def get_gid(self):
        gids = self.mysqldb().query(distinct(TblJijin.jid)).all()
        idlist = []
        for gid in gids:
            idlist.append(gid[0])
        return idlist


#  58.240.217.252 ==
#  58.211.249.171 ==
