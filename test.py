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
from pylib.APIlib.baseAPI import BaseAPI
from pylib.APIlib.courseAPI import CourseAPI
from pylib.APIlib.loginAPI import LoginAPI
from pylib.APIlib.teacherAPI import TeacherAPI

cookie = LoginAPI().login001("auto", "sdfsdfsdf")

# ===============测试CourseAPI==============

courseAPI = CourseAPI(cookie)
info = courseAPI.add(name="大学高数")
print(info)
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
teacherApi = TeacherAPI(cookie)

# =======================列出教师=============
info = teacherApi.list()
print(info)

# ================== 添加教师 ==============
coursesInfo = courseAPI.list()["retlist"]
courseInfo = []
for course in coursesInfo:
    course_dict = {"id": course["id"], "name": course["name"]}
    courseInfo.append(course_dict)


info = teacherApi.add(username="9527-**", realname="9527-**", courses=courseInfo)
print(info)

info = teacherApi.list()
print(info)
