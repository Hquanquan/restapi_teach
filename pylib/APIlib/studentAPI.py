#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 10:08
# @File : studentAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 学生管理API
import copy

import requests

from pylib.APIlib.baseAPI import BaseAPI


class StudentAPI(BaseAPI):

    def updatePassword(self, uid):
        """
        修改学生登录密码
        :param uid:
        :return:
        """
        data = copy.deepcopy(self.conf["updatePassword"])
        data["uid"] = uid
        payload = data
        url = self.host + self.path
        resp = requests.put(url, headers=self.header, data=payload)
        return resp.json()




