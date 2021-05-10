#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 22:10
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import json

import pytest

from pylib.APIlib.trainingAPI import TrainingAPI


@pytest.fixture()
def init_training(get_cookie, init_course):
    """
    初始化创建培训班
    :param get_cookie:
    :param init_course:
    :return:
    """
    trainingAPI = TrainingAPI(get_cookie)
    courseAPI = init_course[0]
    # 获取课程信息，作为创建培训班的字段信息
    coursesInfo = courseAPI.list()["retlist"]
    courseInfo = []
    i = 0
    for course in coursesInfo:
        course_dict = {"id": course["id"], "name": course["name"]}
        courseInfo.append(course_dict)
        i = i + 1
        if i == 3:
            break
    # 非常关键，把列表转换换json字符串
    courseList = json.dumps(courseInfo, ensure_ascii=False)
    new_training = trainingAPI.add(name="语文培训22班",
                                   desc="语文培训班22",
                                   display_idx=100,
                                   courselist=courseList)
    yield trainingAPI, new_training

@pytest.fixture(scope="session")
def get_trainingAPI(get_cookie):
    trainingAPI = TrainingAPI(get_cookie)
    return trainingAPI
