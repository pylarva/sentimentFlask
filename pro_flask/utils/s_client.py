# !/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


def send_message(msg, ip, port):
    sk = socket.socket()
    sk.connect((ip, port))
    sk.settimeout(5)
    data = sk.recv(1024).decode()
    print(msg)
    sk.sendall(msg.strip().encode())
    data = sk.recv(1024).decode()
    print('server:', data)
    sk.close()
    return data


if __name__ == '__main__':
    data = send_message(msg='你好', ip='127.0.0.1', port=9997)
    print(data)