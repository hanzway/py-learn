#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 12:36

# 一个类的实例属性，只允许是字符串类型，其他类型的化报异常，不允许赋值
import random


class Typed:
    def __init__(self, key, keyType):
        self.key = key
        self.keyType = keyType

    def __get__(self, instance, owner):
        print('get方法')
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set方法')
        if type(value) is not self.keyType:
            raise TypeError('{}传入的类型不正确，应该是{}'.format(value, self.keyType))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('delete方法')
        instance.__dict__.pop(self.key)


class Foo(object):

    name = Typed('name', str)
    age = Typed('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


def deco(obj):
    print('deco')
    obj.x = 1
    obj.y = random.randint(100, 200)
    return obj


@deco
class Foo2:
    """hello Foo2"""
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
