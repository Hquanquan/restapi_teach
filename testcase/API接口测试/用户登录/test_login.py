#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 23:12
# @File : test_login.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

import allure
import pytest

from pylib.APIlib.loginAPI import LoginAPI
from utils.excel_tools import get_excelDataByCaseName


@allure.epic("教管系统-接口测试")
@allure.feature("登录模块")
class TestLoginAPI:

    @allure.title("登录认证")
    # @pytest.mark.skip("暂不执行")
    @pytest.mark.parametrize("inData, respDate", get_excelDataByCaseName("登录模块", "Login"))
    def test_login(self, inData, respDate):
        """
        登录接口测试
        :param inData:
        :param respDate:
        :return:
        """
        resp = LoginAPI().login002(inData)
        assert resp == respDate

    # @pytest.mark.skip("暂不执行")
    @allure.title("退出登录")
    def test_logout001(self, get_cookie):
        """
        已登录时，退出正常
        :param get_cookie: 调用这个方法获取cookie，则代表已经登录系统
        :return:    {"retcode": 0}
        """
        resp = LoginAPI.logout()
        assert resp["retcode"] == 0

    @allure.title("退出登录")
    # @pytest.mark.skip("暂不执行")
    def test_logout002(self):
        """
        未登录时，退出登录
        :return:
        """
        resp = LoginAPI.logout()
        assert resp["retcode"] == 0






