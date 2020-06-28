# coding=utf-8
"""
created: 12/13
"""
import os
from tornado.web import authenticated
from handlers.basehd import BaseHandler, check_token, check_authenticated
from tornado.log import app_log as weblog
from common.global_func import get_user_info
import json
from urllib.parse import unquote, unquote_plus


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


class FSMainHandler(BaseHandler):

    # @authenticated
    @check_authenticated
    def get(self):
        curpath = self.get_argument("curpath", None)
        action = self.get_argument("action", None)
        # curpath = unquote_plus(curpath)
        if action is not None and action != "APP":
            curpath = os.path.dirname(curpath)
        # print("curpath:", curpath)
        userinfo = get_user_info(self)
        upload_path = self.settings.get('upload_path')
        if curpath is None or curpath == "" or curpath == "/":
            curpath = os.path.basename(upload_path)

        # if "\\" in curpath:
        #     curpath = curpath.replace("\\", "/")
        # print(userinfo)
        dir_list, file_list = get_paths(os.path.join(self.settings.get('top_path'), curpath))
        # print(curpath)
        self.render("fsmain.html", userinfo=userinfo, curpath=curpath, dirs=dir_list, files=file_list)

    @check_authenticated
    def post(self):
        pass

    def delete(self):
        pass


class AppFSMainHandler(BaseHandler):

    @check_token
    def get(self):
        curpath = self.get_argument("curpath", None)
        action = self.get_argument("action", None)
        # curpath = unquote_plus(curpath)
        if action is not None:
            curpath = os.path.dirname(curpath)
        # print("curpath:", curpath)

        userinfo = get_user_info(self)
        upload_path = self.settings.get('upload_path')
        if curpath is None or curpath == "" or curpath == "/":
            curpath = os.path.basename(upload_path)

        dir_list, file_list = get_paths(os.path.join(self.settings.get('top_path'), curpath))

        return self.write(json.dumps({"error_code": 0, "dirs": dir_list, "files": file_list, "userinfo": userinfo
                                      , "curpath": curpath}))
