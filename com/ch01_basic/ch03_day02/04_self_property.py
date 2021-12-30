#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 23:28
# @Author  : ksu will han
# @File    : 04_self_property.py
# @Software: PyCharm

# 自定义实现Property
import random
import string

class Room(object):
    """Room class"""
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @staticmethod
    def get_random_str(length:str=6):
        return ''.join(random.sample(string.ascii_letters + string.digits, length))


if __name__ == '__main__':
    room = Room('good', 110, 2)
    print(room.area)
    print(Room.get_random_str(length=10))
