#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 11:40
# @Author  : 1823218990@qq.com
# @File    : tbl_word.py
# @Software: PyCharm
import time
import pytesseract
import os
import tornado.web
from PIL import Image

from common.global_func import get_action_word
from handlers.basehd import BaseHandler, check_token
from tornado.log import app_log as weblog
from database.tbl_word import TblWord
import json

from handlers.show.hd_play import get_img_base64


class PyTesseractHandler(tornado.web.RequestHandler):
    def get(self):
        # imgstr = self.get_argument("imgstr", "")
        imgstr = self.request.files['files'][0]
        size = self.get_argument("size", "(0,0)")
        mode = self.get_argument("mode", "P")
        weblog.info("{}".format(self.request.arguments))
        tempname = "/opt/temp/{}".format(str(time.time()) + imgstr['filename'])
        try:
            imgb = imgstr['body']
            size = eval(size)
            # mode = P RGB
            weblog.info("{} {} {}".format(size, len(imgb), tempname))
            # from io import BytesIO
            # imgb = BytesIO(imgb)
            # img = Image.frombytes(mode, size, f)
            with open(tempname, "wb") as f:
                f.write(imgb)
            img = Image.open(tempname)
            # # img.save("/opt/temp/test.gif", format='gif')
            result = pytesseract.image_to_string(img)
            if os.path.exists(tempname):
                os.system("rm -f {}".format(tempname))

            return self.write(json.dumps({"error_code": 0, "msg": result}))
        except Exception as e:
            if os.path.exists(tempname):
                os.system("rm -f {}".format(tempname))
            return self.write(json.dumps({"error_code": 1, "msg": "{}".format(e)}))


class WordHandler(BaseHandler):
    @check_token
    def get(self):
        wid = self.get_argument("wid", None)
        if wid == "-1":
            return self.write(json.dumps({"error_code": 0, "words": self.get_all_word()}))
        else:
            word = self.get_one_word(wid)
            if word is None:
                return self.write(json.dumps({"error_code": 1, "word": word, "msg": u"word id不存在"}))
            return self.write(json.dumps({"error_code": 0, "word": word}))
        pass

    def get_all_word(self):
        words = self.mysqldb().query(TblWord.id, TblWord.word, TblWord.chn).order_by(TblWord.id).all()
        datas = list()
        for word in words:
            datas.append(" ".join([str(word.id), word.word, word.chn]))

        return datas

    def get_one_word(self, wid):
        word = self.mysqldb().query(TblWord).filter(TblWord.id == wid).first()
        if word is None:
            return None
        else:
            return word.tojson()

    @check_token
    def post(self):
        word = self.get_argument("word", None)
        chn = self.get_argument("chn", None)
        agg = self.get_argument("agg", None)
        suffix = self.get_argument("suffix", None)
        picture = self.get_argument("picture", None)
        describe = self.get_argument("describe", "")
        tblword = self.mysqldb().query(TblWord).filter(TblWord.word == word).first()
        first_add = False
        if tblword is None:
            tblword = TblWord()
            first_add = True
        tblword.word = word
        tblword.chn = chn
        tblword.agg = agg
        tblword.suffix = suffix

        # base64Picture = get_img_base64(picture, suffix)
        tblword.picture = picture
        tblword.describe = describe
        if first_add:
            self.mysqldb().add(tblword)

        try:
            self.mysqldb().commit()
            return self.write(json.dumps({"error_code": 0, "msg": u"添加成功"}))
        except Exception as e:
            weblog.error("{}".format(e))
            return self.write(json.dumps({"error_code": 1, "msg": u"添加失败"}))

    @check_token
    def delete(self):
        wid = self.get_argument("wid")

        tblword = self.mysqldb().query(TblWord).filter(TblWord.id == wid).first()

        if tblword is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"word不存在，无法删除"}))
        else:
            self.mysqldb().query(TblWord).filter(TblWord.id == wid).delete()
            try:
                self.mysqldb().commit()
                return self.write(json.dumps({"error_code": 0, "msg": ""}))
            except Exception as e:
                weblog.error("{}".format(e))
                return self.write(json.dumps({"error_code": 1, "msg": u"删除失败"}))


class WordActionHandler(BaseHandler):
    @check_token
    def post(self):
        pid = int(self.get_argument("wid", "-1"))
        action = self.get_argument("action", None)

        if action is None:
            return self.write(json.dumps({"error_code": 1, "msg": u"参数错误", "word": ""}))

        word = get_action_word(self, TblWord, pid, action)
        if word is None:
            if word == "next":
                return self.write(json.dumps({"error_code": 1, "msg": u"最后一个词", "word": ""}))
            else:
                return self.write(json.dumps({"error_code": 1, "msg": u"第一个词", "word": ""}))
        else:
            return self.write(json.dumps({"word": word.tojson(), "error_code": 0}))