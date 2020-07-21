#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 13:37
# @Author  : wangguoqiang@kedacom.com
# @File    : hd_history.py
# @Software: PyCharm

import os
from io import StringIO, BytesIO
import base64
from tornado.web import authenticated
from PIL import Image
from urllib import parse
import json

from handlers.author.hd_main import get_disk_usage
from handlers.basehd import BaseHandler, check_authenticated
from tornado.log import app_log as weblog
from common.global_func import get_user_info, get_history_all
import platform


class HistoryHandler(BaseHandler):
    def get(self):
        curpath = self.get_argument('curpath', None)
        if curpath is None:
            curpath = 'public'
        historylist = get_history_all(self)
        userinfo = get_user_info(self)
        self.render("history.html", historys=historylist, userinfo=userinfo, curpath=curpath,
                    useage=get_disk_usage(self, curpath))
