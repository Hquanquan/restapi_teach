#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 20:27
# @File : baseAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : API基类，实现基本的CRUD增删改查功能，用于被业务api类继承
import copy
import json

from configs.api_env import HOST
from utils.yaml_tools import read_yaml
import requests


class BaseAPI:

    def __init__(self, cookie):
        # cookie 信息，在登录接口获取
        self.header = {"cookie": cookie}
        # 测试接口的URL
        self.host = HOST
        # 接口数据模板文件的相对路径
        filePath = "configs/api_conf.yml"
        # 自定义 读取yaml文件内容 函数
        api_template = read_yaml(filePath)
        # 获取当前类的类名，便于根据类名读取yaml文件里的模板数据
        self.current_className = self.__class__.__name__
        # 根据当前类名获取yaml文件接口数据模板
        self.conf = api_template[self.current_className]
        self.path = self.conf["path"]

    def add(self, **kwargs):
        """
        添加
        :param kwargs: 字典类型的参数
        :return:
        """
        # # 读取配置文件模板中-add的内容
        # data = self.conf["add"]   这样读取会有问题，两者公用同一内存地址
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
            return {"retcode": 9999, "message": "接口返回错误!!!"}

    def list(self, **kwargs):
        """
        列出
        :param kwargs:
        :return:
        """
        # 读取yaml文件模板中-list的内容
        data = copy.deepcopy(self.conf["list"])
        # 把kwargs的内容更新到data字典中
        data.update(kwargs)
        payload = data
        url = self.host + self.path
        resp = requests.get(url, params=payload, headers=self.header)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"retcode": 9999, "message": "接口返回错误!!!"}

    def edit(self, _id, **kwargs):
        """
        编辑
        :param _id: 对象id
        :param kwargs:  字典类型的参数
        :return:
        """
        # 读取yaml文件模板中-edit的内容
        data = copy.deepcopy(self.conf["edit"])
        # 判断data字典是否为空，不为空则执行下面的语句。为空则跳过
        if bool(data):
            # 把kwargs的内容更新到data字典中的newdata字典中
            data["newdata"].update(kwargs)
            # 把data["newdata"]字典转换成json字符串
            data["newdata"] = json.dumps(data["newdata"], ensure_ascii=False)
        # 更改模板中的id值
        data["id"] = _id
        payload = data
        url = self.host + self.path
        resp = requests.put(url, data=payload, headers=self.header)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"retcode": 9999, "message": "接口返回错误!!!"}

    def delete(self, _id):
        """
        删除
        :param _id: 对象id
        :return:
        """
        # 读取yaml文件模板中-delete的内容
        data = copy.deepcopy(self.conf["delete"])
        # 更改模板中的id值
        data["id"] = _id
        payload = data
        url = self.host + self.path
        resp = requests.delete(url, data=payload, headers=self.header)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"retcode": 9999, "message": "接口返回错误!!!"}

    def delete_all(self, **kwargs):
        """
        删除第一页所有的数据
        :param kwargs:  pagenam=1, pagesize=20
        :return:
        """
        infos = self.list(**kwargs)["retlist"]
        for info in infos:
            self.delete(info["id"])


