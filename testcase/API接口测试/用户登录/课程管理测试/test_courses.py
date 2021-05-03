#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 23:52
# @File : test_courses.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有课程
import pytest
import allure


@allure.epic("教管系统-接口测试")
@allure.feature("课程管理模块")
class TestCourseAPI:
    """
    课程API测试
    """

    @pytest.mark.addCourse
    @allure.story("课程管理-列出课程")
    @allure.title("当前已有课程，正常列出课程")
    def test_list_Course002(self, init_course):
        """
        当前已有课程，列出课程信息，预期正常列出数据
        :return:
        """
        self.courseAPI = init_course[0]
        courses = self.courseAPI.list()
        assert courses["retcode"] == 0 and courses["total"] != 0


    @allure.story("课程管理-添加课程")
    @allure.title("当前已有课程，添加信息完全重复的课程")
    def test_add_Course002(self, init_course):
        """
        添加重复课程，预期结果添加失败
        :return:
        """
        self.courseAPI = init_course[0]
        resp = self.courseAPI.add(name="物理课",
                                  desc="初中物理课",
                                  display_idx=1)
        assert resp["retcode"] == 2 and resp["reason"] == "同名课程存在"

    @pytest.mark.addCourse
    @allure.story("课程管理-添加课程")
    @allure.title("当前已有课程，添加课程名称已存在系统，其他信息随意填写")
    def test_add_Course003(self, init_course):
        """
        当前已有课程，添加课程名称已存在系统，其他信息随意填写,预期结果添加课程失败
        :param init_course:
        :return:
        """
        self.courseAPI = init_course[0]
        resp = self.courseAPI.add(name="物理课",
                                  desc="高中物理课程",
                                  display_idx=3)
        assert resp["retcode"] == 2 and resp["reason"] == "同名课程存在"

    @allure.story("课程管理-修改课程")
    @allure.title("修改课程所有信息，课程名不重复")
    @pytest.mark.updateCourse
    def test_update_Course001(self, init_course):
        """
        修改课程所有信息，课程名不重复，预期结果修改成功
        :param init_course:
        :return:
        """
        self.courseAPI = init_course[0]
        self.course = init_course[1]
        resp = self.courseAPI.edit(self.course["id"],
                                   name="高中物理课",
                                   desc="高中物理课描述",
                                   display_idx=3)
        assert resp["retcode"] == 0

    @pytest.fixture()
    def before_test_update_Course002(self, init_course):
        self.courseAPI = init_course[0]
        self.course = init_course[1]
        self.new_course = self.courseAPI.add(name="数学课",
                                             desc="初中数学",
                                             display_idx=5)
        yield
        self.courseAPI.delete(self.new_course["id"])

    @allure.story("课程管理-修改课程")
    @allure.title("修改重复的课程名，其他随意")
    @pytest.mark.updateCourse
    def test_update_Course002(self, before_test_update_Course002):
        """
        修改课程名称为系统已存在的课程名，其他随意，预期结果修改失败.接口报500
        :param before_test_update_Course002:
        :return:
        """
        resp = self.courseAPI.edit(self.new_course["id"],
                                   name="数学课",
                                   desc="高中数学",
                                   display_idx=5)
        assert resp["retcode"] == 0

    @allure.story("课程管理-修改课程")
    @allure.title("以不存在的课程id去修改课程")
    @pytest.mark.updateCourse
    def test_update_Course003(self, init_course):
        """
        修改课程，以不存在的课程id去修改课程，预期结果修改失败
        :param init_course:
        :return:
        """
        self.courseAPI = init_course[0]
        resp = self.courseAPI.edit("courseID",
                                   name="数学课",
                                   desc="高中数学",
                                   display_idx=5)
        assert resp["retcode"] == 9999

    @allure.story("课程管理-删除课程")
    @allure.title("正常删除系统中已存在的课程")
    # @pytest.mark.skip("暂不执行")
    @pytest.mark.deleteCourse
    def test_delete_course001(self, init_course_to_delete):
        """
        删除系统中已存在的课程
        :param init_course_to_delete:
        :return:
        """
        self.courseAPI = init_course_to_delete[0]
        course = init_course_to_delete[1]
        resp = self.courseAPI.delete(course["id"])
        assert resp["retcode"] == 0

    @allure.story("课程管理-删除课程")
    @allure.title("删除系统中不存在的课程")
    @pytest.mark.deleteCourse
    # @pytest.mark.skip("暂不执行")
    def test_delete_course002(self, init_course_to_delete):
        """
        删除系统中不存在的课程,课程id不存在，预期结果删除失败
        :param init_course_to_delete:
        :return:
        """
        self.courseAPI = init_course_to_delete[0]
        resp = self.courseAPI.delete("02135558455")
        assert resp["retcode"] == 0
