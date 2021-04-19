#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 23:22
# @Author  : 黄权权
# @File    : studentAPI.py
# @Software: PyCharm
# @Desc    : 学生管理api

import requests
import json

from configs.api_config import HOST
from pylib.APIlib.loginAPI import LoginAPI
from pylib.APIlib.trainingAPI import TrainingAPI
from pylib.APIlib.training_gradeAPI import TrainingGradeAPI


class StudentAPI:
    """
    学生管理API
    """

    def __init__(self, cookie):
        self.header = {'Cookie': cookie}

    def list_student(self, pagenum=1, pagesize=20):
        """
        列出学生
        :param pagenum:
        :param pagesize:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "list_student",
            "pagenum": pagenum,
            "pagesize": pagesize
        }
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()

    def add_student(self, inData):
        """
        添加学生，与培训班，培训班期关联
        :param inData:
            indata = {
            "username": "学生002",
            "realname": "学生真实名字002",
            "desc": "学生信息",
            "password": "123456",
            "startcoursedate": "2021-04-12T07:50:53.345Z",
            "training_id": training_id,
            "traininggrade_id": traininggrade_id
            }
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "add_student",
            "data": json.dumps(inData, ensure_ascii=False)
        }
        resp = requests.post(url, headers=self.header, data=payload)
        return resp.json()

    def edit_student(self, student_id, newdata):
        """
        修改学生信息
        :param student_id:
        :param newdata:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "modify_student",
            "id": student_id,
            "newdata": json.dumps(newdata, ensure_ascii=False)
        }
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()

    def delete_student(self, student_id):
        """
        单个删除学生信息
        :param student_id:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "delete_student",
            "id": student_id
        }
        resp = requests.delete(url, headers=self.header, data=payload)
        return resp.json()

    def delete_all_student(self):
        """
        批量删除第一页所有的学生信息
        :return:
        """
        students = self.list_student()["retlist"]
        for student in students:
            self.delete_student(student["id"])

    def update_password(self, uid):
        """
        修改学生登录密码
        :param uid:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "changeuserpassword",
            "uid": uid
        }
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()


if __name__ == '__main__':
    # 获取cookie
    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    trainingAPI = TrainingAPI(cookie)
    training_id = trainingAPI.list_training()["retlist"][0]["id"]
    traininggradeAPI = TrainingGradeAPI(cookie)
    traininggrade_id = traininggradeAPI.list_training_grade()["retlist"][0]["id"]
    studentAPI = StudentAPI(cookie)
    # ============= 列出学生 ==============
    students_info = studentAPI.list_student()
    print(students_info)

    # ============== 添加学生 ============================
    # indata = {
    #     "username": "学生002",
    #     "realname": "学生真实名字002",
    #     "desc": "学生信息",
    #     "password": "123456",
    #     "startcoursedate": "2021-04-12T07:50:53.345Z",
    #     "training_id": training_id,
    #     "traininggrade_id": traininggrade_id
    # }
    # info = studentAPI.add_student(indata)
    # print(info)
    #
    # ================== 修改学生信息 =========
    student_id = studentAPI.list_student()["retlist"][0]["id"]
    newdata = {
        "username": "学生0012",
        "realname": "真实名字0012",
        "desc": "学生信息",
        "password": "123456",
        "startcoursedate": "2021-04-12T07:50:53.345Z",
        "graduated": True,
        "training_id": training_id,
        "traininggrade_id": traininggrade_id
    }
    info = studentAPI.edit_student(student_id, newdata)
    print(info)

    # ================单个删除学生信息====================
    # student_id = studentAPI.list_student()["retlist"][0]["id"]
    # info = studentAPI.delete_student(student_id)
    # print(info)
    #
    # students_info = studentAPI.list_student()
    # print(students_info)

    # =================批量删除学生===================================
    # studentAPI.delete_all_student()
    # students_info = studentAPI.list_student()
    # print(students_info)

    # =============== 修改学生密码 ==============
    student_id = studentAPI.list_student()["retlist"][0]["userid"]
    info = studentAPI.update_password(student_id)
    print(info)

    print(studentAPI.list_student())
