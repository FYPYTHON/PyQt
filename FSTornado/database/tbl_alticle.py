#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 09:06
# @Author  : 1823218990@qq.com
# @File    : tbl_alticle.py
# @Software: PyCharm

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, BLOB, DATE, Text
from sqlalchemy.orm import deferred
from database import table_base
from database.db_config import ModelBase


class TblAlticle(ModelBase, table_base.TableBase):
    __tablename__ = 'tbl_alticle'
    id = Column(Integer, unique=True, primary_key=True)
    crt = Column(DateTime, default=datetime.now())
    category = Column(String(10), default=u"文章")
    agg = Column(String(20), default=u"其他")
    author = Column(String(10), nullable=False, default=u"佚名")
    title = Column(String(256), default=u"无题")
    content = deferred(Column(Text, nullable=False))
    describe = deferred(Column(Text, default=""))

    def __repr__(self):
        return "<author=%s, title=%s>" % (self.author, self.title)

    def tojson(self):

        content = self.content.strip('\n').split("\n")

        describe = self.describe.split("\n")

        return {"category": self.category,
                "agg": self.agg,
                "author": self.author,
                "title": self.title,
                "content": content,
                "describe": describe,
                "id": self.id
                }

    def initjson(self, params):
        self.category = params.get("category")
        self.agg = params.get("agg")
        self.author = params.get("author")
        self.title = params.get("title")
        self.content = params.get("content")
        self.describe = params.get("describe")



