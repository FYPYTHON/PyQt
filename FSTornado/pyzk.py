#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 23:04
# @Author  : 1823218990@qq.com
# @File    : pyzk
# @Software: Pycharm
from kazoo.client import KazooClient
from datetime import datetime
import time
zk = KazooClient(hosts="192.168.0.224:2171")
zk.start()

def pp(event):
    print("event go", datetime.now())

def main():
    try:

        print(time.time())
        zk.get("/test", watch=pp)
        msg = "t:{}".format(time.time())
        zk.create("/Resource/Mxm/Source/Mxm", msg.encode(), makepath=True)

        zk.set("/test", msg.encode())
        time.sleep(0.1)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        main()