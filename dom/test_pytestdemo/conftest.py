# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/16 11:23
# @Author : qingwei.han
import pytest

from .calculator import Calc
from .xtool.common import yml_data

yaml_data = yml_data()


@pytest.fixture(scope='function', name='caseDataFromYml')
def acquire_data(request):
    trigger = request.node.get_closest_marker('acquire_data')
    key_list = trigger.args[0].split('$')
    key_num = len(key_list)
    if key_num == 1:
        return yaml_data[key_list[0]]
    elif key_num == 2:
        key1,key2 = key_list
        return yaml_data[key1][key2]
    elif key_num == 3:
        key1, key2, key3 = key_list
        return yaml_data[key1][key2][key3]
    elif key_num == 4:
        key1, key2, key3, key4 = key_list
        return yaml_data[key1][key2][key3][int(key4)]
    else:
        raise


@pytest.fixture(scope='function', name='acquireCalc')
def acquire_calc():
    calc = Calc()
    return calc
