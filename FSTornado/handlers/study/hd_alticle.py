#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 11:11
# @Author  : 1823218990@qq.com
# @File    : hd_alticle.py
# @Software: PyCharm


from handlers.basehd import BaseHandler, check_token, check_authenticated
from tornado.log import app_log as weblog
from handlers.author.hd_main import get_paths
from database.tbl_alticle import TblAlticle
import json


class AlticlesHandler(BaseHandler):
    def get(self):
        ftype = self.get_argument("type", None)
        agg = self.get_argument("agg", u"中华上下五千年")
        category = self.get_argument("category", u"文章")
        if ftype is None:
            return self.render("study.html")
            pass
        else:
            filelist = self.get_poems_list(agg, category)[0]
            agglist = self.get_agg_list()
            categorylist = self.get_category_list(agg)
            flen = int(ftype)
            return self.write(json.dumps({"filelist": filelist, "agglist": agglist,
                                          "categorylist": categorylist, "error_code": 0}))

    def get_poems_list(self, agg, category):
        res = self.mysqldb().query(TblAlticle.id, TblAlticle.category,
                                   TblAlticle.title).filter(TblAlticle.agg == agg, TblAlticle.category == category)
        count = res.count()
        res = res.all()
        poemsdict = list()
        for item in res:
            poemsdict.append([item.id, item.category, item.title])
        return poemsdict, count

    def get_agg_list(self):
        res = self.mysqldb().query(TblAlticle.id, TblAlticle.agg).group_by(TblAlticle.agg)
        res = res.all()
        agg = list()
        for item in res:
            agg.append(item.agg)
        return agg

    def get_category_list(self, agg):
        res = self.mysqldb().query(TblAlticle.id, TblAlticle.category).filter(TblAlticle.agg == agg
                                                                              ).group_by(TblAlticle.category)
        res = res.all()
        category = list()
        for item in res:
            category.append(item.category)
        return category


class AlticleHandler(BaseHandler):
    def get(self):
        pid = int(self.get_argument("pid", "-1"))
        alticle = self.mysqldb().query(TblAlticle).filter(TblAlticle.id == pid).first()
        if alticle is None:
            weblog.error("pid:{} not find".format(pid))
            return self.write(json.dumps({"error_code": 1, "msg": u"不存在", "alticle": ""}))
        else:
            return self.write(json.dumps({"alticle": alticle.tojson(), "error_code": 0}))
