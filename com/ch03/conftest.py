#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 18:58
# @Author  : ksu will han
# @File    : conftest.py
# @Software: PyCharm
import random

import pytest

case_info = {
    'nameList': ['TOM-' + str(i) for i in range(3)],
    'ageList': [random.randint(16, 100) for _ in range(3)],
    'interestList': ['Play-' + str(i) for i in range(10, 13)],
    'defaultList': ['Default-'+ str(i) for i in range(20, 23)]
}


@pytest.fixture(scope='function', name='caseData2')
# @pytest.fixture(scope='function')
def search_case(request):
    index = request.node.get_closest_marker('search_case')
    if len(index.args) == 1 and index.args[0] in case_info.keys():
        caseData = case_info[index.args[0]]
    else:
        caseData = case_info['defaultList']
    return caseData


if __name__ == '__main__':
    search_case()