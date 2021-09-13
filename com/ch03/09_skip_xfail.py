# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/11 8:17


# @pytest.mark.skip表示：无条件跳过，不运行这个测试用例[unconditional skip]
# @pytest.mark.xfail表示：这个用例是一个已知错误的用例
# @pytest.mark.skipif(conditon,message):当condition成立，就不运行这个用例；
import random

import pytest


def test_skip_01():
    assert 100 > random.randint(50, 150)


# 在结果中，使用的是：skipped来标识的，即：无条件跳过这个测试用例。
@pytest.mark.skip
def test_skip_02():
    assert 100 > random.randint(50, 150)

environment = 'andriod'
# 有条件跳过
# @pytest.mark.skipif(condition, reason)，当条件condition为真，不执行这个用例；当条件为假，运行用例！
# @pytest.mark.skipif(condition='100 > random.randint(50, 150)', reason='获取到的随机值大于100时，才执行这个用例')
@pytest.mark.skipif(condition='environment == "andriod"', reason='IOS用例，安卓不运行！')
def test_skip_if_01():
    assert 100 > random.randint(50, 100)


# @pytest.mark.skipif(condition, reason)，当条件condition为真，不执行这个用例；当条件为假，运行用例！
@pytest.mark.skipif(condition='100 > random.randint(50, 150)', reason='获取到的随机值大于100时，才执行这个用例')
def test_skip_if_02():
    assert 100 > random.randint(50, 100)


@pytest.mark.xfail # 结果中的标识：09_skip_xfail.py::test_xfail_01 XPASS
def test_x_fail_01():
    assert 100 > random.randint(50, 100)


# 2021-09-13 增加文件：09-skip-xfail.py
if __name__ == '__main__':
    pytest.main(['-vs'])





