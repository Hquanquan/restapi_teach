#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 23:52
# @File : test_courses.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有课程
import pytest
import allure

from pylib.APIlib.courseAPI import CourseAPI


class TestCourseAPI:
    """
    课程API测试
    """

    @pytest.mark.addCourse
    @allure.story("课程管理-列出课程")
    @allure.title("当前已有课程，正常列出课程")
    # @pytest.mark.skip("暂不执行")
    def test_list_Course002(self, init_course):
        """
        当前已有课程，列出课程信息，预期正常列出数据
        :return:
        """
        self.courseAPI = init_course[0]
        courses = self.courseAPI.list()
        assert courses["retcode"] == 0 and courses["total"] != 0

    @pytest.fixture()
    def brfore_test_add_Course002(self, init_course):
        self.courseAPI = init_course[0]
        yield

    @allure.story("课程管理-添加课程")
    @allure.title("当前已有课程，添加信息完全重复的课程")
    # @pytest.mark.skip("暂不执行")
    def test_add_Course002(self, brfore_test_add_Course002):
        """
        添加重复课程，预期结果添加失败
        :return:
        """
        resp = self.courseAPI.add(name="物理课",
                                  desc="初中物理课",
                                  display_idx=1)
        assert resp["retcode"] == 2 and resp["reason"] == "同名课程存在"

    @pytest.fixture()
    def before_test_add_Course003(self, init_course):
        self.courseAPI = init_course[0]
        yield

    @pytest.mark.addCourse
    @allure.story("课程管理-添加课程")
    @allure.title("当前已有课程，添加课程名称已存在系统，其他信息随意填写")
    def test_add_Course003(self, before_test_add_Course003):
        """
        当前已有课程，添加课程名称已存在系统，其他信息随意填写,预期结果添加课程失败
        :param before_test_add_Course003:
        :return:
        """
        resp = self.courseAPI.add(name="物理课",
                                  desc="高中物理课程",
                                  display_idx=3)
        assert resp["retcode"] == 2 and resp["reason"] == "同名课程存在"

    @pytest.fixture()
    def before_test_update_Course001(self, init_course):
        """
        步骤
        1、新建课程
        2、测试更新课程
        3、删除该测试数据
        """
        self.courseAPI = init_course[0]
        self.course = init_course[1]
        yield
        self.courseAPI.delete(self.course["id"])

    @allure.story("课程管理-编辑更新课程")
    @allure.title("修改课程所有信息，课程名不重复")
    @pytest.mark.updateCourse
    def test_update_Course001(self, before_test_update_Course001):
        resp = self.courseAPI.edit(self.course["id"],
                                   name="数学",
                                   desc="高中物理课描述",
                                   display_idx=3)
        assert resp["retcode"] == 9999


