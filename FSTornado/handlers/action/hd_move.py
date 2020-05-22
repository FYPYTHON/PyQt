# coding=utf-8
import os
import json
from shutil import move
from tornado.web import authenticated
from tornado.log import app_log as weblog
from handlers.basehd import BaseHandler
from handlers.author.hd_main import FSMainHandler


class FsMoveHandler(BaseHandler):
    @authenticated
    def get(self):
        curpath = self.get_argument("curpath", None)
        action = self.get_argument("action", None)  # super subor
        if curpath is not None:
            curpath = os.path.join(self.settings.get("top_path"), curpath)
            if os.path.exists(curpath):
                if os.path.isfile(curpath):
                    curpath = os.path.basename(curpath)
                dirlist = FSMainHandler.get_paths(curpath)[0]
                if action == "super":
                    curpath = os.path.basename(curpath)
                if len(dirlist) == 0:
                    dirlist.append(curpath)
                # else:
                #     dirlist = [os.path.join(curpath, dir).replace("\\", "/") for dir in dirlist]
                return self.write(json.dumps({"msg": "ok", "movepaths": dirlist, "code": 0}))

        return self.write(json.dumps({"msg": "get error", "code": 1}))



    @authenticated
    def post(self):
        oldname = self.get_argument("oldname", None)
        newname = self.get_argument("newname", None)
        curpath = self.get_argument("curpath", None)

        weblog.info("move {} {} {}".format(oldname, newname, curpath))
        toppath = self.settings.get("top_path")
        real_oldname = os.path.join(toppath, curpath, oldname)
        real_newname = os.path.join(toppath, curpath, newname)
        if not os.path.exists(real_oldname):
            return self.write(json.dumps({"msg": "orignal file or path is miss", "code": 1}))
        if not os.path.isdir(real_newname):
            return self.write(json.dumps({"msg": "move to path:{} is not exist".format(newname), "code": 1}))


        try:
            move(real_oldname, real_newname)
            return self.write(json.dumps({"msg": "ok", "code": 0}))
        except Exception as e:
            weblog.exception(e)
            return self.write(json.dumps({"msg": "move error", "code": 1}))