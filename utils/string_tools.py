#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 14:07
# @File : string_tools.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import hashlib
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


def get_md5(psw):
    """
    MD5加密字符
    :param psw: 需要加密的字符串
    :return: 返回加密后的数据
    """
    # 实例化一个md5对象
    md5 = hashlib.md5()
    # 加密字符
    md5.update(psw.encode('utf-8'))
    # 调用hexdigest()获取加密结果数据，并返回
    return md5.hexdigest()


if __name__ == '__main__':
    print(Unicode())
    print(GBK2312())
