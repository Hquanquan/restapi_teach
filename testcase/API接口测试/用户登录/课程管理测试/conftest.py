#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 21:11
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

import pytest

from pylib.APIlib.courseAPI import CourseAPI
from pylib.APIlib.teacherAPI import TeacherAPI


@pytest.fixture(scope="session")
def init_course(get_cookie):
    """
    创建课程
    :param get_cookie:
    :return:
    """
    courseAPI = CourseAPI(get_cookie)
    new_course = courseAPI.add(name="物理课",
                               desc="初中物理课",
                               display_idx=1)
    yield courseAPI, new_course
    courseAPI.delete(new_course["id"])

@pytest.fixture(scope="session")
def init_course_to_delete(get_cookie):
    """
    创建课程
    :param get_cookie:
    :return:
    """
    courseAPI = CourseAPI(get_cookie)
    new_course = courseAPI.add(name="物理课",
                               desc="初中物理课",
                               display_idx=1)
    yield courseAPI, new_course

@pytest.fixture(scope="session")
def empty_teacher(get_cookie):
    """
    清空教师
    :param get_cookie:
    :return:
    """
    teacherAPI = TeacherAPI(get_cookie)
    teacherAPI.delete_all()
    yield teacherAPI

