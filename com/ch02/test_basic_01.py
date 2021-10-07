# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/7 16:48
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @File : test_basic_01.py
# @Project : py-learn
import pytest


def func(a, b):
    return a + b


def test_func():
    assert func(10, 5) == 15


@pytest.mark.parametrize(argnames='num1, num2', argvalues=[(100, 100), (200, 200)],ids=['t_name_100', 't_name_200'])
@pytest.mark.search_case_data('loginInfo')
def test_4_login(case_data_result, num1, num2):
    for value in case_data_result.items():
        pytest.assume(value[1] == '123456')
    pytest.assume(num1 == num2)


@pytest.mark.search_case_data('checkInfo')
def test_check(case_data_result):
    assert case_data_result.get('code') == 200


if __name__ == '__main__':
    pytest.main(['-vs','-m', 'test_4_login'])