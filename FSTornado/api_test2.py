#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 16:21
# @Author  : 1823218990@qq.com
# @File    : api_test2.py
# @Software: PyCharm

import requests
user = "admin1"
pwd = "admin#_@0831"


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
        # add_word(url, imgpath)
        time.sleep(1)


def add_word(url, imgpath=None):
    import os
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


if __name__ == '__main__':
    url = "127.0.0.1:9080"
    # add_word(url)
    add_all(url)