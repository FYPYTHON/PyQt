#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 15:53
# @Author  : 1823218990@qq.com
# @File    : tbl_sum.py
# @Software: PyCharm
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, BLOB, DATE
from database import table_base
from database.db_config import ModelBase


class TblSum(ModelBase, table_base.TableBase):
    __tablename__ = 'tbl_sum'

    id = Column(Integer, unique=True, primary_key=True)
    jid = Column(String(10), comment=u"jid")
    jdate = Column(String(15), default=datetime.now().strftime("%Y-%m-%d"))
    jinc = Column(Integer, comment="0,1=up,-1=down")
    jper = Column(String(15), default="--", comment="%")

    def __repr__(self):
        return "%s<jid=%s, jdate=%s,jper=%s>" % (self.__class__.__name__, self.jid, self.jdate, self.jper)

