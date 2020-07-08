# coding=utf-8
"""
created: 12/13
"""
import os
from io import StringIO, BytesIO
import base64
from tornado.web import authenticated
from tornado.web import StaticFileHandler
from PIL import Image
import json
from handlers.basehd import BaseHandler, check_authenticated, check_token
from tornado.log import app_log as weblog
from common.global_func import get_user_info
import platform


class FsPlayHandler(BaseHandler):
    # @authenticated
    @check_authenticated
    def get(self, filename):
        realpath = os.path.join(self.settings.get('top_path'), filename)
        weblog.info("{} play".format(filename))
        if "\\" in realpath:
            realpath = realpath.replace("\\", '/')
        if os.path.exists(realpath):
            pass
            # print(realpath)
        else:
            return None

        suffix = realpath.split('.')[-1]
        width, height = (600, 600)
        # print(suffix)
        ftype = None
        imgs = None

        if suffix in ['mp4']:
            #print(realpath)
            return self.render("play.html", type=ftype, uri=filename, vsrc=realpath, iwidth=width, iheight=height)
            # return self.redirect(realpath)
        else:
            pass
            ftype = 'none'
        # print(ftype)
        if platform.system() == 'Windows':
            realpath = os.path.abspath(realpath)
        weblog.info("{} {} filename:".format(realpath, ftype, filename))
        return self.render("show.html", type=ftype, uri=filename, img=imgs, iwidth=width, iheight=height)


class AppPlayHandler(BaseHandler):

    @check_token
    def get(self, filename):
        realpath = os.path.join(self.settings.get('top_path'), filename)
        weblog.info("{} play".format(filename))
        if "\\" in realpath:
            realpath = realpath.replace("\\", '/')
        if os.path.exists(realpath):
            pass
        else:
            return self.write(json.dumps({"error_code": 1, "msg": u"视屏文件不存在"}))

        suffix = realpath.split('.')[-1]
        file_type = None
        if suffix in ['mp4']:
            file_type = 'video'
            return self.write(json.dumps({"vsrc": realpath, "error_code": 0, "type": file_type}))
        elif suffix in ['jpg', 'jpge', 'png']:
            file_type = 'image'
            return self.write(json.dumps({"vsrc": realpath, "error_code": 0, "type": file_type}))
        else:
            return self.write(json.dumps({"error_code": 1, "msg": u"不是视屏/图片文件"}))
        # # print(ftype)
        # if platform.system() == 'Windows':
        #     realpath = os.path.abspath(realpath)
        # weblog.info("{} {} filename:".format(realpath, ftype, filename))
        # # return self.render("show.html", type=ftype, uri=filename, img=imgs, iwidth=width, iheight=height)
        # return self.write(json.dumps({"img": imgs, "error_code": 0}))
