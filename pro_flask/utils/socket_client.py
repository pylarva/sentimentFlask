# !/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


class send_message():
    def __init__(self, msg, ip, port):
        self.msg = msg
        self.ip = ip
        self.port = port

    def send(self):
        ip_port = (self.ip, self.port)
        sk = socket.socket()
        sk.connect(ip_port)
        sk.settimeout(5)
        data = sk.recv(1024).decode()
        print('Send Message: %s' % data)
        inp = self.msg
        print(inp)
        if not inp:
            return '未发送任何数据...'
        sk.sendall(inp.encode())
        data1 = sk.recv(1024).decode()
        sk.close()
        print(data1)
        return data1


if __name__ == '__main__':
    s_obj = send_message(msg='hahah', ip='127.0.0.1', port=9997)
    data = s_obj.send()
    print(data)