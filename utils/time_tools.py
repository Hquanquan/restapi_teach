#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 23:10
# @File : time_tools.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 时间相关的工具
import datetime


def get_CurrentTime(time_formate="%Y-%m-%dT%H:%M:%S.%f", tager=True):
    """
    获取当前时间，转换为指定的字符串格式返回
    :param time_formate: 格式
    :param tager: 默认
    :return: 2021-05-08T23:14:03.062Z
    """
    dt = datetime.datetime.now()
    current_time = dt.strftime(time_formate)
    if not tager:
        return current_time
    return current_time[:-3] + "Z"




if __name__ == '__main__':

    print(get_CurrentTime())

