#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 20:31
# @Author     : john
# @File       : c09_04_security_sigle.py

# World.py
import Sun
def run():
    while True:
        Sun.rise()
        Sun.set()

# main.py
import World
World.run()