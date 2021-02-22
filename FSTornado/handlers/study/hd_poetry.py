#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 10:02
# @Author  : 1823218990@qq.com
# @File    : poetryhd.py
# @Software: PyCharm
from common.global_func import get_action_tbl
from handlers.basehd import BaseHandler, check_token, check_authenticated
from tornado.log import app_log as weblog
from handlers.author.hd_main import get_paths
from database.tbl_poetry import TblPoetry
import json


class PoetryHandler(BaseHandler):
    def get(self):
        ftype = self.get_argument("type", None)
        agg = self.get_argument("agg", u"唐诗三百首")
        if ftype is None:
            return self.render("study.html")
            pass
        else:
            filelist = self.get_poems_list(agg)[0]
            agglist = self.get_agg_list()
            flen = int(ftype)
            # filelist = [['-1', 2, 3], ["-1", 2, 3], ["-1", 5, 6]]
            # agglist = [1, 2, 3]
            return self.write(json.dumps({"filelist": filelist, "agglist": agglist, "error_code": 0}))

    def get_poems_list(self, agg):
        res = self.mysqldb().query(TblPoetry.id, TblPoetry.poet, TblPoetry.title).filter(TblPoetry.agg == agg)
        count = res.count()
        res = res.all()
        poemsdict = list()
        for item in res:
            poemsdict.append([item.id, item.poet, item.title])
        return poemsdict, count

    def get_agg_list(self):
        res = self.mysqldb().query(TblPoetry.id, TblPoetry.agg).group_by(TblPoetry.agg)
        res = res.all()
        agg = list()
        for item in res:
            agg.append(item.agg)
        return agg

    @check_token
    async def post(self):
        poet = self.get_argument("poet", None)
        title = self.get_argument("title", None)
        content = self.get_argument("content", None)
        category = self.get_argument("category", None)
        agg = self.get_argument("agg", None)
        describe = self.get_argument("describe", None)
        if not (poet and title and content and category and agg):
            return self.write(json.dumps({"error_code": 1, "msg": u"参数错误"}))
        exist_poem = self.mysqldb().query(TblPoetry).filter(TblPoetry.title == title, TblPoetry.poet == poet,
                                                            TblPoetry.agg == agg).first()
        if exist_poem is not None:
            # manual update
            if exist_poem.content != content:
                exist_poem.content = content
                try:
                    self.mysqldb().commit()
                    return self.write(json.dumps({"error_code": 0, "msg": u"更新成功"}))
                except Exception as e:
                    weblog.error("{}".format(e))
                    return self.write(json.dumps({"error_code": 1, "msg": u"更新失败"}))
            else:
                return self.write(json.dumps({"error_code": 1, "msg": u"已存在: {} {}".format(poet, title)}))

        poemtry = TblPoetry()
        poemtry.title = title
        poemtry.poet = poet
        poemtry.content = content
        poemtry.category = category
        poemtry.agg = agg
        poemtry.describe = describe
        try:
            self.mysqldb().add(poemtry)
            self.mysqldb().commit()
            return self.write(json.dumps({"error_code": 0, "msg": u"添加成功"}))
        except Exception as e:
            weblog.error("{}".format(e))
            return self.write(json.dumps({"error_code": 1, "msg": u"添加失败"}))

    @check_token
    def delete(self):
        poe_id = int(self.get_argument("pid", "-1"))
        if poe_id is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"参数错误"}))

        try:
            self.mysqldb().query(TblPoetry).filter(TblPoetry.id == poe_id).delete()
            self.mysqldb().commit()
            return self.write(json.dumps({"error_code": 0, "msg": u"删除成功"}))
        except Exception as e:
            weblog.error("{}".format(e))
            return self.write(json.dumps({"error_code": 1, "msg": u"删除失败"}))

    @check_token
    def put(self):
        poet = self.get_argument("poet", None)
        title = self.get_argument("title", None)
        content = self.get_argument("content", None)
        category = self.get_argument("category", None)
        agg = self.get_argument("agg", None)
        describe = self.get_argument("describe", None)
        if not (poet and title and content and category and agg):
            return self.write(json.dumps({"error_code": 1, "msg": u"参数错误"}))
        exist_poem = self.mysqldb().query(TblPoetry).filter(TblPoetry.title == title, TblPoetry.poet == poet,
                                                            TblPoetry.agg == agg).first()
        if exist_poem is not None:
            # manual update
            weblog.info("poem id: {}".format(exist_poem.id))
            # print(exist_poem.id)
            if exist_poem.describe != describe:
                exist_poem.describe = describe
                try:
                    self.mysqldb().commit()
                    return self.write(json.dumps({"error_code": 0, "msg": u"更新成功"}))
                except Exception as e:
                    weblog.error("{}".format(e))
                    return self.write(json.dumps({"error_code": 1, "msg": u"更新失败"}))
            else:
                return self.write(json.dumps({"error_code": 1, "msg": u"已存在: {} {}".format(poet, title)}))
        else:
            return self.write(json.dumps({"error_code": 1, "msg": u"不存在: {} {}".format(poet, title)}))


class PoemHandler(BaseHandler):
    def get(self):
        pid = int(self.get_argument("pid", "-1"))
        poem = self.mysqldb().query(TblPoetry).filter(TblPoetry.id == pid).first()
        # print(poem)
        if poem is None:
            weblog.error("pid:{} not find".format(pid))
            return self.write(json.dumps({"error_code": 1, "msg": u"不存在", "poem": ""}))
        else:
            return self.write(json.dumps({"poem": poem.tojson(), "error_code": 0}))

    @check_token
    def put(self):
        pid = int(self.get_argument("pid", "-1"))
        content = self.get_argument("content", None)
        category = self.get_argument("category", None)
        agg = self.get_argument("agg", None)
        describe = self.get_argument("describe", None)
        exist_poem = self.mysqldb().query(TblPoetry).filter(TblPoetry.id == pid).first()
        if exist_poem is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"不存在 pid:{}".format(pid)}))
        if content is not None:
            exist_poem.content = content
        if category is not None:
            exist_poem.category = category
        if agg is not None:
            exist_poem.agg = agg
        if describe is not None:
            exist_poem.describe = describe

        try:
            self.mysqldb().commit()
            return self.write(json.dumps({"error_code": 0, "msg": u"更新成功"}))
        except Exception as e:
            weblog.error("{}".format(e))
            return self.write(json.dumps({"error_code": 1, "msg": u"更新失败"}))

    @check_token
    def post(self):
        pid = int(self.get_argument("pid", "-1"))
        action = self.get_argument("action", None)

        if action is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"参数错误", "poem": ""}))

        poem = get_action_tbl(self, TblPoetry, pid, action)

        if poem is None:
            if poem == "next":
                return self.write(json.dumps({"error_code": 1, "msg": u"最后一篇", "poem": ""}))
            else:
                return self.write(json.dumps({"error_code": 1, "msg": u"第一篇", "poem": ""}))
        else:
            return self.write(json.dumps({"poem": poem.tojson(), "error_code": 0}))


class PoemLikeHandler(BaseHandler):
    """
    like  %key%
    """
    # @check_authenticated
    def get(self):
        key = self.get_argument("key", None)
        keys = self.get_arguments("keys[]", strip=True)
        weblog.info("key:{}, keys:{}".format(key, keys))
        if key is not None:
            keyword = "%{}%".format(key)
        else:
            keyword = None
        res = self.mysqldb().query(TblPoetry.id, TblPoetry.poet, TblPoetry.title, TblPoetry.content)
        if keys:
            pass
            for ks in keys:
                ks = "%{}%".format(ks)
                res = res.filter(TblPoetry.content.like(ks))
        else:
            res = res.filter(TblPoetry.content.like(keyword))
        count = res.count()
        res = res.all()
        resp = []
        for poem in res:
            single = []
            # single.append(poem.id)
            single.append(poem.poet)
            single.append(poem.title)
            if not keys:
                ctt = [item for item in poem.content.split("。") if key in item]
                single.append(ctt)
                if single not in resp:
                    resp.append(single)
            else:
                ctt = list()
                for item in poem.content.split("。"):
                    islikes = True

                    for ks in keys:
                        if ks not in item:
                            islikes = False
                            break
                    if islikes:
                        ctt.append(item)
                if ctt:
                    single.append(ctt)
                    if single not in resp:
                        resp.append(single)
        weblog.info("{} {}".format(resp, count))
        return self.write(json.dumps({"error_code": 0, "poemlike": resp, "count": len(resp)}))
