#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 19:31
import random

import pytest


@pytest.fixture()
def open_browser():
    print('\n打开浏览器，打开百度首页')
    yield
    print('\n执行teardown')
    print('最后关闭浏览器')


@pytest.fixture()
def login():
    print('\n----->登录成功！！')


@pytest.mark.usefixtures('open_browser')
def test_s1():
    print('\ncase1: testS1')
    pytest.assume(100 > random.randint(50, 150))
    pytest.assume(100 > random.randint(50, 150))
    pytest.assume(100 > random.randint(50, 150))


@pytest.mark.usefixtures('login')
def test_s2():
    print('\ncase2: testS2')
    pytest.assume(100 > random.randint(50, 150))
    pytest.assume(100 > random.randint(50, 150))
    pytest.assume(100 > random.randint(50, 150))


if __name__ == '__main__':
    pytest.main(['-vs'])
