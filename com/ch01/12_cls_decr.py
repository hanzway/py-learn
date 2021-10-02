#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 18:42
# @Author  : ksu will han
# @File    : 12_cls_decr.py

# 类的装饰器:给类中传自定义的类属性和类属性的值
def typed(**kwargs):
    print('---outer---')
    def deco(obj):
        print('---inner---')
        for key, value in kwargs.items():
            # error: 'mappingproxy' object does not support item assignment
            # obj.__dict__[key] = value
            setattr(obj, key, value)
        return obj
    print('---->>>>>>', kwargs)
    return deco


@typed(a1=100, b2=200, c3=300)
class Foo(object):
    """Foo class 1002"""
    pass


if __name__ == '__main__':
    print(Foo.__dict__)




