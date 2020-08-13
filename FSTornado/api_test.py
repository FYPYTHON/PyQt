#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 17:19
# @Author  : wangguoqiang@kedacom.com
# @File    : api_test.py
# @Software: PyCharm

import requests


def get_token(url):
    url = 'http://{}/login'.format(url)
    headers = {'User-Agent': "Mobile"}
    parmas = {"loginname": "test123","userAccount": "Tornado", "password": "123123", "inputCode": "APP"}
    result = requests.post(url, data=parmas, headers=headers)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    print(result.content)
    res = result.content.decode('utf-8')
    jres = eval(res)
    fmtprint(jres)
    if "token" in jres.keys():
        return jres.get("token")
    return result.text


# TOKEN = get_token()



def fmtprint(jres):
    import json
    try:
        jres = eval(jres)
    except:
        pass
    jsonf = json.dumps(jres, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    # jsone = json.dumps(jres, sort_keys=True, indent=4, separators=(',', ':'))
    print(jsonf)
    # print(jsone)


def db():
    # coding=utf-8
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    from sqlalchemy.ext.declarative import declarative_base
    import pymysql
    pymysql.install_as_MySQLdb()

    ModelBase = declarative_base()
    engine = create_engine('sqlite:///D:\\workSpace\\go\\study\\src\\wfs.db?check_same_thread=False', echo=True)
    session_factory = sessionmaker(bind=engine)
    db_session = scoped_session(session_factory)
    return db_session

def post_ava():
    file_name = "E:\\tk_color.png"
    url = 'http://139.224.231.14:9016/avator'
    f = open(file_name, 'rb')
    import os
    filesize = os.path.getsize(file_name)

    parmas = {"avator_path": filesize, "loginname": "Tornado", "token": TOKEN}
    headers = {'filesize': str(filesize), 'User-Agent': "Mobile"}
    result = requests.post(url, headers=headers, files={"files": f}, data=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.decode('utf-8')
    jres = eval(res)
    print(jres)
    return result.text


def post_next():
    url = 'http://139.224.231.14:9016/app/play/next'
    parmas = {"action": "next", "curpath": "public/Yuyuan/image", "token": TOKEN, "loginname": "Tornado",
              "ftype": "image", "index": 11}
    headers = {'User-Agent': "Mobile"}
    result = requests.post(url, headers=headers, data=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.decode('utf-8')
    jres = eval(res)
    print(jres.keys())
    if "msg" in jres.keys():
        if jres.get("error_code") == 0:
            print(jres.get("msg"))
            print(jres.get("nowfile"))
            print(len(jres.get("img")))
        else:
            print(jres)
    return result.text


def get_version(url):
    url = 'http://{}/app/version'.format(url)

    parmas = {"loginname": "Tornado", "token": TOKEN}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.replace(b"null",b"None").decode('utf-8')
    jres = eval(res)
    fmtprint(jres)
    return result.text


def get_version_(url):
    url = 'http://{}/appversion'.format(url)

    parmas = {"loginname": "Tornado", "token": "90bd3769d4f627ce99fbcddd4b72408b"}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    print(result.text)
    res = result.content.replace(b"null",b"None").decode('utf-8')
    jres = eval(res)
    fmtprint(jres)
    return result.text



def put_version():
    url = 'http://139.224.231.14:9016/appversion'

    parmas = {"loginname": "Tornado", "token": TOKEN, "version": "1.0.2"}
    headers = {'User-Agent': "Mobile"}
    result = requests.put(url, headers=headers, data=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.decode('utf-8')
    jres = eval(res)
    print(jres)
    return result.text


def get_userinfo():
    url = 'http://139.224.231.14:9016/appuserinfo'

    parmas = {"loginname": "Tornado", "token": TOKEN}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.decode('utf-8')
    jres = eval(res)
    print(jres)
    return result.text

def img_resize():
    from io import BytesIO
    from PIL import Image
    import base64
    import os
    import time
    t1 = time.time()
    realpath = "E:\\IMG_20190503_123846.jpg"
    # realpath = "D:\\workSpace\\rother\\yuyuan\\app\\src\\main\\res\\drawable\\filedialog_file.png"
    # realpath = "E:\\tk_color.png"
    small_size = (30, 30)
    img = Image.open(realpath)
    img.thumbnail(small_size)
    t2 = time.time()
    print("t2:", t2 - t1)
    suffix = realpath.split('.')[-1]
    if suffix == "jpg":
        suffix = "jpeg"
    print("image size: {} {}".format(img.size, os.path.getsize(realpath)))
    img_size = os.path.getsize(realpath)
    beishu = img_size / 1024 / 1024
    print("beisu", beishu)
    t3 = time.time()
    print("t3:", t3 - t2)
    if beishu >= 2:
        small_size = (int(img.size[0] / beishu), int(img.size[0] / beishu))
    else:
        small_size = img.size
    small_size = (int(img.size[0]/1.1), int(img.size[0]/1.1))

    # img = img.resize(small_size, Image.ANTIALIAS)
    t4 = time.time()
    print("t4:", t4 - t3)
    output_buffer = BytesIO()
    img.save(output_buffer, format=suffix)
    print("temp:", time.time() - t4)
    print("image size: {} {}".format(img.size, os.path.getsize(realpath)))
    binary_data = output_buffer.getvalue()
    base64_data = base64.b64encode(binary_data).decode()
    t5 = time.time()
    print("t5:", t5 - t4)
    # print(base64_data)
    # 821824 - 178244
    # import zlib
    # zipdata = zlib.compress(base64_data.encode())
    # print(len(base64_data), type(base64_data))
    # print("zip:", len(zipdata), len(zipdata) / len(base64_data))

    # img.save("E:\\test.jpg")


def get_videoshortcut_base64(realpath, suffix):
    realpath = "E:\\file\\Desktop\\test.mp4"
    import cv2
    cap = cv2.VideoCapture(realpath)
    ret, frame = cap.read()
    cap.release()
    print(ret, frame)
    print(type(frame))
    from PIL import Image
    from io import BytesIO
    import os
    import base64
    img = Image.fromarray(frame)
    if ret:
        # cv2.imwrite("E:\\test1.jpg", frame)
        img = img.resize((20, 20), Image.ANTIALIAS)
        output_buffer = BytesIO()
        img.save(output_buffer, format="jpeg")
        print("image size: {} {}".format(img.size, os.path.getsize(realpath)))
        binary_data = output_buffer.getvalue()
        base64_data = base64.b64encode(binary_data).decode()
        print("len:", len(base64_data))
        img.save("E:\\test2.jpg")


def get_fsmain(url="139.224.231.14:9016"):
    url = 'http://{}/app/fsmain'.format(url)

    parmas = {"loginname": "Tornado", "token": TOKEN, "curpath": "public/File", "action": "super"}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.content)
    res = result.content
    res = res.decode('utf-8')
    jres = eval(res)
    print(jres)
    return result.text


def get_users(url="139.224.231.14:9016"):
    url = 'http://{}/app/user'.format(url)

    parmas = {"loginname": "Tornado", "token": TOKEN, "curpath": "public/File", "action": "super",
              "email":"test1@qq.com", "password": "1234", "nickname": "修改"}

    headers = {'User-Agent': "Mobile"}

    result = requests.get(url + "/1", headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, data=parmas)
    # result = requests.delete(url + "/1", headers=headers)
    # result = requests.put(url + "/3", headers=headers, data=parmas)
    # print(result.content)
    res = result.content
    res = res.decode('utf-8')
    fmtprint(res)
    return result.text


def get_userlist(url="139.224.231.14:9016"):
    url = 'http://{}/app/userlist'.format(url)

    parmas = {"loginname": "Tornado", "token": TOKEN, "page": 1, "limit": 10}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    print(result.content)
    res = result.content
    res = res.decode('utf-8')
    jres = eval(res)
    print(jres)
    return result.text

def post_value(url):
    url = 'http://{}/app/view'.format(url)
    parmas = {"jid": "1717", "jdate": "2020-08-10", "jvalue": "3.7110", "token": TOKEN, "loginname": "Tornado"}
    headers = {'User-Agent': "Mobile"}
    result = requests.post(url, headers=headers, data=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.decode('utf-8')
    fmtprint(res)
    return result.text


def get_value(url):
    url = 'http://{}/app/view'.format(url)
    parmas = {"jid": "1717", "token": TOKEN, "loginname": "Tornado", "all": "all"}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.replace(b"null", b"None").decode('utf-8')
    jres = eval(res)
    fmtprint(jres)
    return result.text


def post_dir(url="139.224.231.14:9016"):
    url = 'http://{}/app/dir'.format(url)
    parmas = {"newname": "123.png", "curpath": "public/Extra","token": TOKEN, "loginname": "Tornado",
              "filename": "vv", "oldname": "1.txt"}
    headers = {'User-Agent': "Mobile"}
    # result = requests.post(url, headers=headers, data=parmas)
    # result = requests.delete(url + "?filename=%s&curpath=%s" % (parmas.get('filename'), parmas.get("curpath")), headers=headers)
    result = requests.put(url, headers=headers, data=parmas)
    print(result.text)
    res = result.content.decode('utf-8')
    jres = eval(res)
    if "msg" in jres.keys():
        print(jres)
    return result.text


def play(url):
    url = 'http://{}/app/play'.format(url)
    parmas = {"newname": "123.png", "curpath": "public/Cugb/2017", "token": TOKEN, "loginname": "test123",
              "filename": "127.jpg", "oldname": "IMG_20190503_123846.jpg", "index": 1, "ftype": "image",
              "action": "previous"}
    headers = {'User-Agent': "Mobile"}
    print(url)
    # result = requests.get(url + "/" + parmas.get("filename"), headers=headers, params=parmas)
    result = requests.post(url + "/" + parmas.get("filename"), headers=headers, data=parmas)
    # result = requests.delete(url + "?filename=%s&curpath=%s" % (parmas.get('filename'), parmas.get("curpath")), headers=headers)
    # result = requests.put(url, headers=headers, data=parmas)
    # print(result.text)
    res = result.content.decode('utf-8')
    fmtprint(res)
    return result.text


def view(url):
    url = 'http://{}/app/view'.format(url)
    parmas = {"curpath": "public/Extra", "token": TOKEN, "loginname": "test123",
              "page": 1, "jid": "1717", "all": "all2"}
    # parmas = {}
    headers = {'User-Agent': "Mobile"}
    print(url)
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, data=parmas)
    # result = requests.delete(url + "?filename=%s&curpath=%s" % (parmas.get('filename'), parmas.get("curpath")), headers=headers)
    # result = requests.put(url, headers=headers, data=parmas)
    # print(result.content)

    res = result.content.replace(b"null", b"None").decode('utf-8')
    jres = eval(res)
    fmtprint(jres)
    return result.text


def post_upload(url):
    # requests.post(url, data=params, files={"file": f})
    from urllib import parse
    file_name = "E:\\file\\gcc.exe"
    url = 'http://{}/app/upload'.format(url)
    f = open(file_name, 'rb')
    import os
    filesize = os.path.getsize(file_name)

    params = {"curpath": "public/File", "loginname": "Tornado", "token": TOKEN}

    headers = {'User-Agent': "Mobile", 'filesize': str(filesize)}
    # fl = open('test.png', 'rb')
    # files = {'files': ('test.png', fl, 'application/octet-stream', {'Expires': '0'})}
    result = requests.post(url, headers=headers, files={"file": f}, data=params)

    # print(result.text)
    res = result.content.replace(b"null", b"None").decode('utf-8')
    fmtprint(res)
    return result.text

def post_uploadlist(url):
    # requests.post(url, data=params, files={"file": f})
    from urllib import parse
    file_name = "E:\\file\\gcc.exe"
    url = 'http://{}/app/uploadlist'.format(url)
    f = open(file_name, 'rb')
    import os
    filesize = os.path.getsize(file_name)

    params = {"curpath": "public/Extra", "loginname": "Tornado", "token": TOKEN}

    headers = {'User-Agent': "Mobile", 'filesize': str(filesize)}
    # fl = open('test.png', 'rb')
    # files = {'files': ('test.png', fl, 'application/octet-stream', {'Expires': '0'})}
    # result = requests.post(url, headers=headers, files={"file": f}, data=params)

    files = {
        "files": [
            open("E:\\file\\gcc.exe", "rb"),
            open("E:\\file\\config.json", "rb"),
            open("E:\\file\\OpsPython.tar.gz", "rb")
        ]
    }
    files = {
            "f1": open("E:\\file\\gcc.exe", "rb"),
            "f2": open("E:\\file\\config.json", "rb"),
            "f3": open("E:\\file\\OpsPython.tar.gz", "rb")
    }
    files = [
        ("files", open("E:\\file\\gcc.exe", "rb")),
        ("files", open("E:\\file\\config.json", "rb")),
        ("files", open("E:\\file\\OpsPython.tar.gz", "rb"))
    ]
    print(type(f))
    result = requests.post(url, headers=headers, files=files, data=params)
    # print(result.text)
    res = result.content.replace(b"null", b"None").decode('utf-8')
    fmtprint(res)
    return result.text


def get_download(url):
    from urllib import parse
    url = 'http://{}/download'.format(url)
    headers = {"User-Agent": "Mobile"}
    params = {"filename": "public/Extra/OpsPython.tar.gz", "loginname": "Tornado", "token": TOKEN}
    result = requests.get(url, headers=headers, params=params)
    # result = requests.post(url, headers=headers, data=params)
    # print(result.text)
    ctx = result.content
    print(len(ctx))
    if len(ctx) > 10:
        print(ctx[0:100])
    # print("headers:", result.headers)
    # print(result.headers['content-length'])
    # file_name = result.headers['Content-Disposition'].split('=')
    # print(file_name)
    import os
    with open("/opt/data/public/File"+ "/" + os.path.basename(params.get("filename")), "wb") as f:
        f.write(ctx)
    return ctx

def mutilpool(url):
    from threadpool import ThreadPool, makeRequests

    task_pool = ThreadPool(8)
    request_list = []  # 存放任务列表
    urls = []
    # 首先构造任务列表
    for device in range(20):
        urls.append(url)
        request_list.append(makeRequests(view, url))
    # map(task_pool.putRequest, request_list)
    requests = makeRequests(view, urls)
    [task_pool.putRequest(req) for req in requests]
    task_pool.wait()


TOKEN = "5ba74eaaae2445a1cb0b08eb463b5266"
if __name__ == "__main__":
    # url = "127.0.0.1:807"
    url = "139.196.197.13:807"
    # url = "139.224.231.14:9016"
    import time
    ts = time.time()
    # get_token(url)
    # post_ava()
    # post_next()
    # img_resize()
    # get_version(url_remote)
    # put_version()
    # get_userinfo()
    # get_videoshortcut_base64(1, 2)
    # get_fsmain(url_remote)
    # get_users(url)
    # get_userlist(url)
    # post_value(url)
    # get_value(url)
    # post_dir(url)
    play(url)
    # view(url)
    # post_upload(url)
    # post_uploadlist(url)
    # get_download(url)
    te = time.time()
    print(te - ts)
    # get_version_(url_remote)
    # print(time.time() - te)
    # BFS（百度） GoogleFS（谷歌） TFS（淘宝）
    # from database.tbl_account import TblAccount
    # res = db().query(TblAccount.loginname, TblAccount.last_logintime, TblAccount.register_time).all()
    # for i in res:
    #     print(i)
    mutilpool(url)
