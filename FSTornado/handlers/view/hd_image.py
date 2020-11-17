#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 13:09
# @Author  : 1823218990@qq.com
# @File    : hd_image.py
# @Software: PyCharm

from handlers.basehd import BaseHandler
import requests

from handlers.view.hd_jijin import get_gid_all_data, get_gid_range_data


class ShowImageHandler(BaseHandler):
    def get(self):
        # imgs = "data:image/{};base64,".format(suffix) + ims
        # xdata = range(1, 6)
        # ydata = range(11, 16)
        jid = self.get_argument("jid", None)
        jdata = get_gid_all_data(self, '1717')
        xdata = jdata.get("jdate")
        ydata = jdata.get("jvalue")
        print(xdata)
        print(ydata)
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
        return self.render("image.html", img=img, uri=uri)

    def tt(self):
        import matplotlib.pyplot as plt
        pass