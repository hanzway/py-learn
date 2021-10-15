# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/15 16:10


from collections import namedtuple

import pytest


"""
1.pytest中，测试用例的命名方式：
1.1 Test files should be named test_<something>.py or <something>_test.py.
1.2 Test methods in class or functions should be named test_<something>.
1.3 Test classes should be named Test<Something>.
2.pytest中，一个测试用例运行后，可能的几个结果：
2.1 运行成功:  .
2.2 运行失败或者：xpass + strict： F
2.3 用例没有运行，无条件跳过：s == skipped; 有条件跳过
2.4 期望是失败的用例：x，@pytest.mark.xfail()
"""
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    print('第一个测试用例-1')
    t1 = Task()
    assert t1 == Task(None, None, False, None)


def test_memeber_access():
    print('第二个测试用例2')
    e1 = 'buy milk'
    e2 = 'brain'
    t = Task(e1, e2)
    assert t.summary == e1
    assert t.owner == e2
    assert (t.id, t.done) == (None, False)


if __name__ == '__main__':
    pytest.main(['-vs'])