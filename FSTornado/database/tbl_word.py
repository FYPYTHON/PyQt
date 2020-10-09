#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 13:45
# @Author  : 1823218990@qq.com
# @File    : tbl_word.py
# @Software: PyCharm
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, BLOB, DATE, Text
from sqlalchemy.orm import deferred
from database import table_base
from database.db_config import ModelBase, db_session


class TblWord(ModelBase, table_base.TableBase):
    __tablename__ = 'tbl_word'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    word = Column(String(20), nullable=False, unique=True)
    chn = Column(String(20), default="")
    picture = deferred(Column(Text))
    suffix = Column(String(5), default="png")
    agg = Column(String(20), default=u"常用")
    describe = deferred(Column(Text))

    def __repr__(self):
        return "<word=%s, chn=%s>" % (self.word, self.chn)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def tojson(self):
        return {
            "id": self.id,
            "agg": self.agg,
            "suffix": self.suffix,
            "word": self.word,
            "chn": self.chn,
            "picture": self.picture,
            "describe": self.describe
        }


