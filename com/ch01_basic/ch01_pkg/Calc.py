# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/14 18:15
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @File : Calc.py
# @Project : py-learn


class Calc(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        if self.b == 0:
            raise
        return self.a // self.b

    def multi(self):
        return self.a * self.b
