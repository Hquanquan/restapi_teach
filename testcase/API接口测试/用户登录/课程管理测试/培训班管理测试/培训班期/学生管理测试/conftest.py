#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 10:06
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from pylib.APIlib.studentAPI import StudentAPI


@pytest.fixture(scope="session")
def get_studentAPI(get_cookie):
    """
    获取studentAPI实例对象
    :param get_cookie:
    :return:
    """
    studentAPI = StudentAPI(get_cookie)
    return studentAPI


@pytest.fixture()
def init_student(get_cookie, init_trainingGrade):
    studentAPI = StudentAPI(get_cookie)
    trainingGradeAPI = init_trainingGrade[0]
    trainingAPI = init_trainingGrade[1]
    training_id = trainingAPI.list()["retlist"][0]["id"]
    trainingGrade_id = trainingGradeAPI.list()["retlist"][0]["id"]
    new_student = studentAPI.add(username="小明",
                                 realname="王小明",
                                 desc="学生王小明的描述信息",
                                 # "password": "123456",
                                 # "startcoursedate": "2021-02-15T07:50:53.345Z",
                                 training_id=training_id,
                                 traininggrade_id=trainingGrade_id)

    yield studentAPI, trainingGradeAPI, trainingAPI, new_student
    # studentAPI.delete(new_student["id"])
    # trainingGradeAPI.delete_all()
