#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST = 'localhost'
PORT = 10011

def echo_server():
    # echo server 的server端

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象绑定到指定的主机和端口上
    s.bind((HOST,PORT))
    # 只接收1个链接
    s.listen(1)
    while True:
        # accept 表示接收用户端的链接
        conn, addr = s.accept()
        # 输出客户端的地址
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
    s.close()


if __name__ == '__main__':
    echo_server()