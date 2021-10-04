# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/1 9:35
# @Author : qingwei.han


# 1.列表解析，字典解析，集合解析，过滤器
# 2.为元祖中的每个元素命名
import random
from enum import IntEnum

original_list = [random.randint(-10, 10) for _ in range(10)]


def t01_list():
    """列表解析"""
    new_list = [i for i in original_list if i > 0]
    print(original_list)
    print(new_list)


def t02_filter():
    # 结果是生成器对象，需要使用list方法，将生成器对象转换为列表；
    new_2_list = filter(lambda x: x > 0, original_list)
    print(new_2_list)  # <filter object at 0x00000237BBE70348>
    print(list(new_2_list))


def t03_dict():
    dest_score = 80
    grade_score = {'student%i' % i: random.randint(40, 100) \
                   for i in range(1, 21)}
    print('old score: ', grade_score)
    # 字典解析：过滤score > 60的所有学生:
    new_score = {k: v for k, v in grade_score.items() if v >= dest_score}
    print('> 60\'student score: ', new_score)
    new_2_score = filter(lambda item: item[1] > dest_score, grade_score.items())
    print('new score: ', dict(new_2_score))


def t04_set():
    old_set = {random.randint(-50, 50) for _ in range(10)}
    more_zero = {i for i in old_set if i > 0}
    print(old_set)
    print(more_zero)


# 2.为元祖中的每个元素命名，访问元祖中元素的时候，需要使用索引，不利于可读性；
stu_dict = ('tom', 16, 'M')


def named_tuple():
    # 2.1 通过数值常量进行索引的数字命名named；
    NAME, AGE, SEX = range(3)
    print(stu_dict[NAME])
    print(stu_dict[AGE])
    print(stu_dict[SEX])


# 2.2 定义数字枚举
class StudentEnum(IntEnum):
    """学生类的属性枚举值"""
    NAME = 0
    AGE = 1
    SEX = 2


def enum_named():
    print(stu_dict[StudentEnum.NAME])
    print(stu_dict[StudentEnum.AGE])
    print(stu_dict[StudentEnum.SEX])


from collections import namedtuple


def named_tuple():
    # 想自定义类一样访问类的对象的属性；
    Student = namedtuple('Student', ['name', 'age', 'sex'])
    s1 = Student('tom1', 100, 'F')
    s2 = Student('tom2', 200, 'M')
    print(s1.name)
    print(s1.age)
    print(s1.sex)
    print(s1)


if __name__ == '__main__':
    named_tuple()
