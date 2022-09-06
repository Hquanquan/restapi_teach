#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 23:07
# @File : test_teachers.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import allure
import pytest


@allure.epic("教管系统-接口测试")
@allure.feature("教师管理模块")
class TestTeacherAPI:

    @pytest.fixture()
    def before_test_add_teacher001(self, init_teacher):
        self.teacherAPI = init_teacher[0]
        self.courseAPI = init_teacher[1]
        courses = self.courseAPI.list()["retlist"]
        self.courseInfo = []
        for course in courses:
            course_dict = {"id": course["id"], "name": course["name"]}
            self.courseInfo.append(course_dict)
        yield
        self.teacherAPI.delete(self.new_teacher["id"])

    @allure.story("教师管理-添加教师")
    @allure.title("当前系统已存在教师，正常添加系统不存在的教师")
    @pytest.mark.addTeacher
    def test_add_teacher001(self, before_test_add_teacher001):
        """
        当前系统已有教师，正常添加系统不存在的教师
        :param before_test_add_teacher001:
        :return:
        """
        self.new_teacher = self.teacherAPI.add(username="语文老师",
                                               realname="李三",
                                               courses=self.courseInfo)
        assert self.new_teacher["retcode"] == 0

    @pytest.fixture()
    def before_test_add_teacher002(self, init_teacher):
        """
        前置条件：1、创建一个课程
                2、创建一个教师
        """
        self.teacherAPI = init_teacher[0]
        self.courseAPI = init_teacher[1]
        courses = self.courseAPI.list()["retlist"]
        self.courseInfo = []
        for course in courses:
            course_dict = {"id": course["id"], "name": course["name"]}
            self.courseInfo.append(course_dict)
        yield

    @allure.story("教师管理-添加教师")
    @allure.title("当前系统已存在教师，正常添加系统已存在的教师")
    @pytest.mark.addTeacher
    def test_add_teacher002(self, before_test_add_teacher002):
        """
        当前系统已有教师，正常添加系统已存在的教师
        :param before_test_add_teacher002:
        :return:
        """
        self.new_teacher = self.teacherAPI.add(username="数学老师",
                                               realname="王大锤",
                                               courses=self.courseInfo)
        assert self.new_teacher["retcode"] == 1 and "已经存在" in self.new_teacher["reason"]
