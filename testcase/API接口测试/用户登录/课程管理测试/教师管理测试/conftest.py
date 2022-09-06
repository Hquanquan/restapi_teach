#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 23:08
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from pylib.APIlib.teacherAPI import TeacherAPI


@pytest.fixture()
def init_teacher(get_cookie, init_course):
    """
    初始化创建教师
    :param get_cookie:
    :param init_course:
    :return:
    """
    teacherAPI = TeacherAPI(get_cookie)
    courseAPI = init_course[0]
    course = courseAPI.list()["retlist"][0]
    courseInfo = [{"id": course["id"], "name": course["name"]}]
    new_teacher = teacherAPI.add(username="数学老师",
                                 realname="王大锤",
                                 courses=courseInfo)
    yield teacherAPI, courseAPI, new_teacher
    teacherAPI.delete(new_teacher["id"])


