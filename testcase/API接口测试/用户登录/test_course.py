#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 23:47
# @File : test_course.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统账号未有课程
import allure
import pytest


class TestCourseAPI:
    """
    课程API测试
    """

    @allure.story("课程管理-列出课程")
    @allure.title("当前系统没有课程，列出课程")
    def test_list_Course001(self, empty_course):
        """
        当前系统没有课程，列出课程
        :param empty_course:
        :return:
        """
        self.courseAPI = empty_course
        course_list = self.courseAPI.list()
        assert course_list["retcode"] == 0 and course_list["total"] == 0

    @pytest.fixture()
    def before_test_add_Course001(self, empty_course):
        """
        测试添加课程前，清空课程；
        测试完成后，删除新添加的课程
        :param empty_course:
        :return:
        """
        self.courseAPI = empty_course
        yield
        self.courseAPI.delete(self.new_course["id"])

    @allure.story("课程管理-添加课程")
    @allure.title("当前系统没有课程，正常添加课程")
    def test_add_Course001(self, before_test_add_Course001):
        """
        当前系统没有课程，正常添加课程
        :return:
        """
        self.new_course = self.courseAPI.add(name="物理课",
                                             desc="初中物理课",
                                             display_idx=1)
        # 断言：返回结果retcode=0 and id 不为空
        assert self.new_course["retcode"] == 0 and self.new_course["id"] is not None


    def test_update_Course(self):
        pass

    def test_delete_Course(self):
        pass



