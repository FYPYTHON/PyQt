#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 19:24
# @Author  : wangguoqiang@kedacom.com
# @File    : TcpClient.py
# @Software: PyCharm
# port 5060 test use socket to send sip packet
import socket
import sys

# receive_count: int = 0


def start_tcp_client(ip, port):
    ###create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    failed_count = 0
    while True:
        try:
            print("start connect to server ")
            s.connect((ip, port))
            break
        except socket.error:
            failed_count += 1
            print("fail to connect to server %d times" % failed_count)
            if failed_count == 100: return

    # send and receive
    while True:
        print("connect success")

        # get the socket send buffer size and receive buffer size
        s_send_buffer_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        s_receive_buffer_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

        print("client TCP send buffer size is %d" % s_send_buffer_size)
        print("client TCP receive buffer size is %d" % s_receive_buffer_size)

        receive_count = 0
        while True:
            msg = 'PTIONS sip:0512110000232@10.67.1.108:42035;transport\u003dTCP SIP/2.0\r\n' \
                  'Via: SIP/2.0/UDP 10.67.18.123:5090;rport;branch\u003dz9hG4bKPjEF7fucovPYFn2.kQvfL5vQaYdNj30jAO\r\n' \
                  'Max-Forwards: 70\r\nFrom: \"wqq的会议\" \u003csip:1231208@10.67.18.123:5090\u003e;tag\u003drR-Uo08Egguwcjldq2.RdU0lY1L8RSL1\r\n' \
                  'To: \u003csip:0512110000232@10.67.1.108:42035\u003e;tag\u003dcd91c06e2a90418f982e8623fde90fc6\r\n' \
                  'Call-ID: 02502d47-47b9-3835-102a-5634343434ef\r\nCSeq: 81 OPTIONS\r\n' \
                  'Route: \u003csip:10.67.18.123:5060;lr\u003e\r\nContent-Length:  {}\r\n\r\n'.format(receive_count)

            s.send(msg.encode('utf-8'))
            print("send len is : [%d]" % len(msg))

            msg = s.recv(1024)
            print(msg.decode('utf-8'))
            print("recv len is : [%d]" % len(msg))

            import time
            # time.sleep(0.001)

            receive_count += 1

            if receive_count == 10**6:
                msg = 'disconnect'
                print("total send times is : %d " % receive_count)
                s.send(msg.encode('utf-8'))
                break

        break

    s.close()


if __name__ == '__main__':
    # ip = "127.0.0.1"
    ip = "172.16.83.222"
    start_tcp_client(ip, 5060)