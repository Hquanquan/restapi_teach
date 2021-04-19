#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 12:44
# @File : training_gradeAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 培训班期管理api
import json
import requests
from configs.api_config import HOST
from pylib.APIlib.loginAPI import LoginAPI
from pylib.APIlib.trainingAPI import TrainingAPI

class TrainingGradeAPI:
    """
    培训班期管理API
    """

    def __init__(self,cookie):
        # 请求头添加cookie
        self.header = {"Cookie": cookie}

    def list_training_grade(self, pagenum=1, pagesize=20):
        """
        列出培训班期
        :param pagenum:
        :param pagesize:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "list_training_grade",
            "pagenum": pagenum,
            "pagesize": pagesize
        }
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()

    def add_training_grade(self, inData):
        """
        添加培训班期，与培训班关联
        :param inData:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "add_training_grade",
            "data": json.dumps(inData, ensure_ascii=False)
        }
        resp = requests.post(url, headers=self.header, data=payload)
        return resp.json()

    def edit_training_grade(self, training_grade_id, newdata):
        """
        修改培训班期
        :param training_grade_id:
        :param newdata:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "modify_training_grade",
            "id": training_grade_id,
            "newdata": json.dumps(newdata, ensure_ascii=False)
        }
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()

    def delete_training_grade(self, training_grade_id):
        """
        单个删除培训班期
        :param training_grade_id:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "delete_training_grade",
            "id": training_grade_id
        }
        resp = requests.delete(url, headers=self.header, data=payload)
        return resp.json()

    def delete_all_training_grade(self):
        """
        批量删除第一页的所有培训班期
        :return:
        """
        training_grades_info = self.list_training_grade()["retlist"]
        for training_grade_info in training_grades_info:
            self.delete_training_grade(training_grade_info["id"])


if __name__ == '__main__':

    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    trainingAPI = TrainingAPI(cookie)
    # 培训班列表第一个培训班的id
    training_id = trainingAPI.list_training()["retlist"][0]["id"]

    trainingGradeAPI = TrainingGradeAPI(cookie)
    # =================列出培训班期============
    info = trainingGradeAPI.list_training_grade()
    print(info)

    # ==================添加培训班期===================
    # indate = {
    #     "name": "语文培训班2期",
    #     "desc": "语文培训班2期",
    #     "display_idx": 2,
    #     "training_id": training_id
    # }
    # info = trainingGradeAPI.add_training_grade(indate)
    # print(info)

    # ==============编辑培训班期================
    # training_grade_id = trainingGradeAPI.list_training_grade()["retlist"][0]["id"]
    # newdata = {
    #     "name": "培训班期",
    #     "desc": "描述培训班期",
    #     "display_idx": 3,
    #     "training_id": training_id
    # }
    # info = trainingGradeAPI.edit_training_grade(training_grade_id, newdata)
    # print(info)

    # =============== 删除培训班期 =================
    # training_grade_id = trainingGradeAPI.list_training_grade()["retlist"][0]["id"]
    # info = trainingGradeAPI.delete_training_grade(training_grade_id)
    # print(info)
    #
    # info = trainingGradeAPI.list_training_grade()
    # print(info)

    # =================== 批量删除培训班期 ================
    trainingGradeAPI.delete_all_training_grade()
    info = trainingGradeAPI.list_training_grade()
    print(info)




