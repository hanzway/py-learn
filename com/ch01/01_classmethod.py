#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 18:50
# @Author  : ksu will han
# @File    : 01_classmethod.py
# @Software: PyCharm

class Room(object):
    def __init__(self, name:str='tom'):
        self.name = name

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


if __name__ == '__main__':
    room = Room('jerry')
    print(room.give_name)
    room.tell_info()
    print(Room.testAdd(100, 202))
    print(room.testAdd(111, 202))