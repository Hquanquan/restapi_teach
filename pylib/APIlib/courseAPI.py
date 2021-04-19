#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 10:48
# @File : courseAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 课程管理API
import json

from configs.api_config import HOST
import requests

from pylib.APIlib.loginAPI import LoginAPI


class CourseAPI:
    """
    课程管理API
    """

    def __init__(self, cookie):
        self.header = {'Cookie': cookie}  # 请求头

    def add_course_json(self, inData):
        """
        json格式添加课程
        :param inData:  字典格式数据
            {
                 "name": "高数",
                 "desc": "大学课程高数",
                 "display_idx": "999"
            }
        :return:
        """
        url = f"{HOST}/apijson/mgr/sq_mgr/"
        self.header["Content-Type"] = "application/json"
        payload = {"action": "add_course_json", "data": inData}
        resp = requests.post(url, headers=self.header, json=payload)
        return resp.json()

    def add_course(self, inData):
        """
        添加课程
        :param inData: 字典格式数据
            {
                 "name": "高数",
                 "desc": "大学课程高数",
                 "display_idx": "999"
            }
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        # json.dumps(inData, ensure_ascii=False) 把字典转换成json字符串，ensure_ascii=False避免编码乱码
        payload = {"action": "add_course", "data": json.dumps(inData, ensure_ascii=False)}
        resp = requests.post(url, headers=self.header, data=payload)
        return resp.json()

    def list_course(self, pagenum=1, pagesize=20):
        """
        列出指定页码，条数的课程信息，默认第1页，每页20条
        :param pagenum:页码
        :param pagesize:每页条数
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {"action": "list_course", "pagenum": pagenum, "pagesize": pagesize}
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()

    def edit_course(self, course_id, newdata):

        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {"action": "modify_course",
                   "id": course_id,
                   "newdata": json.dumps(newdata, ensure_ascii=False)
                   }

        resp = requests.put(url, data=payload, headers=self.header)
        if resp.status_code == "200":
            return resp.json()
        return resp

    def delete_course(self, course_id):
        """
        删除单个课程
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {"action": "delete_course", "id": course_id}
        resp = requests.delete(url, headers=self.header, data=payload)
        return resp.json()

    def delete_all_course(self):
        """
        删除第一页全部课程
        :return:
        """
        # 课程全部信息
        courses = self.list_course()["retlist"]
        for course in courses:
            self.delete_course(course["id"])


if __name__ == '__main__':
    # 获取cookie
    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    # 实例化courseAPI对象为course
    course = CourseAPI(cookie)

    # ===================列出课程：页码1，每页20条======================
    info = course.list_course()
    print(info)

    # ================添加课程=============
    # indata1 = {
    #     "name": "高数",
    #     "desc": "大学课程高数",
    #     "display_idx": "999"
    # }
    # indata = json.loads(indata1)
    # print(type(indata1))
    # info = course.add_course(indata1)
    # print(info)

    # ===========编辑课程=============
    # 获取课程列表的第一个课程id
    # info = course.list_course()
    # course_id = info["retlist"][0]["id"]
    # newdata = {
    #     "name": "初中化学11",
    #     "desc": "初中课程",
    #     "display_idx": "55"
    # }
    # info = course.edit_course(course_id, newdata)
    # print(info)

    # =========删除课程===========
    # 获取课程列表的第一个课程id
    # info = course.list_course()
    # course_id = info["retlist"][0]["id"]
    # info = course.delete_course(course_id)
    # print(info)

    # 删除第一页全部课程
    # course.delete_all_course()
    # info = course.list_course()
    # print(info)

    # ================ 添加课程 json===============
    # indata1 = {
    #         "name": "高数",
    #         "desc": "大学课程高数",
    #         "display_idx": "999"
    #     }
    # info = course.add_course_json(indata1)
    # print(info)

