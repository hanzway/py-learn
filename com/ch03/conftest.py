#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

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


def base_login(username, pwd):
    return '_'.join([username, pwd, ''.join(random.sample(string.ascii_letters, 6))])


@pytest.fixture(scope='function', name='token_info')
def get_token(request):
    index = request.node.get_closest_marker('get_token')
    user_info = index.args[0]
    username = user_info.get('name')
    pwd = user_info.get('pwd')
    return base_login(username, pwd)


if __name__ == '__main__':
    search_case()