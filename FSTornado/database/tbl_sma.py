#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 9:29
# @Author  : wangguoqiang@kedacom.com
# @File    : tbl_sma.py
# @Software: PyCharm


from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, BLOB, DATE, UniqueConstraint
from database import table_base
from database.db_config import ModelBase


class TblSma(ModelBase, table_base.TableBase):
    __tablename__ = 'tbl_sma'

    id = Column(Integer, unique=True, primary_key=True)
    jid = Column(String(10), comment=u"jid")
    wmin = Column(Integer, comment="window len")
    wmax = Column(Integer, comment="window len")
    model = Column(Integer, comment="save many sma win args ")
    __table_args__ = (
        UniqueConstraint('jid', 'model'),  # jid & model is unique
    )

    def __repr__(self):
        return "%s<jid=%s, model=%s, win=(%s,%s)>" % (self.__class__.__name__, self.jid, self.model, self.wmin, self.wmax)
