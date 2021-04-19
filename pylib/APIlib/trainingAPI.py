#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 18:40
# @Author  : 黄权权
# @File    : trainingAPI.py
# @Software: PyCharm
# @Desc    : 培训班管理api
import requests
import json
from configs.api_config import HOST
from pylib.APIlib.courseAPI import CourseAPI
from pylib.APIlib.loginAPI import LoginAPI


class TrainingAPI:
    """
    培训班管理API
    """

    def __init__(self, cookie):
        self.header = {'Cookie': cookie}

    def add_training(self, inData, courseList):
        """
        添加培训班，与课程关联
        :param inData:
        :param courseList:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        if courseList:
            inData["courselist"] = courseList
        else:
            inData["courselist"] = []
        payload = {
            "action": "add_training",
            "data": json.dumps(inData)
        }
        resp = requests.post(url, headers=self.header, data=payload)
        return resp.json()

    def list_training(self, pagenum=1, pagesize=100):
        """
        列出培训班
        :param pagenum:
        :param pagesize:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "list_training",
            "pagenum": pagenum,
            "pagesize": pagesize
        }
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()

    def edit_training(self, training_id, newdata, courselist=None):

        if courselist:
            newdata["courselist"] = courselist
        else:
            newdata["courselist"] = []

        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "modify_training",
            "id": training_id,
            "newdata": json.dumps(newdata, ensure_ascii=False)
        }
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()

    def delete_training(self, training_id):
        """
        根据training_id删除单个培训班
        :param training_id:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "delete_training",
            "id": training_id
        }
        resp = requests.delete(url, headers=self.header, data=payload)
        return resp.json()

    def delete_all_training(self):
        """
        删除第一页的全部培训班
        :return:
        """
        trainings_info = self.list_training()["retlist"]
        for training in trainings_info:
            self.delete_training(training["id"])


if __name__ == '__main__':
    # 获取cookie
    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    trainingAPI = TrainingAPI(cookie)
    course = CourseAPI(cookie)
    # ===============添加培训班==========================
    coursesInfo = course.list_course()["retlist"]
    courseInfo = []
    for course in coursesInfo:
        course_dict = {"id": course["id"], "name": course["name"]}
        courseInfo.append(course_dict)

    courseList = [courseInfo[1]]

    inData = {
        "name": "语文培训1班",
        "desc": "描述：语文培训班",
        "display_idx": "1"
    }

    info = trainingAPI.add_training(inData, courseList)
    print(info)

    # =========== 删除单一培训班=============
    # info = trainingAPI.list_training()
    # print(info)
    #
    # info = trainingAPI.delete_training(53)
    # print(info)
    #
    # info = trainingAPI.list_training()
    # print(info)
    # trainingAPI.delete_all_training()
    #
    info = trainingAPI.list_training()
    print(info)

    # ============== 编辑培训班 ================
    # trainings_info = trainingAPI.list_training()
    # training_id = trainings_info["retlist"][0]["id"]
    #
    # newdata = {
    #     "name": "数学培训1班",
    #     "desc": "初中数学培训班",
    #     "display_idx": "2"
    # }
    # info = trainingAPI.edit_training(training_id, newdata)
    # print(info)

