#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 12:58
# @Author  : ksu will han
# @File    : 09_doc.py
# @Software: PyCharm

# the attribute --doc--
class Foo:
    """Foo doc"""
    pass


class Bar(Foo):
    pass


# if __name__ == '__main__':
#     print(Bar.__doc__)
#     # error: ['mappingproxy' object has no attribute 'pop']
#     # print(Bar.__dict__.pop('__doc__'))
#     print(Bar.__dict__)

# del析构方法：当内存回收对象时，会调用对象的del析构函数

class Foo2:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('del methods is executing!')

    def __call__(self, *args, **kwargs):
        print('实例执行成功，obj()')


if __name__ == '__main__':
    f1 = Foo2('tom')
    f1()

