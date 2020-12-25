#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

content = "13231143991"
a = re.match(".{11}",content).group()
a1 = re.match(".{11}",content).span()
print(a)
print(a1)

a2 = re.match("@","123@123.com")
a3 = re.match(".*@.*","123@123.com")
print(a2)
print(a3)
a4 = re.match(".*@.*","123@123.com").group()
print(a4)

a5 = re.match("(.*)@(.*)","abc@123.com").group(2)
print(a5)

a6 = re.search("@",'abc@123.com')
print(a6)

a7 = re.findall("123","123@123.com")
print(a7)

a8 = re.sub("123","abc","123@123.com")
a9 = re.sub("\d","xyz","123@123.com")
a10 = re.sub("\d+","xyz","123@123.com")
# a11 = re.sub("\d.","xyz","123@123.com")
print(a8)
print(a9)
print(a10)
# print(a11)

a12 = re.split("@","123@123.com")
a13 = re.split("(@)","123@123.com")
print(a12)
print(a13)