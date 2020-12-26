#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys  # 标准输入输出的控制
import os   # 创建和处理子进程
import time # 时间的显示

'''
手工编写第一个daemon
'''


def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:
        # 创建子进程
        pid = os.fork()
        print('fork#1 的 pid is:{}'.format(os.getpid()))
        if pid > 0:
            # 父进程先与子进程exit，会使子进程变为孤儿进程
            # 这样子进程呗init这个用户级守护进程手痒
            sys.exit(0)  # 0表示正常退出
    except OSError as err:
        sys.stderr.write('_Fork #1 faild: {0}\n'.format(err))
        sys.exit(1) # 1表示非期望的退出
    os.system('ps -ef|grep test003.py')

    # 从父进程环境脱离
    # decouple from parent environment
    # chdir 确认进程不占用任何目录，否则不能umount
    os.chdir("/")
    # 调用umask（0） 拥有写任何文件的权限，避免进程自父进程的umask呗修改导致自身权限不足
    os.umask(0)
    # setid调用成功后，进程成为新的会话组长和新的进程租场，并与原来的登录会话和进程组脱离
    os.setsid()

    #第二次fork
    try:
        pid = os.fork()
        print('fork#2  的 pid is:{}'.format(os.getpid()))
        if pid >0:
            # 第二个父进程退出
            sys.exit(0)
    except OSError as err:
        sys.stderr.write('_Fork #2 faild: {0}\n'.format(err))
        sys.exit(1)
    os.system('ps -ef|grep test003.py')

    # 重定向标准文件描述符
    sys.stdout.flush()
    sys.stderr.flush()
    si = open(stdin,'r')
    so = open(stdout,'a+')
    se = open(stderr,'w')

    # dup2 函数原子化关闭和复制文件描述符
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

# 每秒显示一个时间戳
def test():
    print('test start')
    sys.stdout.write('Daemon started with pid %d\n' % os.getpid())
    while True:
        now = time.strftime("%X",time.localtime())
        sys.stdout.write(f'{time.ctime()}\n')   # 输出时间
        sys.stdout.flush()  # 1111
        time.sleep(1)


# 主函数
if __name__ == "__main__":
    daemonize('/dev/null','/opt/geektime_code/week01/d1.log','/dev/null')
    print('daemonize end')
    test()

time.sleep(20)
