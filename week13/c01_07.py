#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:28
# @Author     : john
# @File       : c01_07.py


class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误1111')
except UserInputError as ue:
    print(ue)
finally:
    del userinput

print('end')