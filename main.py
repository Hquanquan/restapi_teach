#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 9:25
# @File : main.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 测试入口文件
import os

import pytest

def run():
    for one in os.listdir('report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'report/tmp/{one}')
    pytest.main(['testcase/API接口测试', '-s', '--alluredir=report/tmp'])
    # pytest.main(['-k test_courses.py', '-s', '--alluredir=report/tmp'])
    os.system('allure serve report/tmp')


if __name__ == '__main__':

    run()
    # pytest.main(["-s", "-k test_teachers.py"])
    # pytest.main(["-s", "-m", "updateCourse"])






