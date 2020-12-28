#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def strip_operate(exp):    # 合并多余的操作符
    exp = exp.replace("+-", "-")
    exp = exp.replace("--", "+")
    exp = exp.replace("-+", "-")
    exp = exp.replace("++", "+")
    return exp


def cal_exp_son(exp_son):    # 计算两数的乘除
    if "/" in exp_son:
        a, b = exp_son.split("/")
        return str(float(a)/float(b))
    elif "*" in exp_son:
        a, b = exp_son.split("*")
        return str(float(a)*float(b))


def cal_no_bracket(exp):    # 计算一个里面已经没有括号的式子
    exp = exp.strip("()")
    while True:
        ret1 = re.search(r"\d+\.?\d*[/*]-?\d+\.?\d*", exp)
        if ret1:     # 先乘除
            exp_son = ret1.group()
            ret2 = cal_exp_son(exp_son)
            exp = exp.replace(exp_son, ret2)
            exp = strip_operate(exp)
        else:      # 后加减
            ret4 = re.findall(r"-?\d+\.?\d*", exp)
            sum1 = 0
            for i in ret4:
                sum1 += float(i)
            return str(sum1)


def main_1(express):
    while True:
        ret = re.search(r"\([^()]+\)", express)
        if ret:
            express_no_bracket = ret.group()
            ret3 = cal_no_bracket(express_no_bracket)
            express = express.replace(express_no_bracket, ret3)
            express = strip_operate(express)
        else:
            ret4 = cal_no_bracket(express)
            return ret4


# express = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
express = '1 -+22 )'
express = express.replace(" ", "")
ret5 = main_1(express)
print(ret5)
