#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 17:19
# @Author  : wangguoqiang@kedacom.com
# @File    : api_test.py
# @Software: PyCharm

import requests


def get_token():
    url = 'http://139.224.231.14:9016/login'
    headers = {'User-Agent': "Mobile"}
    parmas = {"userAccount": "Tornado", "password": "dgj_039103", "inputCode": "APP"}
    result = requests.post(url, data=parmas, headers=headers)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    # print(result.content)
    res = result.content.decode('utf-8')
    jres = eval(res)
    print(jres)
    if "token" in jres.keys():
        return jres.get("token")
    return result.text


# TOKEN = get_token()
TOKEN = "9ac32aea3dc5e77cbd24744a3a0de8b0"


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


def get_version():
    url = 'http://139.224.231.14:9016/appversion'

    parmas = {"loginname": "Tornado", "token": TOKEN}
    headers = {'User-Agent': "Mobile"}
    result = requests.get(url, headers=headers, params=parmas)
    # result = requests.post(url, headers=headers, files={"FILE": None})
    # print(result.text)
    res = result.content.decode('utf-8')
    jres = eval(res)
    print(jres)
    return result.text


def put_version():
    url = 'http://139.224.231.14:9016/appversion'

    parmas = {"loginname": "Tornado", "token": TOKEN, "version": "1.0"}
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
    realpath = "E:\\IMG_20190607_163529.jpg"
    # realpath = "E:\\tk_color.png"
    img = Image.open(realpath)
    suffix = realpath.split('.')[-1]
    if suffix == "jpg":
        suffix = "jpeg"
    print("image size: {} {}".format(img.size, os.path.getsize(realpath)))
    img_size = os.path.getsize(realpath)
    beishu = img_size / 1024 / 1024
    print("beisu", beishu)
    if beishu >= 2:
        small_size = (int(img.size[0] / beishu), int(img.size[0] / beishu))
    else:
        small_size = img.size
    small_size = (int(img.size[0]/1.1), int(img.size[0]/1.1))
    img = img.resize(small_size, Image.ANTIALIAS)
    output_buffer = BytesIO()
    img.save(output_buffer, format=suffix)
    print("image size: {} {}".format(img.size, os.path.getsize(realpath)))
    binary_data = output_buffer.getvalue()
    base64_data = base64.b64encode(binary_data).decode()
    # 821824 - 178244
    import zlib
    zipdata = zlib.compress(base64_data.encode())
    print(len(base64_data), type(base64_data))
    print("zip:", len(zipdata), len(zipdata) / len(base64_data))

    img.save("E:\\test.jpg")


if __name__ == "__main__":
    # get_token()
    # post_ava()
    # post_next()
    # img_resize()
    # get_version()
    # put_version()
    get_userinfo()
