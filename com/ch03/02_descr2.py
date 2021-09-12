#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 12:36

# 一个类的实例属性，只允许是字符串类型，其他类型的化报异常，不允许赋值
import random


def Typed(**kwargs):
    def deco(obj):
        # obj.x1 = 1
        # obj.x2 = 2
        # obj.x3 = 3
        for key, value in kwargs.items():
            setattr(obj, key, value)
        return obj
    return deco


@Typed(x01=1, x02=2, x03=3)
class Foo(object):
    '''OK'''
    pass


if __name__ == '__main__':
    print(Foo.__dict__)
