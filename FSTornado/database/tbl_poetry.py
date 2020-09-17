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

    @property
    def raw_content_id(self):
        tids = [297]
        cids = [712, 713, 714, 715, 716, 717, 723, 725, 726, 727, 731, 736, 743, 744, 745, 746, 754, 755, 756, 759,
                760, 761, 762, 763, 770, 771, 772, 777, 778, 779, 781, 782, 783, 784]
        gids = [798, 799, 800, 801, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 818, 819,
            820, 823, 824, 825, 826, 831, 832, 833, 834, 835, 836, 837, 838, 846, 847, 848, 849, 850, 851,
            852, 853, 855, 856, 857, 859]
        return tids + cids + gids

    def tojson(self):
        if self.id in self.raw_content_id:
            content = self.content.split("\n")
        else:
            content = self.content.replace("。", "。\n")
            if "(" in content or ")" in content:
                content = content.replace("(", "\n(")
                content = content.replace(")", ")\n")
            if "）" in content or "（" in content:
                content = content.replace("）", "）\n")
                content = content.replace("（", "\n（")
            # if "？" in content:
            #     content = content.replace("？", "？\n")
            # if "！" in content:
            #     content = content.replace("！", "！\n")
            #
            # if "；" in content:
            #     content = content.replace("；", "；\n")

            content = content.strip('\n').split("\n")
            content = [c.strip(" ") for c in content if c != ""]
            content = self.replace_char(content)
            content = [c.strip('\u3000') for c in content if c != ""]

        describe = self.describe.split("\n")
        describe = [d if len(d) < 8 else "\t" + d for d in describe]
        return {"category": self.category,
                "agg": self.agg,
                "poet": self.poet,
                "title": self.title,
                "content": content,
                "describe": describe,
                "id": self.id
                }

    def replace_char(self, content):
        res = []
        for con in content:
            if con.startswith("（"):
                pass
            # print(con)
            elif "；" in con[8:]:
                con = con.replace("；", "；\n")
                # for con in contemp:
                #     pos = 8 + con[8:].index("；") + 1
                #     con = con[:pos] + '\n' + con[pos:]
                # if con.index("；") > 8:
                #     con = con.replace("；", "；\n")
            elif "？" in con[8:]:
                pos = 8 + con[8:].index("？") + 1
                con = con[:pos] + '\n' + con[pos:]
                # if con.index("？") > 8:
                #     con = con.replace("？", "？\n")
            elif "！" in con[8:]:
                pos = 8 + con[8:].index("！") + 1
                con = con[:pos] + '\n' + con[pos:]
                # if con.index("！") > 8:
                #     con = con.replace("！", "！\n")
            elif "：" in con[8:]:    # : before , then split content
                pos = 8 + con[8:].index("：") + 1
                con = con[:pos] + '\n' + con[pos:]
            elif "，" in con[10:]:
                pos = 10 + con[10:].index("，") + 1
                con = con[:pos] + '\n' + con[pos:]

            else:
                pass
            res.extend(con.split("\n"))
        return res

