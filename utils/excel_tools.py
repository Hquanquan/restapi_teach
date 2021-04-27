#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 13:10
# @File : excel_tools.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import json

from configs.api_env import TestCaseFilePath
import xlrd


def get_excelDataByCaseName(sheetName, caseName, filePath=TestCaseFilePath):
    """
    根据sheetName和caseName,获取测试用例表里的用例
    :param filePath: 文件路径
    :param sheetName:
    :param caseName:
    :return:
    """
    resList = []
    # 1、打开Excel表格，formatting_info=True 保持原样式打开
    workBook = xlrd.open_workbook(filePath, formatting_info=True)
    # 2、获取sheet子表
    workSheet = workBook.sheet_by_name(sheetName)
    # 3、读取一列数据
    idx = 0  # 开始的下标2
    for one in workSheet.col_values(0):
        if caseName in one:
            # 读取Excel表格里的请求体参数
            reqBodyData = workSheet.cell(idx, 9).value
            # 读取Excel里的预期响应结果数据
            respData = workSheet.cell(idx, 11).value
            # 列表里嵌套元组
            resList.append((json.loads(reqBodyData), json.loads(respData)))
        idx += 1
    return resList


if __name__ == '__main__':
    data = get_excelDataByCaseName("登录模块", "Login", "../data/教管系统接口测试用例.xls")
    for one in data:
        print(one[0]["username"])
