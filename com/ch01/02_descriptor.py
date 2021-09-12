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
            raise TypeError('type error : %s, the correct type is %s'%(value,self.wantedType))
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
    print('======')
    obj.x = 1
    obj.y = False
    obj.z = [1,2,3]
    return obj


@decr # Foo = decr(Foo)
class Foo(object):
    '''xyz'''
    pass


if __name__ == '__main__':
    f = Foo()
    print(f.__dict__)
    print(Foo.__dict__)