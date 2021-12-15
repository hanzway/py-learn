# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/22 20:37
import logging

import pytest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='report.log',
    filemode='w'
)

logger = logging.getLogger(__name__)


# 作用：用来修改用例的编码方式，从而支持给用例名起中文名字,hook函数不用加入到fixture中的。
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        # item.name:用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item._nodeid:用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)

    items.reverse()



def pytest_addoption(parser, pluginmanager):
    # 创建组名，将下面所有的Options，展示在这个组名下面。
    mygroup = parser.getgroup('school')
    mygroup.addoption('--env', # 注册一个命令行选项
                       default = 'test', # 参数的默认值
                       dest = 'env', # 存储的变量
                       help='set your run env 2021.')  # 帮助提示，对参数的描述

@pytest.fixture(scope='session')
def cmdoption(request):
    envValue = request.config.getoption('--env', default='test')
    if envValue == 'test':
        print('env is test!')
    elif envValue == 'dev':
        print('env is develop')
    return envValue