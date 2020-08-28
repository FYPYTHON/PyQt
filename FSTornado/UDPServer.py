#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 11:02
# @Author  : 1823218990@qq.com
# @File    : UDPServer.py.py
# @Software: PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 5060

s.bind((ip, port))  # 绑定服务器的ip和端口
while True:
    data = s.recv(1024)  # 一次接收1024字节
    print(data.decode())  # decode()解码收到的字节
    if data.decode() == "close":
        break
