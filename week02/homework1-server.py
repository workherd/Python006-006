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
    # accept 表示接收用户端的链接
    conn, addr = s.accept()
    # 输出客户端的地址


    conn.sendall(bytes('welcome send files',encoding='utf-8'))

    file_size = str(conn.recv(1024),encoding='utf-8')
    conn.sendall(bytes('1001',encoding='utf-8'))
    total_size = int(file_size)
    has_recv = 0

    f = open('new.html', 'wb')
    while True:
        if total_size == has_recv:
            break

        data = conn.recv(1024)
        f.write(data)
        has_recv += len(data)

    f.close()

print( 'kkkk')


if __name__ == '__main__':
    print('server run')
    echo_server()