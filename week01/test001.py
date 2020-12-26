#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


def add_sub(a_s):
    if '--' in a_s:
        a_s = a_s.replace('--', '+')
    # if '-+' in a_s:
    #     a_s = a_s.replace('-+','-')
    # if '+-' in a_s:
    #     a_s = a_s.replace('+-','-')

    a_s = re.findall('\-?\d+\.?\d*', a_s)
    ls = []
    for i in range(len(a_s)):
        ls.append(float(a_s[i]))
    return str(sum(ls))


def mul_div(m_d):
    while True:
        m_d01 = re.search(r'\d+\.?\d*[*/](\d+\.?\d*)', m_d)
        if m_d01 == None: return m_d
        if '*' in m_d01.group():
            m_d02 = re.findall(r'\d+\.?\d*', m_d01.group())
            result = float(m_d02[0]) * float(m_d02[1])
            m_d = re.sub(r'\(?\d+\.?\d*\*(\d+\.?\d*)\)?', str(result), m_d, 1)
        elif '/' in m_d01.group():
            m_d03 = re.findall(r'\d+\.?\d*', m_d01.group())
            result = float(m_d03[0]) / float(m_d03[1])
            m_d = re.sub(r'\(?\d+\.?\d*\/(\d+\.?\d*)\)?', str(result), m_d, 1)
        else:
            break
    return m_d


def result_all(r_a):
    while True:
        if re.findall('[*/]', r_a):
            r_a = mul_div(r_a)
        if re.findall('[+-]', r_a):
            r_a = add_sub(r_a)
        else:
            break
    return r_a


def remove_brackets(r_b):
    while True:
        if '(' in r_b:
            r_b1 = re.search(r'\([^()]+\)', r_b)
            r_b1 = result_all(r_b1.group())
            r_b = re.sub(r'\([^()]+\)', str(r_b1), r_b, 1)
        else:
            break
    return result_all(r_b)


while True:
    run_num = "".join(input(">>输入计算公式:").split())
    print(remove_brackets(run_num.strip()))
