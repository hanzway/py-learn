# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/15 16:20


"""Test the Task data type."""
import sys
from collections import namedtuple

import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


# @pytest.mark.order(x),x越小，越先运行，设置了1，2，3后，先运行用例1，在依次运行用例2，3。
@pytest.mark.order(1)
def test_asdict():
    """
    _asdict() should return a dictionary.
    """
    print('第三个测试用例3')
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    hope_dict = dict(zip(['summary', 'owner', 'done', 'id'],
                         ['do something', 'okken', True, 21]))
    assert t_dict == hope_dict


@pytest.mark.order(2)
def test_replace():
    """
    replace() should change passed in fields.
    """
    print('第四个测试用例4')
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


@pytest.mark.order(2)
@pytest.mark.skip(reason='misunderstood the API')
def test_skipped():
    """
    just test the decorators:
    @pytest.mark.skip(condition, msg)
    @pytest.mark.skipif(condition, msg)
    """
    print('第5个测试用例5')
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 101)
    assert t_after == t_expected


# @pytest.mark.skipif(condition='sys.platform=="win32"', reason='misunderstood the API2')
@pytest.mark.skipif(condition='sys.platform=="macOS"', reason='misunderstood the API2')
def test_skip_if2():
    """
    just test the decorators:
    @pytest.mark.skip(msg)：无条件跳过
    @pytest.mark.skipif(condition, msg)：有条件跳过，条件成立：跳过，不执行用例；条件不成立，不跳过，需要执行用例；
    """
    print('第5个测试用例5')
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


if __name__ == '__main__':
    print(sys.version)
