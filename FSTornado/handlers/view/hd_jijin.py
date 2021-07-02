# coding=utf-8
"""
created: 2020/05/06
"""
from tornado.web import authenticated
from tornado.log import app_log as weblog
from common.global_func import get_user_info, DATE_FORMAT
from common.common_base import DatetimeManage
from common.msg_def import WEEK_DAY
from handlers.basehd import BaseHandler, check_token, check_authenticated, check_role
from database.tbl_jijin import TblJijin
from datetime import datetime, timedelta
from sqlalchemy import distinct
import json


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


def get_date_week(jdate):
    try:
        dt = datetime.strptime(jdate, "%Y-%m-%d")
        wk = dt.weekday()
        date_week = "{} {}".format(jdate[5:], WEEK_DAY[wk])
        return date_week
    except Exception as e:
        weblog.error("{}".format(e))
        return jdate


def get_gid_all_data(self, jid, dayrange=-30):
    two_weeks_before = datetime.now() + timedelta(days=dayrange)
    str_date = two_weeks_before.strftime(DATE_FORMAT)
    result = self.mysqldb().query(TblJijin.jdate, TblJijin.jvalue).filter(TblJijin.jid == jid
                                                                          , TblJijin.jdate >= str_date).order_by(
        TblJijin.jdate.asc()
    ).all()
    jdata = dict()
    jdate = []
    jvalue = []
    for res in result:
        jdate.append(get_date_week(res.jdate))
        jvalue.append(res.jvalue)
    jdata["jdate"] = jdate
    jdata["jvalue"] = jvalue
    jdata["jmax"] = max(jvalue) if jvalue else 0
    jdata["jmin"] = min(jvalue) if jvalue else 0
    return jdata


def get_gid_range_data(self, jid, weeks_ago):
    monday, sunday = DatetimeManage.get_current_week(weeks_ago, True)
    result = self.mysqldb().query(TblJijin.jdate, TblJijin.jvalue).filter(TblJijin.jid == jid
                                                                          , TblJijin.jdate >= monday
                                                                          , TblJijin.jdate <= sunday).order_by(
        TblJijin.jdate.asc()
    ).all()
    jdata = dict()
    jdate = []
    jvalue = []
    for res in result:
        jdate.append(get_date_week(res.jdate))
        jvalue.append(res.jvalue)
    jdata["jdate"] = jdate
    jdata["jvalue"] = jvalue
    jdata["jmax"] = max(jvalue) if jvalue else 0
    jdata["jmin"] = min(jvalue) if jvalue else 0
    jdata["monday"] = monday
    jdata["sunday"] = sunday
    return jdata


class JiJinHandler(BaseHandler):

    # @authenticated
    @check_authenticated
    def get(self):
        gid = self.get_argument("jid", None)
        dayrange = self.get_argument("dayrange", "30")
        try:
            dayrange = -int(dayrange)
        except:
            dayrange = -30
        gids = get_gid(self)
        if gid is None:
            if len(gids) > 0:
                gid = gids[0]
            else:
                gid = None
        jdata = get_gid_all_data(self, gid, dayrange)
        current_week_data = get_gid_range_data(self, gid, 0)
        last_week_data = get_gid_range_data(self, gid, 1)
        return self.render("view.html", jdata=jdata, jids=gids, jid=gid, jdata0=current_week_data, jdata1=last_week_data)

    # @authenticated
    @check_authenticated
    @check_role
    def post(self):
        jid = self.get_argument("jid")
        jdate = self.get_argument("jdate")
        jvalue = self.get_argument("jvalue")
        if not strtime_check(self, jdate):
            weblog.error("{} is error".format(jdate))
        if jid == "" or jid is None:
            return self.write(json.dumps({"msg": "参数错误", "error_code": 1}))
        isexit = self.mysqldb().query(TblJijin).filter(TblJijin.jid == jid, TblJijin.jdate == jdate).first()
        if isexit:
            isexit.jvalue = jvalue
            try:
                self.mysqldb().commit()
                return self.write(json.dumps({"msg": "{}数据已存在,已更新".format(jdate), "error_code": 0}))
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


class AppJiJinHandler(BaseHandler):
    @check_token
    def get(self):
        gid = self.get_argument("jid", None)
        dayrange = self.get_argument("dayrange", "60")
        try:
            dayrange = -int(dayrange)
        except:
            dayrange = -30

        gids = get_gid(self)
        if gid is None:
            if len(gids) > 0:
                gid = gids[0]
            else:
                gid = None
        jdata = get_gid_all_data(self, gid, dayrange=dayrange)
        current_week_data = get_gid_range_data(self, gid, 0)
        last_week_data = get_gid_range_data(self, gid, 1)
        last_twoweek_data = get_gid_range_data(self, gid, 2)
        # return self.render("view.html", jdata=jdata, jids=gids)
        return self.write(json.dumps({"error_code": 0, "msg": "ok", "jdata": jdata, "jids": gids, "jid": gid
                                , "jdata0": current_week_data, "jdata1": last_week_data, "jdata2": last_twoweek_data}))

    @check_token
    def post(self):
        jid = self.get_argument("jid")
        jdate = self.get_argument("jdate")
        jvalue = self.get_argument("jvalue")

        if not strtime_check(self, jdate):
            weblog.error("{} is error".format(jdate))
        isexit = self.mysqldb().query(TblJijin).filter(TblJijin.jid == jid, TblJijin.jdate == jdate).first()
        if isexit:
            isexit.jvalue = jvalue
            try:
                self.mysqldb().commit()
                return self.write(json.dumps({"msg": "{}数据已存在,已更新".format(jdate), "error_code": 0}))
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

    @check_token
    def delete(self):
        jid = self.get_argument("jid", None)
        if jid is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"参数错误"}))
        try:
            self.mysqldb().query(TblJijin).filter(TblJijin.jid == jid).delete()
            self.mysqldb().commit()
            return self.write(json.dumps({"error_code": 0, "msg": u"删除成功"}))
        except Exception as e:
            weblog.error("{}".format(e))
            return self.write(json.dumps({"error_code": 1, "msg": u"删除失败"}))
