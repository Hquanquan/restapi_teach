#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 20:00
# @Author  : 黄权权
# @File    : lessonAPI.py
# @Software: PyCharm
# @Desc    : 课时管理api
import json
import requests
from configs.api_config import HOST
from pylib.APIlib.loginAPI import LoginAPI
from pylib.APIlib.courseAPI import CourseAPI


class LessonAPI:
    """
    课时管理API
    """

    def __init__(self, cookie):
        self.header = {'Cookie': cookie}

    def list_lesson(self, pagenum=1, pagesize=20):
        """
        列出课时
        :param pagenum:
        :param pagesize:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "list_lesson",
            "pagenum": pagenum,
            "pagesize": pagesize
        }
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()

    def add_lesson(self, inDate):
        """
        添加课时，与课程关联
        :param inDate:
            inData = {
                "course_id": 2172,
                "starttime": "2021-04-10T16:00:00.000Z",
                "endtime": "2021-04-24T16:00:00.000Z",
                "desc": "课时"
            }
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "add_lesson",
            "data": json.dumps(inDate, ensure_ascii=False)
        }
        resp = requests.post(url, headers=self.header, data=payload)
        return resp.json()

    def edit_lesson(self, lesson_id, newdata):
        """
        编辑课时
        :param lesson_id:
        :param newdata:
        :return:
        """
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "modify_lesson",
            "id": lesson_id,
            "newdata": json.dumps(newdata, ensure_ascii=False)
        }
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()

    def delete_lesson(self, lesson_id):
        url = f"{HOST}/api/mgr/sq_mgr/"
        payload = {
            "action": "delete_lesson",
            "id": lesson_id
        }
        resp = requests.delete(url, headers=self.header, data=payload)
        return resp.json()

    def delete_all_lesson(self):
        """
        删除第一页所有的课时
        :return:
        """
        lessons = self.list_lesson()["retlist"]
        for lesson in lessons:
            self.delete_lesson(lesson["id"])




if __name__ == '__main__':
    # 获取cookie
    cookie = LoginAPI().login001("auto", "sdfsdfsdf")
    lessonAPI = LessonAPI(cookie)
    # 课程列表第一个课程的id
    course_id = CourseAPI(cookie).list_course()["retlist"][0]["id"]

    lesson_info = lessonAPI.list_lesson()
    # 课时列表第一个课时的id
    lesson_id = lesson_info["retlist"][0]["id"]

    #  ============列出课时=============
    # lesson_info = lessonAPI.list_lesson()
    # print(lesson_info)

    # ================ 添加课时 ==============

    # inData = {
    #     "course_id": course_id,
    #     "starttime": "2021-04-10T16:00:00.000Z",
    #     "endtime": "2021-04-24T16:00:00.000Z",
    #     "desc": "课时"
    # }
    # info = lessonAPI.add_lesson(inData)
    # print(info)

    # ============= 编辑课时 =============
    # inData = {
    #     "course_id": course_id,
    #     "starttime": "2021-04-10T16:00:00.000Z",
    #     "endtime": "2021-04-24T16:00:00.000Z",
    #     "desc": "英文课时1"
    # }
    #
    # info = lessonAPI.edit_lesson(lesson_id, inData)
    # print(info)

    # =========== 删除课时==============
    # lesson_info = lessonAPI.list_lesson()
    # print(lesson_info)
    # info = lessonAPI.delete_lesson(lesson_id)
    # print(info)
    # lesson_info = lessonAPI.list_lesson()
    # print(lesson_info)

    # ============批量删除课时==================
    # lesson_info = lessonAPI.list_lesson()
    # print(lesson_info)
    # lessonAPI.delete_all_lesson()
    # lesson_info = lessonAPI.list_lesson()
    # print(lesson_info)
