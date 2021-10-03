# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/3 09:40
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @Project : py-learn

"""
type是python的内置类
"""


class Foo:
    pass


def t1():
    f1 = Foo()
    print(type(f1))  # <class '__main__.Foo'>
    print(type(Foo))  # <class 'type'>


def welcome(self):
    print('hello, welcome !')


Foo2 = type('Foo2', (object,), {'x': 1, 'y': 2, 'welcome': welcome})


def t2():
    print(Foo2)
    print(Foo2.__dict__)
    foo2 = Foo2()
    print(foo2)
    # Foo2.welcome()
    foo2.welcome()

# 通过自定义原类，实现类的自定义原类
class MyType(type):
    def __init__(self, a, b, c):
        print('元类的构造函数执行！')
        print(a) # 字符串类名：Foo3
        print(b) # 要继承的父类列表：()
        print(c) # 数据属性和函数属性的字典：dict

    def __call__(self, *args, **kwargs):
        print('------->>>>>')
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj

class Foo3(metaclass=MyType):
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    foo3 = Foo3('tom31111')
    print(foo3.name)

