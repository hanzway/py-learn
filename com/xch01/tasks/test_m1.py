# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/22 20:33
import pytest


@pytest.mark.parametrize('name',
                         ['hello', 'gosh', 'school'],
                         ids=['用例1','用例2','用例3'])
def test_mm(name):
    assert 'h' in name


def test_01_login():
    print('\ntest_01_login')


def test_02_login():
    print('\ntest_02_login')


def test_03_login():
    print('\ntest_03_login')


if __name__ == '__main__':
    pytest.main(['-vs', '-m login'])
