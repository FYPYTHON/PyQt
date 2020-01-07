# coding=utf-8
"""
created: 12/13
"""
import os
from tornado.web import authenticated
from handlers.basehd import BaseHandler
from tornado.log import access_log as weblog
from common.global_func import get_user_info


class FSMainHandler(BaseHandler):

    @authenticated
    def get(self):
        curpath = self.get_argument("curpath", None)
        action = self.get_argument("action", None)
        if action is not None:
            curpath = os.path.dirname(curpath)
        # print("curpath:", curpath)
        weblog.info("%s ,main page. curpath: %s", self._request_summary(), curpath)
        userinfo = get_user_info(self)
        upload_path = self.settings.get('upload_path')
        if curpath is None or curpath == "" or curpath == "/":
            curpath = os.path.basename(upload_path)



        # if "\\" in curpath:
        #     curpath = curpath.replace("\\", "/")
        # print(userinfo)
        dir_list, file_list = self.get_paths(os.path.join(self.settings.get('top_path'), curpath))
        # print(curpath)
        self.render("fsmain.html", userinfo=userinfo, curpath=curpath, dirs=dir_list, files=file_list)

    def post(self):
        pass

    @staticmethod
    def get_paths(file_path):
        # file_path = os.path.join('/opt/data', file_path)
        if "\\" in file_path:
            curpath = file_path.replace("\\", "/")
        dir_list = list()
        file_list = list()
        if os.path.exists(file_path):
            content = os.listdir(file_path)
        else:
            content = list()
        for name in content:
            all_name = os.path.join(file_path, name)
            if os.path.isdir(all_name):
                if name not in dir_list:
                    dir_list.append(name)
            elif os.path.isfile(all_name):
                if name not in file_list:
                    file_list.append(name)

        dir_list.sort()
        file_list.sort()
        return dir_list, file_list

