#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 22:22
# @File : test_trainings.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import allure
import pytest


@allure.epic("教管系统-接口测试")
@allure.feature("培训班管理模块")
class TestTrainingAPI:

    @pytest.fixture()
    def after_test_list_training(self, init_training):
        self.trainingAPI = init_training[0]
        yield
        self.trainingAPI.delete(self.training_id)

    @allure.story("培训班管理-列出培训班")
    @allure.title("列出培训班")
    @pytest.mark.listTraining
    def test_list_training(self, after_test_list_training):
        """
        列出培训班
        :return:
        """
        resp = self.trainingAPI.list()
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        assert resp["retcode"] == 0 and resp["total"] != 0

    @pytest.fixture()
    def before_test_update_training(self, init_training, init_course):
        """
        前置条件：1、创建一个培训班
                2、获取到列表中的第一个培训班id
        """
        self.trainingAPI = init_training[0]
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        yield
        """后置处理：删除培训班"""
        self.trainingAPI.delete(self.training_id)

    @allure.story("培训班管理-修改培训班")
    @allure.title("修改培训班")
    @pytest.mark.editTraining
    def test_update_training(self, before_test_update_training):
        """
        修改培训班
        :param before_test_update_training:
        :return:
        """
        resp = self.trainingAPI.edit(self.training_id,
                                     name="语文培训3班",
                                     desc="语文培训班3",
                                     display_idx=103,
                                     courselist=[]
                                     )
        assert resp["retcode"] == 0

    @pytest.fixture()
    def before_test_delete_training(self, init_training):
        self.trainingAPI = init_training[0]
        self.training_id = self.trainingAPI.list()["retlist"][0]["id"]
        yield

    @allure.story("培训班管理-删除培训班")
    @allure.title("删除培训班")
    @pytest.mark.deleteTraining
    def test_delete_training(self, before_test_delete_training):
        """
        删除培训班
        :return:
        """
        resp = self.trainingAPI.delete(self.training_id)
        assert resp["retcode"] == 0
