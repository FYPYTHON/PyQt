# coding=utf-8
"""
created: 02/17
"""
from tornado.web import authenticated
import time
from datetime import datetime
from database.tbl_account import TblAccount
from handlers.basehd import BaseHandler, check_authenticated, check_token
from json import dumps as json_dumps
from tornado.log import access_log as weblog
from method.data_encode import MD5
# from handlers.common_handler import get_expires_datetime
from common.global_func import get_expires_datetime, get_user_all, get_user_info
from common.msg_def import SESSION_ID, USER_IS_NONE, USER_OR_PASSWORD_ERROR, VER_CODE_ERROR


class ManageHandler(BaseHandler):
    # @authenticated
    @check_authenticated
    def get(self):
        curpath = self.get_argument('curpath', None)
        if curpath is None:
            curpath = 'public'
        # self.clear_cookie(SESSION_ID)
        # self.redirect('/login')
        userlist = get_user_all(self)
        userinfo = get_user_info(self)
        self.render("manage.html", users=userlist, userinfo=userinfo, curpath=curpath)

    # @authenticated
    @check_authenticated
    def post(self):
        loginname = self.get_argument("loginname", None)
        nickname = self.get_argument('nickname', None)
        password = self.get_argument('password', None)
        email = self.get_argument("email", None)
        userrole = self.get_argument("userrole", "2")

        if loginname is not None and nickname is not None and password is not None and email is not None:

            password = MD5(password)
            user = TblAccount()
            user.password = password
            user.loginname = loginname
            user.nickname = nickname
            user.email = email
            user.userrole = userrole
            user.userstate = 0
            self.mysqldb().add(user)
            try:
                self.mysqldb().commit()
                return self.write(json_dumps({"code": 0, "msg": u"添加成功"}))
            except Exception as e:
                self.mysqldb().rollbakc()
                weblog.error("{}".format(e))
        else:
            return self.write(json_dumps({"code": 1, "msg": u"添加失败"}))


class RestartHandler(BaseHandler):
    @check_token
    def post(self):
        cur_user = self.get_argument("loginname", None)
        self.restart(cur_user)

    @check_authenticated
    def get(self):
        if self.current_user:
            cur_user = self.current_user.decode('gbk')
        else:
            cur_user = None

        self.restart(cur_user)

    def restart(self, cur_user):
        user = self.mysqldb().query(TblAccount).filter(TblAccount.loginname == cur_user).first()
        TO_RESTART = False
        if user:
            if user.userrole == 0:
                TO_RESTART = True
        if TO_RESTART:
            import os
            res = os.system("bash /opt/midware/FSTornado/shell/restart.sh")
            if res == 0:
                return self.write(json_dumps({"error_code": 0, "msg": u"服务已重启"}))
            else:
                return self.write(json_dumps({"error_code": 1, "msg": u"服务重启失败"}))
        else:
            return self.write(json_dumps({"error_code": 1, "msg": u"没有操作权限"}))