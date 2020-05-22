# coding=utf-8
import hashlib

from database.db_config import db_session
from method.data_encode import MD5
def init_admin():
    from database.tbl_admin import TblAdmin
    user = TblAdmin()
    user.name = "__MAIL__"
    user.value = "1490726887@qq.com"
    user.type = 1
    db_session.add(user)
    db_session.commit()
    db_session.close()

def init_user():
    from database.tbl_account import TblAccount
    account = TblAccount()
    account.loginname = "youth303"
    account.nickname = u"青春"
    account.password = MD5("303303")
    account.email = ""
    account.userstate = 0
    account.userrole = 2
    db_session.add(account)
    db_session.commit()
    db_session.close()

def init_setting():
    from database.tbl_admin import TblAdmin
    db_session.add_all([
    TblAdmin(name="currentname",value="feiying",type=0),
    TblAdmin(name="description",value="test only",type=0),
    TblAdmin(name="admin_email", value="1490726887@qq.com", type=0),
    TblAdmin(name="can_register", value="1", type=1),
    TblAdmin(name="can_comment", value="1", type=1),
    TblAdmin(name="comments_notify", value="1", type=1),
    TblAdmin(name="default_category", value="default_category", type=0),
    TblAdmin(name="page_size", value="10", type=1),
    TblAdmin(name="rss_size", value="10", type=1),
    TblAdmin(name="rss_excerpt", value="1", type=1),
    TblAdmin(name="new_rss_size", value="5", type=1),
    TblAdmin(name="new_page_size", value="5", type=1),
    ])

    db_session.commit()



if __name__ == "__main__":
    # init_admin()
    # init_user()
    # init_setting()
    from database.tbl_jijin import TblJijin
    from datetime import datetime
    dis = TblJijin()
    dis.jid = "test2"
    dis.jdate = '2020-05-05'
    dis.jvalue = '2.13'
    db_session.add(dis)
    db_session.commit()
