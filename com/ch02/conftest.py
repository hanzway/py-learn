#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 12:33


import pytest

from com.ch02.caseData import CASE_DATA

"""
公用前置函数写在conftest.py文件中
available fixtures: 自定义的fixture是：【case_data_result和login】；
	cache, capfd, capfdbinary, caplog, capsys, capsysbinary, 
	case_data_result, doctest_namespace, login, 
	monkeypatch, pytestconfig, record_property, 
	record_testsuite_property, record_xml_attribute, 
	recwarn, tmp_path, tmp_path_factory, 
	tmpdir, tmpdir_factory
"""


@pytest.fixture(scope='session')
def login():
    print('登陆了')


@pytest.fixture(scope='function', name='case_data_result')
# @pytest.fixture(scope='function')
def search_case_data(request):
    index = request.node.get_closest_marker('search_case_data')
    if len(index.args) == 1 and index.args[0] in CASE_DATA.keys():
        case_data_rlt = CASE_DATA[index.args[0]]
    else:
        raise Exception('执行的用例数据不存在：%s' % index.args[0])
    return case_data_rlt
