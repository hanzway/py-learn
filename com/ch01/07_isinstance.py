#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 10:57
# @Author  : ksu will han
# @File    : 07_isinstance.py
# @Software: PyCharm

# isinstance
class Foo(object):
    pass


class Bar(Foo):
    pass


def t01():
    print(isinstance(Bar(), Foo))
    print(isinstance(Bar(), Bar))
    print(isinstance(Bar(), object))

if __name__ == '__main__':
    t01()
