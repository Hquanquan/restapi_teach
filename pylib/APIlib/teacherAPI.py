#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 17:23
# @File : teacherAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 教师管理API
import requests

from configs.api_config import HOST
import json

from pylib.APIlib.courseAPI import CourseAPI
from pylib.APIlib.loginAPI import LoginAPI


class TeacherAPI:
    """
    教师管理API
    """

    def __init__(self, cookie):
        # 请求头添加cookie
        self.header = {"Cookie": cookie}

    def add_teacher(self, inData, course_info):
        """
        添加教师,关联着课程信息
        :param inData:
        :param course_info:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        inData["courses"] = course_info
        payload = {
            "action": "add_teacher",
            "data": json.dumps(inData, ensure_ascii=False)
        }
        resp = requests.post(url, headers=self.header, data=payload)
        return resp.json()

    def list_teacher(self, pagenum=1, pagesize=20):
        """
        列出教师
        :param pagenum:
        :param pagesize:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "list_teacher",
            "pagenum": pagenum,
            "pagesize": pagesize,
        }
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()

    def edit_teacher(self, teacher_id, newdata, course_info=None):
        url = f"{HOST}/api/mgr/sq_mgr/"
        if course_info:
            newdata["courses"] = course_info
        else:
            newdata["courses"] = []
        payload = {
            "action": "modify_teacher",
            "id": teacher_id,
            "newdata": json.dumps(newdata, ensure_ascii=False)
        }
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()

    def delete_teacher(self, teacher_id):
        """
        单个删除教师
        :param teacher_id:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "delete_teacher",
            "id": teacher_id
        }
        resp = requests.delete(url, headers=self.header, data=payload)
        return resp.json()

    def delete_all_teacher(self):
        """
        批量删除教师
        :return:
        """
        # 课程全部信息
        teachers_info = self.list_teacher()["retlist"]
        for teacher in teachers_info:
            self.delete_teacher(teacher["id"])


if __name__ == '__main__':
    # 获取cookie
    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    teacherApi = TeacherAPI(cookie)
    course = CourseAPI(cookie)
    # =======================添加教师=============
    coursesInfo = course.list_course()["retlist"]
    courseInfo = []
    for course in coursesInfo:
        course_dict = {"id": course["id"], "name": course["name"]}
        courseInfo.append(course_dict)
        # print(courseInfo)
    #
    # indata = {
    #     "username": "user0002",
    #     "password": "123456",
    #     "realname": "realname002",
    #     "desc": "描述字段",
    #     "display_idx": 1
    # }
    # info = teacherApi.add_teacher(indata, courseInfo)
    # print(info)

    teacher_info = teacherApi.list_teacher()
    print(teacher_info)

    t_id = teacher_info["retlist"][0]["id"]
    # newdata = {
    #     "username": "user001",
    #     "password": "123456",
    #     "realname": "realname001"
    # }
    # info = teacherApi.edit_teacher(t_id, newdata)
    # print(info)

    teacherApi.delete_all_teacher()
    print(info)
    teacher_info = teacherApi.list_teacher()
    print(teacher_info)
