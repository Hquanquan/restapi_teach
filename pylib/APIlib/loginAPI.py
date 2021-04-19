#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 9:38
# @File : loginAPI.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 登录接口
import requests

from configs.api_config import HOST


class LoginAPI:
    """
    登录接口
    """

    def login002(self, inData):
        """
        登录方法
        :param inData:  字典类型的参数，如：{"username": username, "password": password}
        :return:
        """
        url = f"{HOST}/api/mgr/loginReq"
        payload = inData
        resp = requests.post(url, data=payload)
        return resp.json()

    @staticmethod
    def login001(username, password):
        """
        登录方法001，需要输入账号，密码
        :param username:
        :param password:
        :return:
        """
        url = f"{HOST}/api/mgr/loginReq"
        inData = {"username": username, "password": password}
        payload = inData
        resp = requests.post(url, data=payload)
        return resp.headers['Set-Cookie'].split(";")[0]

    @staticmethod
    def logout():
        """
        退出登录
        :return:
        """
        url = f"{HOST}/api/mgr/logoutreq"
        resp = requests.get(url)
        return resp.json()


if __name__ == '__main__':
    loginInfo = LoginAPI().login001("auto", "sdfsdfsdf")
    print(loginInfo)

    # inData1 = {"username": "auto", "password": "sdfsdfsdf"}
    # loginInfo = LoginAPI().login002(inData1)
    # print(loginInfo)
    info = LoginAPI().logout()
    print(info)




