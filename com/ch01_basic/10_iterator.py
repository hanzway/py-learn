#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 13:07
# @Author  : ksu will han
# @File    : 10_iterator.py
# @Software: PyCharm

"""
10.迭代器协议：对象必须提供一个next方法，执行该方法时，要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代
1. 可迭代对象：实现了迭代器协议的对象，在对象内部定义一个__iter__()方法；
2. 协议是一种约定，可迭代对象实现了迭代器协议，python的内部工具：for, sum, max, min, avg,都使用了迭代器协议访问对象的。

"""
class Fab:
    def __init__(self, n):
        self._a = 1
        self._b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        if self._b > self.n:
            raise StopIteration()
        return self._b


if __name__ == '__main__':
    f1 = Fab(100)
