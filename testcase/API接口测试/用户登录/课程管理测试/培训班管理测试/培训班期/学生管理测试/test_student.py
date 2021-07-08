#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 10:25
# @File : test_student.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

import allure
import pytest


@allure.epic("教管系统-接口测试")
@allure.feature("学生管理模块")
class TestStudentAPI:

    @pytest.fixture()
    def before_test_add_student(self, get_studentAPI, init_trainingGrade):
        self.studentAPI = get_studentAPI
        self.trainingGradeAPI = init_trainingGrade[0]
        self.trainingAPI = init_trainingGrade[1]
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        self.trainingGrade_id = self.trainingGradeAPI.list()["retlist"][0]["id"]
        yield
        self.studentAPI.delete(self.new_student["id"])
        self.trainingGradeAPI.delete_all()

    @allure.story("学生管理-添加学生")
    @allure.title("添加学生")
    @pytest.mark.addStudent
    def test_add_student(self, before_test_add_student):
        self.new_student = self.studentAPI.add(username="小明",
                                               realname="王小明",
                                               desc="学生王小明的描述信息",
                                               # "password": "123456",
                                               # "startcoursedate": "2021-02-15T07:50:53.345Z",
                                               training_id=self.training_id,
                                               traininggrade_id=self.trainingGrade_id)
        assert self.new_student["retcode"] == 0

    @pytest.fixture()
    def after_test_list_student(self, init_student):
        self.studentAPI = init_student[0]
        self.trainingGradeAPI = init_student[1]
        self.new_student_id = init_student[3]["id"]
        yield
        self.studentAPI.delete(self.new_student_id)
        self.trainingGradeAPI.delete_all()


    @allure.story("学生管理-列出学生")
    @allure.title("列出学生")
    @pytest.mark.listStudent
    def test_list_student(self, after_test_list_student):
        """
        列出学生
        :param after_test_list_student:
        :return:
        """
        resp = self.studentAPI.list()
        assert resp["retcode"] == 0 and resp["total"] != 0

    @pytest.fixture()
    def before_test_update_student(self, init_student):
        self.studentAPI = init_student[0]
        self.trainingGradeAPI = init_student[1]
        self.trainingAPI = init_student[2]
        self.new_student_id = init_student[3]["id"]
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        self.trainingGrade_id = self.trainingGradeAPI.list()["retlist"][0]["id"]
        yield
        self.studentAPI.delete(self.new_student_id)
        self.trainingGradeAPI.delete_all()

    @allure.story("学生管理-编辑修改学生")
    @allure.title("编辑修改学生")
    @pytest.mark.updateStudent
    def test_update_student(self, before_test_update_student):
        """
        编辑修改学生
        :param before_test_update_student:
        :return:
        """
        resp = self.studentAPI.edit(self.new_student_id,
                                    username="李拉三",
                                    realname="李四",
                                    training_id=self.training_id,
                                    traininggrade_id=self.trainingGrade_id)
        assert resp["retcode"] == 0

    @pytest.fixture()
    def before_test_delete_student(self, init_student):
        self.studentAPI = init_student[0]
        self.trainingGradeAPI = init_student[1]
        self.new_student_id = init_student[3]["id"]
        yield
        self.trainingGradeAPI.delete_all()

    @allure.story("学生管理-删除学生")
    @allure.title("删除学生")
    @pytest.mark.deleteStudent
    def test_delete_student(self, before_test_delete_student):
        """
        删除学生
        :param before_test_delete_student:
        :return:
        """
        resp = self.studentAPI.delete(self.new_student_id)
        assert resp["retcode"] == 0


