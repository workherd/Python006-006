#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import logging
import os

# start
creat_timer = time.strftime('%Y-%m-%d',time.localtime())
log_path = '/var/log/python-{}/'.format(creat_timer)
if not os.path.exists(log_path):
    os.mkdir(log_path)
abs_path = log_path + "logger_demo.log"
logging.basicConfig(filename=r"{}".format(abs_path),
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s.%(msecs)d %(levelname)s  %(name)s  [line: %(lineno)d] %(message)s')

def loger():
    for i in range(10):
        print(i)
        logging.info('This is {}!'.format(i))


loger()