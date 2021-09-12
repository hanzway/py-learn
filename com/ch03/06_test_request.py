#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 19:41
import random

import pytest


list_data = [random.randint(50, 100) for _ in range(3)]


# 第一种传参：通过fixture进行传参。
@pytest.fixture(params=list_data,\
                ids=['case-' + str(i) for i in range(len(list_data))],
                name='the_age')
def test_data(request):
    if type(request.param) is int and request.param <= 60:
        request.param += 10
    return request.param


def test_one(the_age):
    print('\ntest data: {}'.format(the_age))
    assert the_age > 60


if __name__ == '__main__':
    pytest.main(['-vs'])
