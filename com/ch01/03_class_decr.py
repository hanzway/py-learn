#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:55
# @Author  : ksu will han
# @File    : 03_class_decr.py
# @Software: PyCharm

def Typed(**kwargs):
    print(kwargs)
    def decr(obj):
        print('======')
        for k,v in kwargs.items():
            # obj.__dict__[k] = v
            setattr(obj, k, v)
            # obj.k = v
        return obj
    return decr


#字典取值的三种方式：
# 1.dict.key = value
# 2.setattr(obj,key,value)
# 3.dict[key] = value

@Typed(x=1, y =False, z=[1, 22, 333])
class Foo(object):
    pass



if __name__ == '__main__':
    print(Foo.__dict__)