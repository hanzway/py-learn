#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 13:35
# @Author  : ksu will han
# @File    : 11_desc.py
# @Software: PyCharm

"""
描述符的优先级：
1.类属性
2.数据描述符
3.实例属性
4.非数据描述符
5.找不到的属性，会触发：--getattr--()
"""


class Foo:
    def __init__(self, key):
        self.key = key

    def __get__(self, instance, owner):
        print('-----get----')
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('-----set------')
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('------delete-----')


class Bar:

    x = Foo('x')

    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    bar = Bar(100)
    print(bar.x)
