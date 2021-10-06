#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:11
# @Author  : ksu will han
# @File    : 02_descriptor.py
# @Software: PyCharm

# 数据描述符的优先级： 类属性 - 数据描述符 - 实例属性 - 非数据描述符 - __getattr__
class Typed(object):

    def __init__(self, key, wantedType):
        self.key = key
        self.wantedType = wantedType

    def __get__(self, instance, owner):
        print('get method')
        # print('instance参数：【%s】-->' % instance, type(instance))
        # print('owner参数：%s' % owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set method')
        # print('instance参数：【%s】-->' % instance, type(instance))
        # print('要给属性赋值的值为：%s'% value)
        if not isinstance(value, self.wantedType):
            raise TypeError('type error : %s, the correct type is %s' % (value, self.wantedType))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('delete方法')
        print('instance参数：【%s】' % instance)
        instance.__dict__.pop[self.key]


class Worker:
    name = Typed('name', str)
    age = Typed('age', int)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return self.__dict__.__str__()


# 类的装饰器
def decr(obj):
    # print('======')
    obj.x = 1
    obj.y = False
    obj.z = [1, 2, 3]
    return obj


@decr  # Foo = decr(Foo)
class Foo(object):
    '''xyz'''
    pass


from functools import wraps


# 被装饰函数被替换为闭包函数中的wrapper函数。
def decr(func):
    # print('outer')

    @wraps(func)  # 作用：将index的双下划线开头的内置函数的值，复制给闭包函数wrapper的双下划线开头的内置函数的值
    # @wraps(func) 伪代码： wrapper.__name__ = func.__name__ wrapper.__doc__ = index.__doc__
    def wrapper(*args, **kwargs):
        print('do another thing.')
        result = func(*args, **kwargs)
        return result

    return wrapper


# 有参装饰器：在无参装饰器的基础上，在包一层。
def save_args(location):
    def decr(func):
        @wraps(func) # 加上这个装饰器后，就会将原函数的所有内置变量复制给装饰器函数；
        def wrapper(*args, ** kwargs):
            print('save arguments to the file: %s' % location)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decr


@decr
def index(x, y):
    """index description"""
    return x + y


def t01():
    # <function decr.<locals>.wrapper at 0x000001AA64B11798>；加上@wraps后，会更新为：<function index at 0x00000260F471D708>
    print(index)
    print(index.__name__)  # wrapper 加上@wraps后，会更新为：index；
    print(index.__doc__)  # None,加上@wraps后，会更新为：index description；


@save_args(location='c://data//log1.log')
def index2(x, y):
    """index description"""
    return x + y

def t02():
    print(index2(100, 30))

if __name__ == '__main__':
    t02()
