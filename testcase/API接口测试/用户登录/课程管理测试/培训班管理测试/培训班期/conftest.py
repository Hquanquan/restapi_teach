#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:24
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from pylib.APIlib.trainingGradeAPI import TrainingGradeAPI


@pytest.fixture(scope="session")
def get_trainingGradeAPI(get_cookie):
    trainingGradeAPI = TrainingGradeAPI(get_cookie)
    return trainingGradeAPI


@pytest.fixture()
def init_trainingGrade(get_cookie, init_training):
    """初始化创建一个培训班期"""
    trainingGradeAPI = TrainingGradeAPI(get_cookie)
    trainingAPI = init_training[0]
    training_id = trainingAPI.list()["retlist"][0]["id"]
    new_trainingGrade = trainingGradeAPI.add(name="语文培训班期",
                                             desc="语文培训班期描述",
                                             display_idx=30,
                                             training_id=training_id)
    yield trainingGradeAPI, trainingAPI, new_trainingGrade
    # 删除创建的培训班信息
    trainingAPI.delete_all()
