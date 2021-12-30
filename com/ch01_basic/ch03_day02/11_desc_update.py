#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 13:35
# @Author  : ksu will han
# @File    : 11_desc.py
# @Software: PyCharm

"""
描述符的优先级：
1.类属性 > 数据描述符
2.数据描述符 》 实例属性
3.实例属性 》 非数据描述符
4.非数据描述符 》 找不到属性
5.当找不到的属性，会触发：__getattr__()
"""


class Foo:
    def __init__(self, key):
        self.key = key

    def __get__(self, instance, owner):
        print('-----get--------')
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('-------set--------')
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('------delete-----')


class Bar:
    x = Foo('x')

    def __init__(self, x):
        self.x = x


class Typed:
    def __init__(self, key, expect_type):
        self.key = key
        self.expect_type = expect_type

    def __get__(self, instance, owner):
        print('--get--')
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('-->set---')
        if not isinstance(value, self.expect_type):
            raise TypeError('%s传入的参数类型应为：%s,而传的是：%s' % \
                            (self.key, self.expect_type, type(value)))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('--->delete<---')
        instance.__dict__.pop(self.key)


def deco(**kwargs):
    """deco function"""
    print('---->', kwargs)

    def wrapper(obj):
        for key,key_type in kwargs.items():
            setattr(obj, key, Typed(key, key_type))
        return obj
    return wrapper


@deco(name=str, age=int)
class People:
    """People class"""
    # name = Typed('name', str)
    # age = Typed('age', int)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


def t10():
    p1 = People('tim', 100, 12.99)
    print(p1.__dict__)
    p2 = People(21.3, 100, 12.99)
    print(p2.__dict__)


def t11():
    p1 = People('tim', 100, 12.99)
    print(p1.__dict__)
    p2 = People('summer', 12, 30.21)
    print(p2.__dict__)

if __name__ == '__main__':
    t11()
