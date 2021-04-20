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
from pylib.APIlib.baseAPI import BaseAPI, CourseAPI
from pylib.APIlib.loginAPI import LoginAPI
cookie = LoginAPI().login001("auto", "sdfsdfsdf")

baseApi = BaseAPI(cookie)
baseApi.add()


courseAPI = CourseAPI(cookie)
# info = courseAPI.add()
# print(info)
course_id = courseAPI.list()["retlist"][0]["id"]
print(course_id)
# info = courseAPI.edit(course_id, name="newname1")
# print(info)
info = courseAPI.delete(course_id)
print(info)