#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import sys


c = bytes('a',encoding='utf-8')
# cc = bytes('abcd',encoding='utf-8')
cc = bytes('好好学习天天向上',encoding='utf-8')

for i in c:
    print(sys.getsizeof(i))
    print(id(i))
for i in cc:
    print(sys.getsizeof(i))
    print(hex(id(i)))

counter = 0
str = "123"
str1 = "abcd"
# print(f'str size is {sys.getsizeof(str)}')
# print(f'str size is {sys.getsizeof(str1)}')
# print('增加1个字符，内存开销为{}字节'.format(sys.getsizeof(str1)-sys.getsizeof(str)))
for i in str:
    print(f'i的类型为{type(i)}')
    byte_list = bytes(i, encoding="utf-8")
    print('byte_list 的类型为', type(byte_list), f'byte_list长度{len(byte_list)}')
    print('*' * 11, byte_list)
    for k in byte_list:
        counter += 1
        print('byte_list的基本元素类型为 ', type(k))
        print('占用的磁盘空间为', sys.getsizeof(k))
        print('二进制码：',bin(k))
        print('16进制内存地址为：',hex(id(k)))
        print('one count of k')
print(counter)
print('*'*88)

# for i in str1:
#     byte_list = bytes(i,encoding='utf-8')
#     print(f'字符串内字符的内地地址{hex(id(i))}')
#     for k in byte_list:
#         print(hex(id(k)))


# print(aa)
print(sys.getsizeof(c))
print(sys.getsizeof(cc))