# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/3 10:07
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @Project : py-learn


class Course:
    def __init__(self, course_name, course_price):
        self.course_name = course_name
        self.course_price = course_price


class School:
    def __init__(self, name, addr, course: Course):
        self.name = name
        self.addr = addr
        self.course = course


def t1():
    course = Course('Chinese', 2000)
    print(course.course_price)
    school = School('新东方', 'beijing', course)
    print(school.course.course_price)


# 多态
class Animal(object):
    def eat(self, food):
        print('the Animal is eating %s !' % food)

    def animal_sing(self):
        print('Animal is singing songs.')


class Dog(Animal):
    def eat(self, food):
        print('the dog is eating %s !' % food)

    def dog_sing(self):
        super(Dog, self).animal_sing()
        print('the Dog is singing songs !')


class Duck(Animal):
    def eat(self, food):
        print('the duck is eating %s !' % food)


class TestP:
    def __init__(self, animal: Animal):
        self.animal = animal

    def t_eat(self):
        self.animal.eat(food='花生')


"""
封装 encap, 约定：
1. 属性名字要是以单个下划线开头，这个属性在外部不建议使用，但是在外部可以通过属性名访问的
2. 以两个下划线开头的属性，python在内部会将属性名进行重命名为：
_className__attributeName来访问的，就需要通过新的属性名来访问。
"""


class People(object):
    _star = 'earth'

    def __init__(self, id, name):
        self._id = id
        self.__name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self.__name


def t2():
    p1 = People(100, 'tom')
    print(p1.get_id())
    print(p1._id)
    # 第一种访问方式
    print(p1._People__name)
    # 第二种访问方式：通过函数属性获取
    print(p1.get_name())


class Room(object):
    def __init__(self, owner, length, width):
        self.owner = owner
        self.__width = width
        self.__length = length

    def tell_area(self):
        return self.__width * self.__length


def t3():
    room1 = Room('tom', 200, 4)
    print(room1.tell_area())


if __name__ == '__main__':
    t3()
