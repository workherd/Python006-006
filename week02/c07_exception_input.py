#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import pretty_errors

class UserInputError(Exception):
    def __init__(self, ErroInfo):
        super().__init__(self, ErroInfo)
        self.errorinfo = ErroInfo

    def __str__(self):
        return self.errorinfo


userinput = 'a'
b = 1/0
try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    print('run finnally')
    del userinput

print('func end')