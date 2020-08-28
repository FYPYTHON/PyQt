#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 13:06
# @Author  : 1823218990@qq.com
# @File    : tbl_poetry.py
# @Software: PyCharm

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, BLOB, DATE, Text
from sqlalchemy.orm import deferred
from database import table_base
from database.db_config import ModelBase


class TblPoetry(ModelBase, table_base.TableBase):
    __tablename__ = 'tbl_poetry'
    id = Column(Integer, unique=True, primary_key=True)
    crt = Column(DateTime, default=datetime.now())
    category = Column(String(10), default=u"诗词")
    agg = Column(String(20), default=u"其他")
    poet = Column(String(10), nullable=False, default=u"佚名")
    title = Column(String(256), default=u"无题")
    content = deferred(Column(Text, nullable=False))
    describe = deferred(Column(Text, default=""))

    def __repr__(self):
        return "<poet=%s, title=%s>" % (self.poet, self.title)

    def tojson(self):
        content = self.content.replace("。", "。\n")
        if "(" in content or ")" in content:
            content = content.replace("(", "\n(")
            content = content.replace(")", ")\n")
        if "）" in content or "（" in content:
            content = content.replace("）", "）\n")
            content = content.replace("（", "\n（")
        content = content.strip('\n').split("\n")
        content = [c for c in content if c != ""]
        return {"category": self.category,
                "agg": self.agg,
                "poet": self.poet,
                "title": self.title,
                "content": content,
                "describe": self.describe.split("\n"),
                }
