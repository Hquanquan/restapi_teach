#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 20:46
# @File : test.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

# ============ 测试read_yaml函数==============
# from utils.yaml_tools import read_yaml
#
# data = read_yaml("configs/api_conf.yml")
# print(data)



# =============测试BaseAPI类==================
import json

from pylib.APIlib.baseAPI import BaseAPI
from pylib.APIlib.courseAPI import CourseAPI
from pylib.APIlib.loginAPI import LoginAPI
from pylib.APIlib.teacherAPI import TeacherAPI
from pylib.APIlib.trainingAPI import TrainingAPI

cookie = LoginAPI().login001("auto", "sdfsdfsdf")

# ===============测试CourseAPI==============

courseAPI = CourseAPI(cookie)
print(courseAPI.delete("2402"))
# id = courseAPI.list()["retlist"][0]["id"]
# info = courseAPI.edit(id, name="2", desc="22")
# print(info)

# print(courseAPI.delete("459999"))


# print(json.dumps(b, ensure_ascii=False))



# info = courseAPI.add(name="大学高数")
# print(info)
# course_id = courseAPI.list()["retlist"][0]["id"]
# print(course_id)
# info = courseAPI.edit(course_id, name="newname3")
# print(info)
# info = courseAPI.delete(course_id)
# print(info)

# info = courseAPI.list()
# print(info)
# courseAPI.delete_all()
# info = courseAPI.list()
# print(info)


# ===================测试TeacherAPI=============
# 获取cookie
# teacherApi = TeacherAPI(cookie)
# info = teacherApi.list()["retlist"]
# print(info)
# info = teacherApi.list()["retlist"][0]["id"]
#
# response = teacherApi.edit(info, username="数学老师", realname="李三")
# print(response)
# =======================列出教师=============
# info = teacherApi.list()
# print(info)

# ================== 添加教师 ==============
# coursesInfo = courseAPI.list()["retlist"]
# courseInfo = []
# for course in coursesInfo:
#     course_dict = {"id": course["id"], "name": course["name"]}
#     courseInfo.append(course_dict)

# 添加
# info = teacherApi.add(username="9527-*1*", realname="9527-**", courses=courseInfo)
# print(info)
#
# info = teacherApi.list()
# print(info)

# 删除
# teacher_id = teacherApi.list()["retlist"][0]["id"]
# info = teacherApi.delete(teacher_id)
# print(info)
# info = teacherApi.list()
# print(info)

# 修改
# teacher_id = teacherApi.list()["retlist"][0]["id"]
# info = teacherApi.edit(teacher_id,
#                        username="历史老师",
#                        password="123456",
#                        realname="李政",
#                        courses=courseInfo)
#
# info = teacherApi.list()
# print(info)

# =================培训班=====================

# coursesInfo = courseAPI.list()["retlist"]
# courseInfo = []
# i = 0
# for course in coursesInfo:
#     course_dict = {"id": course["id"], "name": course["name"]}
#     courseInfo.append(course_dict)
#     i = i + 1
#     if i == 3:
#         break
# # 非常关键，把列表转换换json字符串
# courseList = json.dumps(courseInfo, ensure_ascii=False)
# print(courseList)
#
#
# trainingAPI = TrainingAPI(cookie)

# # 列出培训班
# info = trainingAPI.list()
# print(info)

# # 添加培训班
# info = trainingAPI.add(name="语文培训22班",
#                        desc="语文培训班22",
#                        display_idx=102,
#                        courselist=courseList)
# print(info)


# 修改培训班
# training_id = trainingAPI.list()["retlist"][0]["id"]
#
# info = trainingAPI.edit(training_id,
#                         name="语文培训3班",
#                         desc="语文培训班3",
#                         display_idx=102,
#                         courselist=[])
# print(info)



# info = trainingAPI.delete(training_id)
# print(info)
#
# print(trainingAPI.list())

# b = {'retcode': 0, 'retlist': [{'id': 2160, 'name': '大学英语158973986548', 'desc': '大学英语课程', 'display_idx': 0}], 'total': 16}
# c = json.dumps(b, ensure_ascii=False)
# print(type(c))

