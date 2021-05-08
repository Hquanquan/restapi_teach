#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 22:48
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from pylib.APIlib.lessonAPI import LessonAPI
from utils.time_tools import get_CurrentTime


@pytest.fixture(scope="session")
def init_lesson(get_cookie, init_course):
    lessonAPI = LessonAPI(get_cookie)
    courseAPI = init_course[0]
    course_id = init_course[1]["id"]
    new_lesson = lessonAPI.add(course_id=course_id,
                               starttime=get_CurrentTime(),
                               # "endtime": "2023-12-31T23:00:00.000Z",  默认使用这个
                               desc="课时描述")
    yield lessonAPI, courseAPI


@pytest.fixture(scope="session")
def get_lessonAPI(get_cookie):
    lessonAPI = LessonAPI(get_cookie)
    return lessonAPI
