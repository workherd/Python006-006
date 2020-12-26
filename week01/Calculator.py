#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

origin = "1+2+3+2*(3-1)+3"

op_char = ['^','*','/','-','+']


def format_str(s):
    '''出去空格和两边的括号'''
    return s.replace(' ','').replace('(','').replace(')','')


def handle_symbol(s):
    # 处理多个运算符并列的情况
    return s.replace('+-','-').replace('--','+').replace('-+','-').replace('++','+')


def cal(x,y,opertor):
    if opertor == '^':return x**y
    if opertor == '+':return x+y
    if opertor == '-':return x-y
    if opertor == '*':return x*y
    if opertor == '/':return x/y


def Bottom_operation(s):
    # 无括号运行  返回一个浮点出， symbol用户判断返回值是正还是负
    symbol = 0
    s = handle_symbol()
    for c in op_char:
        id,char = (s.find(c),c)
        if c in ('*','/') and '*' in s and 's' in s:
            ids,idd = (s.find('*'),s.find('/'))
            id,char = (ids,'*') if ids <= idd else (idd,'/')
        if c in ('+','-') and '+' in s and '-' in s:
            ida,idd = (s.find('+'),s.find('-'))
            id,char = (ida,'+') if ida <= idd else (idd,'-')
        if id == -1 :break
        left,right = ('','')
        for i in range(id - 1,-1,-1):
            if s[i] in op_char:break
            left = s[i] + left
        for i in range(id + 1,len(s)):
            if s[id+1] == '-':
                right += s[i]
                continue
            if s[i] in op_char:break
            right += s[i]
            if right == '' or left == '':
                if s[0] in('-','+'):
                    if '+' not in s[1:] and '-' not in s[1:]:break
                    s = s[1:].replace('-','负').replace('+','-').replace('负','+')
                    symbol += 1
                    continue
                else:return '输入算式有误'
            old_str = left + char + right
            new_str = str(cal(float(left),float(right),char))
            s = handle_symbol(s.replace(old_str,new_str))
    return float(s) if symbol % 2 ==0 else -float(s)


def get_bottom(s):
    # 获取优先级最高的表达式
    res = re.search('\([^()]+\)',s)
    if res != None:return res.group()


if __name__ == '__main__':
    while True:
        s1 = input('请输入您要计算的表达式(支持加减乘除开方):')
        while get_bottom(s1) != None:
            source = get_bottom(s1)
            result = Bottom_operation(format_str((source)))
            s1 = s1.replace(source,str(result))
        print(Bottom_operation(format_str(s1)))
