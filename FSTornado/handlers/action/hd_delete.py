#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 15:20
# @Author  : wangguoqiang@kedacom.com
# @File    : hd_delete.py.py
# @Software: PyCharm

import os
import json
from tornado.log import app_log as weblog
from handlers.basehd import BaseHandler, check_authenticated, check_token


class FsDeleteHandler(BaseHandler):
    @check_authenticated
    def delete(self):
        curpath = self.get_argument("curpath", None)
        filelist = self.get_arguments("filelist[]", False)  # super subor
        # print(self.request.arguments)
        # print(self.get_query_arguments("filelist"))
        for i in range(len(filelist)):
            file = filelist[i]
            real_file = os.path.join(self.settings.get("top_path"), file)
            filelist[i] = real_file
            if not os.path.exists(real_file):
                msg = u"{}不存在".format(file)
                return self.write(json.dumps({"error_code": 1, "msg": msg}))

        file_str = " ".join(filelist)
        try:
            cmd = "rm -rf {}".format(file_str)
            weblog.info("{}".format(cmd))
            os.system(cmd)
            return self.write(json.dumps({"error_code": 0, "msg": "文件已删除"}))
        except Exception as e:
            weblog.exception("{}".format(e))
            return self.write(json.dumps({"error_code": 1, "msg": u"删除失败"}))

    @check_token
    def post(self):
        pass