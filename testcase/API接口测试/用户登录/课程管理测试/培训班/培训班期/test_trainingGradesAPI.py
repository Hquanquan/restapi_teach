#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:25
# @File : test_trainingGradesAPI.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 培训班期
import allure
import pytest


@allure.epic("教管系统-接口测试")
@allure.feature("培训班期管理模块")
class TestTrainingGradesAPI:

    @pytest.fixture()
    def before_test_add_trainingGrade(self, get_trainingGradeAPI, init_training):
        self.trainingGradeAPI = get_trainingGradeAPI
        self.trainingAPI = init_training[0]
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        yield
        self.trainingGradeAPI.delete_all()

    @allure.story("培训班期管理-添加培训班期")
    @allure.title("添加培训班期")
    @pytest.mark.addTrainingGrade
    def test_add_trainingGrade(self, before_test_add_trainingGrade):
        self.new_trainingGrade = self.trainingGradeAPI.add(name="语文培训班期",
                                                           desc="语文培训班期描述",
                                                           display_idx=30,
                                                           training_id=self.training_id)
        assert self.new_trainingGrade["retcode"] == 0

    @pytest.fixture()
    def after_test_list_trainingGrade(self, init_trainingGrade):
        self.trainingGradeAPI = init_trainingGrade[0]
        yield
        self.trainingGradeAPI.delete_all()

    @allure.story("培训班期管理-列出培训班期")
    @allure.title("列出培训班期")
    @pytest.mark.listTrainingGrade
    def test_list_trainingGrade(self, after_test_list_trainingGrade):
        resp = self.trainingGradeAPI.list()
        assert resp["retcode"] == 0 and resp["retlist"] != []

    @pytest.fixture()
    def before_test_update_trainingGrade(self, init_trainingGrade):
        self.trainingGradeAPI = init_trainingGrade[0]
        self.trainingAPI = init_trainingGrade[1]
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        self.trainingGrade_id = self.trainingGradeAPI.list()["retlist"][0]["id"]
        yield
        self.trainingGradeAPI.delete_all()
        self.trainingAPI.delete_all()

    @allure.story("培训班期管理-列出培训班期")
    @allure.title("列出培训班期")
    @pytest.mark.updateTrainingGrade
    def test_update_trainingGrade(self, before_test_update_trainingGrade):
        resp = self.trainingGradeAPI.edit(self.trainingGrade_id,
                                          name="新培训班期名称",
                                          desc="新培训班期描述",
                                          display_idx=30,
                                          training_id=self.training_id)
        assert resp["retcode"] == 0

    @pytest.fixture()
    def before_test_delete_trainingGrade(self, init_trainingGrade):
        self.trainingGradeAPI = init_trainingGrade[0]
        self.trainingAPI = init_trainingGrade[1]
        self.trainingGrade_id = self.trainingGradeAPI.list()["retlist"][0]["id"]
        yield
        self.trainingAPI.delete_all()

    @allure.story("培训班期管理-删除培训班期")
    @allure.title("删除培训班期")
    @pytest.mark.deleteTrainingGrade
    def test_delete_trainingGrade(self, before_test_delete_trainingGrade):
        resp = self.trainingGradeAPI.delete(self.trainingGrade_id)
        assert resp["retcode"] == 0


