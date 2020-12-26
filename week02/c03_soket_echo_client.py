#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST = 'localhost'
PORT = 10011

def echo_client():
    # Echo server  client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True:
        # 接收用户输入数据并发送服务端
        data = input('input >')

        # 设定退出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data.encode())

        # 接收服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    s.close()


if __name__ == '__main__':
    echo_client()
