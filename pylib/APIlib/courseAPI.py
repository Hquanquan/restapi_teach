#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 23:30
# @File : courseAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : CourseAPI 继承BaseAPI类
import copy
import json

import requests

from pylib.APIlib.baseAPI import BaseAPI
from pylib.APIlib.loginAPI import LoginAPI


class CourseAPI(BaseAPI):

    def add(self, **kwargs):
        """
        添加
        :param kwargs: 字典类型的参数
        :return:
        """

        # 读取配置文件模板中-add的内容
        # data = self.conf["add"]  这样有问题
        # 深度拷贝，避免data与self.cong["add"]共用对同一地址
        data = copy.deepcopy(self.conf["add"])
        # 判断data字典是否为空，不为空则执行下面的语句。为空则跳过
        if bool(data):
            # 把字典类型的参数更新到data中
            data["data"].update(kwargs)
            # 把data["data"]字典转换成json字符串
            data["data"] = json.dumps(data["data"], ensure_ascii=False)
        payload = data
        url = self.host + self.path
        resp = requests.post(url, data=payload, headers=self.header)
        if resp.status_code == 200:
            return resp.json()
        else:
            return "接口返回错误!!!"




