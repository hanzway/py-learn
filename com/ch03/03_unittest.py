#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 18:30
# @Author  : ksu will han
# @File    : 03_unittest.py
# @Software: PyCharm
import pytest


@pytest.fixture()
def login():
    print('\n------》登录成功！')


def test_soso(login):
    print('\ntest-soso-----')


def test_looklook():
    print('\n不登录随便查看')


def test_addCart(login):
    print('\n登录后，将商品加入购物车！')


if __name__ == '__main__':
    pytest.main(['-vs'])
