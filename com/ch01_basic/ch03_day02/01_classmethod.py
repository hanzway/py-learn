#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 18:50
# @Author  : ksu will han
# @File    : 01_classmethod.py
# @Software: PyCharm

class Room(object):
    def __init__(self, length:int, width:int, name:str= 'tom'):
        self.name = name
        self.length = length
        self.width = width


    @classmethod
    def tell_info(cls):
        print('room - tell - info')

    @staticmethod
    def testAdd(num1, num2):
        return num1 + num2

    def set_name(self, name):
        self.name = name

    @property
    def give_name(self):
        return self.name

    @property
    def area(self):
        return self.width * self.length

    @classmethod
    def getMax(cls, num1, num2):
        if not isinstance(num1, int) or  not isinstance(num2, int):
            raise TypeError('类型错误')
        else:
            return num1 if num1 > num2 else num2


# @property的第1种用法
class Foo(object):
    def __init__(self, orderNo):
        self.orderNo = orderNo

    @property
    def order(self):
        return self.orderNo

    @order.setter
    def order(self, orderNo):
        self.orderNo = orderNo

    @order.deleter
    def order(self):
        del self.orderNo


if __name__ == '__main__':
    # r1 = Room('jerry', 100, 4)
    # print(r1.testAdd(100, 200))
    print(Room.getMax(300, 600))
    print(Room.getMax(300, 200))