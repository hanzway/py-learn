# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/3 11:23
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @Project : py-learn


def welcome():
    print('welcome outer function !')

class Home(object):
    def __init__(self, owner):
        self.owner = owner

    def say_hi2(self):
        print('welcome from Home!')


def t1():
    home1 = Home('jerry')
    if not hasattr(home1, 'say_hi'):
        # home1.say_hi = welcome
        setattr(home1, 'say_hi', welcome)
    home1.say_hi()


def t2_get_function_name():
    home2 = Home('Rick')
    # print(home2.__dict__['say_hi'])
    print(home2.say_hi2.__name__)


if __name__ == '__main__':
    t1()
    # t2_get_function_name()


