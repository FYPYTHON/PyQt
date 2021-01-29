#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 13:09
# @Author  : 1823218990@qq.com
# @File    : hd_image.py
# @Software: PyCharm

from handlers.basehd import BaseHandler, check_token
import requests
from datetime import datetime
from json import dumps as json_dumps
import os.path
from handlers.view.hd_jijin import get_gid_all_data, get_gid_range_data, get_gid


class ShowImageHandler(BaseHandler):
    def get(self):
        # imgs = "data:image/{};base64,".format(suffix) + ims
        # xdata = range(1, 6)
        # ydata = range(11, 16)
        jid = self.get_argument("jid", None)
        if jid is None: jid = '1717'
        savefile = "/opt/data/fs/{}_{}.png".format(jid, datetime.now().strftime("%Y-%m-%d"))
        if os.path.exists(savefile):
            # return self.write(json_dumps({"error_code": 0, 'img': open(savefile, 'r').read(), "jids": get_gid(self)}))
            with open(savefile, 'r') as f:
                img = f.read()
            return self.render("image.html", img=img, uri=savefile, jids=get_gid(self))

        jdata = get_gid_all_data(self, jid)
        xdata = jdata.get("jdate")
        ydata = jdata.get("jvalue")
        # print(xdata)
        # print(ydata)
        params = {"xdata": list(xdata), "ydata": list(ydata)}
        uri = "xy_{}.png".format(self.request.request_time())
        try:
            res = requests.get("http://127.0.0.1:9081/matimage", params=params)
            code = res.status_code
            data = res.json()
            img = data['img']
        except requests.exceptions.ConnectionError as e:
            # print(e)
            code = 404
            img = ""
        # print(res.content)
        if code != 404:
            img = "data:image/{};base64,".format('png') + img
        with open(savefile, 'w') as f:
            f.write(img)
        return self.render("image.html", img=img, uri=uri, jids=get_gid(self))

    def tt(self):
        import matplotlib.pyplot as plt
        pass


class AppImageHandler(BaseHandler):
    @check_token
    def get(self):
        # imgs = "data:image/{};base64,".format(suffix) + ims
        # xdata = range(1, 6)
        # ydata = range(11, 16)
        jid = self.get_argument("jid", None)
        if jid is None: jid = '1717'

        savefile = "/opt/data/fs/{}_{}.png".format(jid, datetime.now().strftime("%Y-%m-%d"))
        if os.path.exists(savefile):
            return self.write(json_dumps({"error_code": 0, 'img': open(savefile, 'r').read(), "jids": get_gid(self)}))

        jdata = get_gid_all_data(self, jid)
        xdata = jdata.get("jdate")
        ydata = jdata.get("jvalue")
        # print(xdata)
        # print(ydata)
        params = {"xdata": list(xdata), "ydata": list(ydata)}
        uri = "xy_{}.png".format(self.request.request_time())
        try:
            res = requests.get("http://127.0.0.1:9081/matimage", params=params)
            code = res.status_code
            data = res.json()
            img = data['img']
        except requests.exceptions.ConnectionError as e:
            # print(e)
            code = 404
            img = ""
        # print(res.content)
        if code != 404:
            img = "data:image/{};base64,".format('png') + img
        with open(savefile) as f:
            f.write(img)

        # return self.render("image.html", img=img, uri=uri, jids=get_gid(self))
        return self.write(json_dumps({"error_code": 0, 'img': img, "jids": get_gid(self)}))
