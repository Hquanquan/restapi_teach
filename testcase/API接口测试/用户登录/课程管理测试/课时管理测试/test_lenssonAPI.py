#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 22:49
# @File : test_lenssonAPI.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 课时管理测试
import allure
import pytest

from utils.time_tools import get_CurrentTime


@allure.epic("教管系统-接口测试")
@allure.feature("课时管理模块")
class TestLenssonAPI:

    @pytest.fixture()
    def before_test_add_lesson(self, get_lessonAPI, init_course):
        self.lessonAPI = get_lessonAPI
        self.course_id = init_course[1]["id"]
        yield
        self.lessonAPI.delete_all()

    @pytest.mark.addLesson
    @allure.story("课时管理-添加课时")
    @allure.title("添加课时")
    def test_add_lesson(self, before_test_add_lesson):
        """
        添加课时
        :param before_test_add_lesson:
        :return:
        """
        resp = self.lessonAPI.add(course_id=self.course_id,
                                  starttime=get_CurrentTime(),
                                  # "endtime": "2023-12-31T23:00:00.000Z",  默认使用这个
                                  desc="课时描述")
        assert resp["retcode"] == 0

    @pytest.fixture()
    def after_test_list_lesson(self, init_lesson):
        self.lessonAPI = init_lesson[0]
        yield
        self.lessonAPI.delete_all()

    @pytest.mark.listLesson
    @allure.story("课时管理-列出课时")
    @allure.title("列出课时")
    def test_list_lesson(self, after_test_list_lesson):
        resp = self.lessonAPI.list()
        print(resp)
        assert resp["retcode"] == 0 and resp["total"] != 0

    @pytest.fixture()
    def before_test_edit_lesson(self, init_lesson):
        self.lessonAPI = init_lesson[0]
        self.lesson_id = self.lessonAPI.list()["retlist"][0]["id"]
        self.course_id = self.lessonAPI.list()["retlist"][0]["course_id"]
        yield
        self.lessonAPI.delete_all()

    @pytest.mark.updateLesson
    @allure.story("课时管理-编辑修改课时")
    @allure.title("编辑修改课时")
    def test_edit_lesson(self, before_test_edit_lesson):
        print(self.lesson_id)
        print(self.course_id)
        resp = self.lessonAPI.edit(self.lesson_id,
                                   course_id=self.course_id,
                                   starttime=get_CurrentTime(),
                                   # "endtime": "2023-12-31T23:00:00.000Z",  默认使用这个
                                   desc="新课时描述")

        assert resp["retcode"] == 0

    @pytest.fixture()
    def before_test_delete_lesson(self, init_lesson):
        self.lessonAPI = init_lesson[0]
        self.lesson_id = self.lessonAPI.list()["retlist"][0]["id"]
        yield

    @pytest.mark.deleteLesson
    @allure.story("课时管理-删除课时")
    @allure.title("删除课时")
    def test_delete_lesson(self, before_test_delete_lesson):
        resp = self.lessonAPI.delete(self.lesson_id)
        assert resp["retcode"] == 0

