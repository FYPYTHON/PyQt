#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 11:03
# @Author  : 1823218990@qq.com
# @File    : UDPClient.py
# @Software: PyCharm

import socket
import time

# 创建socket对象
# SOCK_DGRAM  udp模式
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送数据 字节
ip = "172.16.83.222"
# ip = "127.0.0.1"
port = 5060

count = 0
receive_count = count
while True:
    msg = 'PTIONS sip:0512110000232@10.67.1.108:42035;transport\u003dTCP SIP/2.0\r\n' \
          'Via: SIP/2.0/UDP 10.67.18.123:5090;rport;branch\u003dz9hG4bKPjEF7fucovPYFn2.kQvfL5vQaYdNj30jAO\r\n' \
          'Max-Forwards: 70\r\nFrom: \"wqq的会议\" \u003csip:1231208@10.67.18.123:5090\u003e;tag\u003drR-Uo08Egguwcjldq2.RdU0lY1L8RSL1\r\n' \
          'To: \u003csip:0512110000232@10.67.1.108:42035\u003e;tag\u003dcd91c06e2a90418f982e8623fde90fc6\r\n' \
          'Call-ID: 02502d47-47b9-3835-102a-5634343434ef\r\nCSeq: 81 OPTIONS\r\n' \
          'Route: \u003csip:10.67.18.123:5060;lr\u003e\r\nContent-Length:  {}\r\n\r\n'.format(count)
    s.sendto(msg.encode(), (ip, port))
    count += 1
    print(count)
    time.sleep(0.001)
    if count == 10 ** 6:
        s.sendto("close".encode(), (ip, port))
        break


