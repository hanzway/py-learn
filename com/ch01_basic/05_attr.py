#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 10:09
# @Author  : ksu will han
# @File    : 05_attr.py
# @Software: PyCharm

# about the method build-in: getattr, setattr, delattr;

# 设计一个类，要求Foo的所有的属性都是：字符串。
class Foo:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __getattr__(self, item):
        print('---->', item)

    def __setattr__(self, key, value):
        # print(key, ' -> ', value)
        if type(value) is str:
            print('开始字符串设置：', value)
            self.__dict__[key] = value
        else:
            print('the value: %s is not str.' %(str(value),))

    def __delattr__(self, item):
        self.__dict__.pop(item)


def t01():
    foo = Foo('tom')
    print(foo.name)  # _Foo__name
    foo.age = 100
    print(foo.age)  # age
    print(foo.__dict__)
    del foo._Foo__name
    print(foo.__dict__)


class List(list):
    def append(self, __object) -> None:
        if type(__object) is str:
            super().append(__object)
        else:
            raise BaseException('only append the str value: ', __object)

    def show_middle(self):
        mid_index = int(len(self)/2)
        return self[mid_index]



if __name__ == '__main__':
    l1 = List('12345678')
    # l1.append(100)
    print(l1)
    print(l1.show_middle())
    l1.append('hello')
    l1.append('world')
    print(l1)
    print(l1.show_middle())


