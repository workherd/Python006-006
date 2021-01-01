
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import os

HOST = 'localhost'
PORT = 10011

def echo_client():
    # Echo server  client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    # start
    print('conn start')
    ret_bytes = s.recv(1024)
    print(str(ret_bytes,encoding='utf-8'))
    print('conn finished')
    size = os.stat('index111.html').st_size
    print('file size is ',size)
    s.sendall(bytes(str(size),encoding='utf-8'))

    s.recv(1024)


    # 发送文件
    with open('index111.html','rb') as f:
        for line in f:
            s.sendall(line)
    s.close()

print('finished')
if __name__ == '__main__':
    echo_client()
