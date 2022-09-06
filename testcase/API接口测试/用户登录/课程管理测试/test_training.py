#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 21:42
# @File : test_training.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前没有培训班
import json

import allure
import pytest


@allure.epic("教管系统-接口测试")
@allure.feature("培训班管理模块")
class TestTrainingAPI:
    """
    培训班API测试类
    """

    @pytest.fixture()
    def before_test_add_training(self, empty_training, init_course):
        """
        前置条件：1、创建课程
                2、清空所有的培训班
        """
        self.trainingAPI = empty_training
        self.courseAPI = init_course[0]
        # 获取课程信息，作为创建培训班的字段信息
        coursesInfo = self.courseAPI.list()["retlist"]
        courseInfo = []
        i = 0
        for course in coursesInfo:
            course_dict = {"id": course["id"], "name": course["name"]}
            courseInfo.append(course_dict)
            i = i + 1
            if i == 3:  # 只获取3个课程
                break
        # 非常关键，把列表转换换json字符串
        self.courseList = json.dumps(courseInfo, ensure_ascii=False)
        yield
        self.trainingAPI.delete_all()

    @allure.story("培训班管理-添加培训班")
    @allure.title("当前系统没有培训班，添加培训班")
    @pytest.mark.addTraining
    def test_add_training(self, before_test_add_training):
        """
        当前系统没有培训班，添加培训班,预期结果：添加成功
        :param before_test_add_training:
        :return:
        """
        self.new_training = self.trainingAPI.add(name="语文培训22班",
                                                 desc="语文培训班22",
                                                 display_idx=102,
                                                 courselist=self.courseList)
        assert self.new_training["retcode"] == 0
