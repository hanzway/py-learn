#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 19:22
# @Author  : ksu will han
# @File    : 13_property.py
# @Software: PyCharm

"""
1.描述符的分类：
 - 数据描述符：实现了set,get,delete三个方法的新式类；
 - 非数据描述符：没有实现set方法的新式类；

2、描述符中的get方法有两个参数：
 - 第一个参数：instance：被修饰类的实例本身；
 - 第二个参数：owner:被修饰的类；

3、Property的约定：
 - 当用例实例调用方法名时，就像访问实例属性一样，获取到返回值；300
 - 当用类调用方法名时，返回描述符对象本身：<__main__.CustomProperty object at 0x00000173899AF248>
"""


class CustomProperty:
    def __init__(self, func):
        # print('====>>>>', func)
        self.func = func

    def __get__(self, instance, owner):
        # print(instance)
        # print(owner)
        if instance is None:
            return self
        res = self.func(instance)
        setattr(instance, self.func.__name__, res)
        return res


class Room(object):

    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    @CustomProperty  # area = CustomProperty(area)
    def area(self):
        return self.width * self.length


def t01():
    room = Room(100, 3)
    print(room.area)
    print(Room.area)


class Thing:
    def __init__(self, original_price, discount):
        self.original_price = original_price
        self.discount = discount

    @property
    def price(self):
        return self.original_price * self.discount

    @price.setter
    def price(self, new_price):
        self.original_price = new_price

    @price.deleter
    def price(self):
        del self.original_price


if __name__ == '__main__':
    thing =Thing(100, 0.8)
    print(thing.price)
    thing.price = 200
    print(thing.price)
    del thing.price
    print(thing.price)
