#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 16:21
# @Author  : 1823218990@qq.com
# @File    : api_test2.py
# @Software: PyCharm

import requests

user = "a123456"
pwd = "123456"


def get_token(url):
    url = 'http://{}/login'.format(url)
    headers = {'User-Agent': "Mobile"}
    parmas = {"loginname": user, "userAccount": user, "password": pwd, "inputCode": "APP"}
    result = requests.post(url, data=parmas, headers=headers)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    # print(result.content)
    res = result.content.decode('utf-8')
    jres = eval(res)
    # fmtprint(jres)
    if "token" in jres:
        return jres.get("token")
    return result.text

def getVerifyImage(imgpath):
    pass
    from PIL import Image
    from io import BytesIO
    import base64
    # imgpath = "./tkcode.png"
    suffix = imgpath.split('.')[-1]
    if suffix == "jpg":
        suffix = "jpeg"
    img = Image.open(imgpath)
    output_buffer = BytesIO()
    img.save(output_buffer, format=suffix)
    binary_data = output_buffer.getvalue()
    base64_data = base64.b64encode(binary_data).decode()
    # data = {"imageFile": base64_data}
    #
    # res = requests.post(url, data=data)
    return base64_data, suffix


def add_all(url):
    import os
    import time
    root_dir = "/opt/data/public/cutpicture"
    files = os.listdir(root_dir)
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(root_dir, x)))
    files.reverse()
    print(len(files))
    for file in files:
        imgpath = os.path.join(root_dir, file)
        print(imgpath)
        add_word(url, imgpath)
        time.sleep(1)


def add_word(url, imgpath=None):
    import os
    if imgpath is None:
        imgpath = "E:/motorcycle_racing_摩托车比赛.gif"
    pictrue, suffix = getVerifyImage(imgpath)
    filename = os.path.basename(imgpath)
    temp = filename.split(".")[0].split("_")
    word = " ".join(temp[0: -1])
    chn = temp[-1]
    agg = u"常用"
    data = {"picture": pictrue,
            "word": word,
            "chn": chn,
            "suffix": suffix,
            "agg": agg,
            "describe": "",
            'token': get_token(url),
            'loginname': user}
    url = 'http://{}/word'.format(url)
    res = requests.post(url, data=data)
    print(word, res.text)


def get_code(url):
    headers = {'User-Agent': 'Mobile'}
    token = get_token(url)
    parmas = {'loginname': user, 'destr': '4K6h3JXgrLXgu43jkKPjiZnjjL3jlIvZr+Cpo+Ckt9uB',
              'token': token}
    url = 'http://{}/app/code'.format(url)
    res = requests.post(url, headers=headers, data=parmas).text
    print(res)

    p1 = {'loginname': user, 'enstr': '6*5=sqrt(30)',
              'token': token}
    res = requests.put(url, headers=headers, params=p1).text
    print(res)


def get_holiday():
    import json
    import requests
    date = "20201001"
    server_url = "http://api.goseek.cn/Tools/holiday?date="

    vop_response = requests.get(server_url + date)

    vop_data = vop_response.json()

    if vop_data[date] == '0':
        print("this day is weekday")
    elif vop_data[date] == '1':
        print('This day is weekend')
    elif vop_data[date] == '2':
        print('This day is holiday')
    else:
        print('Error')

def sendEmail(url):
    token = get_token(url)
    url = 'http://{}/sendmail'.format(url)
    headers = {'User-Agent': "Mobile"}
    parmas = {"loginname": user, "inputCode": "APP", "code": 1234, "token": token}
    result = requests.post(url, data=parmas, headers=headers)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    # print(result.content)
    res = result.content.decode('utf-8')
    print(res)
    jres = eval(res)
    # fmtprint(jres)
    # print(jres)
    return result.text

# -------------------------------------
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
ModelBase = declarative_base()


class TblAdmin(ModelBase):
    __tablename__ = 'tbl_admin'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(60), unique=True, comment=u"变量名")
    value = Column(String(60))
    type = Column(Integer)

    def __repr__(self):
        return "%s<id=%s, name=%s,value=%s>" % (self.__class__.__name__, self.id, self.name, self.value)



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

ModelBase = declarative_base()
engine = create_engine('mysql+pymysql://root:Faye0808@localhost:3306/faye_dream?charset=utf8', pool_size=100,
                       echo=False)
session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)

def add_data():
    from datetime import datetime
    from time import sleep
    aa = db_session.query(TblAdmin).all()
    for i in aa:
        print(i)

    for i in range(1000):
        t1 = TblAdmin()
        t1.name = str(datetime.now().timestamp())
        t1.value = str(datetime.now())
        t1.type = datetime.now().microsecond % 2
        # sleep(1)
        print(t1)
        db_session.add(t1)
        db_session.commit()


def add_code(url):
    headers = {'User-Agent': 'Mobile'}
    token = get_token(url)
    parmas = {'loginname': user, 'code': '1234', "msg": "测试", "key": "test",
              'token': token}
    url_p = 'http://{}/app/addcode'.format(url)
    res = requests.post(url_p, headers=headers, data=parmas).text
    print(res)

    p1 = {'loginname': user, 'enstr': '6*5=sqrt(30)',
          'token': token}
    res = requests.put("http://{}/app/code".format(url), headers=headers, params=p1).text
    print(res)

if __name__ == '__main__':
    url = "127.0.0.1:9080"
    url = "139.224.231.14:9016"
    # add_word(url)
    # add_all(url)
    # get_holiday()
    # sendEmail(url)
    # get_code(url)
    # add_data()
    add_code(url)