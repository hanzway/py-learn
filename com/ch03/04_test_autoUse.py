#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 18:52
# @Author  : ksu will han
# @File    : 04_test_autoUse.py
# @Software: PyCharm
import pytest


# autouse=True时，每个测试用例执行之前，先运行的；scope的四种选择：
# scope: package, session, module, function, default is function.
@pytest.fixture(scope='function', autouse=True)
def login():
    print('\n------》登录成功！')
    yield
    print('\n------》退出成功！')


def test_soso():
    print('\ntest-soso-----')


def test_looklook():
    print('\n不登录随便查看')


def test_addCart():
    print('\n登录后，将商品加入购物车！')


@pytest.mark.search_case('nameList')
def test_add_account(caseData2):
    default1, default2, default3 = caseData2
    print('\n', default1)
    print(default2)
    print(default3)


if __name__ == '__main__':
    pytest.main(['-vs'])
