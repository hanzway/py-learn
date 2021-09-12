#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 19:41
import random

import pytest

the_param_data = [('1+2', 3), ('4+5', 9), ('5*6', 30), ('9/3', 3.0), ('70-30', 40)]


# 第二种传参：通过@pytest.mark.parametrize进行传参。
@pytest.mark.parametrize('input_expression,expected', the_param_data,\
                         ids=['CASE_' + str(i) for i in range(len(the_param_data))])
def test_eval(input_expression, expected):
    print('\n{}--{}'.format(input_expression, expected))
    assert eval(input_expression) == expected


if __name__ == '__main__':
    pytest.main(['-vs'])
