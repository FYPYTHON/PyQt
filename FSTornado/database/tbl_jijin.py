# coding=utf-8
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, BLOB, DATE
from database import table_base
from database.db_config import ModelBase


class TblJijin(ModelBase, table_base.TableBase):
    __tablename__ = 'tbl_jijin'

    id = Column(Integer, unique=True, primary_key=True)
    jid = Column(String(10), comment=u"jid")
    jvalue = Column(String(10))
    jdate = Column(String(15), default=datetime.now().strftime("%Y-%m-%d"))

    def __repr__(self):
        return "%s<jid=%s, jdate=%s,jvalue=%s>" % (self.__class__.__name__, self.jid, self.jdate, self.jvalue)

