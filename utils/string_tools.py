#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 14:07
# @File : string_tools.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

import random

def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

if __name__ == '__main__':
    print(Unicode())
    print(GBK2312())