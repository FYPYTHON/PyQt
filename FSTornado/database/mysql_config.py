#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 15:10
# @Author  : wangguoqiang@kedacom.com
# @File    : mysql_config.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, Text
from sqlalchemy.orm import sessionmaker, scoped_session, deferred
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import pymysql
pymysql.install_as_MySQLdb()

ModelBase = declarative_base()

host = "172.16.83.226"
port = 3306

# postgresql+psycopg2://user:password@hostname:port/database_name
engine = create_engine('mysql://root:fy123456@{}:{}/testonly?charset=utf8'.format(host, port), echo=True)
session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)

class TblAdmin(ModelBase):
    __tablename__ = 'tbl_admin_modb'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(60), unique=True, comment=u"变量名")
    value = Column(String(60))
    type = Column(Integer)

    def __repr__(self):
        return "%s<id=%s, name=%s,value=%s>" % (self.__class__.__name__, self.id, self.name, self.value)
ModelBase.metadata.create_all(engine)

def get_randstr(num):
    import random
    str = ''
    for i in range(num):
        str += random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
    return str

def add_data():
    from datetime import datetime
    for i in range(10):
        dd = TblAdmin()
        dd.name = get_randstr(10)
        dd.value = get_randstr(5)
        dd.type = i % 5
        db_session.add(dd)
        db_session.commit()

if __name__ == '__main__':
    add_data()

