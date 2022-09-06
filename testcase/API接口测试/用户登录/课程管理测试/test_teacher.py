#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 11:46
# @File : test_teacher.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前没有教师
import allure
import pytest


@allure.epic("教管系统-接口测试")
@allure.feature("教师管理模块")
class TestTeacherAPI:

    @pytest.fixture()
    def before_test_add_teacher001(self, empty_teacher, init_course):
        """
        前置条件：创建课程，获取课程信息
        """
        self.teacherAPI = empty_teacher
        self.courseAPI = init_course[0]
        courses = self.courseAPI.list()["retlist"]
        self.courseInfo = []
        for course in courses:
            course_dict = {"id": course["id"], "name": course["name"]}
            self.courseInfo.append(course_dict)
        yield
        """
        后置处理：删除创建的教师
        """
        self.teacherAPI.delete(self.new_teacher["id"])

    @allure.story("教师管理-添加教师")
    @allure.title("当前没有教师，正常添加教师")
    @pytest.mark.addTeacher
    def test_add_teacher001(self, before_test_add_teacher001):
        """
        当前没有教师，新增教师
        :param before_test_add_teacher001:
        :return:
        """
        self.new_teacher = self.teacherAPI.add(username="数学老师",
                                               realname="王大锤",
                                               courses=self.courseInfo)
        assert self.new_teacher["retcode"] == 0

    @allure.story("教师管理-列出教师")
    @allure.title("当前没有教师，列出教师")
    @pytest.mark.listTeacher
    def test_list_teacher(self, empty_teacher):
        """
        当前没有教师，列出教师
        :param empty_teacher:
        :return:
        """
        self.teacherAPI = empty_teacher
        resp = self.teacherAPI.list()
        assert resp["retcode"] == 0 and resp["retlist"] == []

    @allure.story("教师管理-删除教师")
    @allure.title("当前没有教师，以不存在的教师id去删除教师")
    @pytest.mark.deleteTeacher
    def test_delete_teacher(self, empty_teacher):
        """
        当前没有教师，以不存在的教师id去删除教师
        :return:
        """
        self.teacherAPI = empty_teacher
        resp = self.teacherAPI.delete("5555555555")
        assert resp["retcode"] == 1 and "老师不存在" in resp["reason"]
