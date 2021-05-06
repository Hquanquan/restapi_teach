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
from pylib.APIlib.trainingAPI import TrainingAPI


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


@pytest.fixture(scope="session")
def empty_training(get_cookie):
    """清空培训班"""
    trainingAPI = TrainingAPI(get_cookie)
    trainingAPI.delete_all()
    yield trainingAPI


@pytest.fixture(scope="session")
def get_trainingAPI(get_cookie):
    """
    返回trainingAPI实例对象
    :param get_cookie:
    :return:
    """
    trainingAPI = TrainingAPI(get_cookie)
    return trainingAPI
