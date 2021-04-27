#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 22:43
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from pylib.APIlib.courseAPI import CourseAPI
from pylib.APIlib.loginAPI import LoginAPI


@pytest.fixture(scope="session")
def get_cookie():
    """获取cookie"""
    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    return cookie

@pytest.fixture(scope="session")
def empty_course(get_cookie):
    """
    清空课程
    :param get_cookie:
    :return: 返回courseAPI实例对象
    """
    courseAPI = CourseAPI(get_cookie)
    courseAPI.delete_all()
    yield courseAPI


