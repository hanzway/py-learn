# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/8 8:17

"""
1.sys模块
2.os模板
"""
import os


def t_01():
    # print(os.linesep) # 行分隔符: \r\n
    # print(os.pathsep) # 路径分隔符：;
    # print(os.sep)     # \
    f_path_name = 'C:\\aa\\bb\\cc\\d.txt'
    # 1.将一个文件地址path分为两份：一份是目录，一份文件名;
    print(os.path.split(f_path_name))
    print(os.path.normcase(__file__))
    print(os.path.normpath(__file__)) # 文件盘符D是大写的。
    print(os.path.split(__file__))
    # result:('C:\\aa\\bb\\cc', 'd.txt')
    # 2.直接获取文件所在的目录/文件名：
    print(os.path.dirname(f_path_name)) # 获取文件所在目录
    print(os.path.basename(f_path_name)) # 获取文件的文件名


def t_readme():
    # print(os.path.normpath(__name__))
    # print(os.path.normcase())
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    readme_path = os.path.join(BASE_DIR, 'README.md')
    with open(readme_path, 'rt', encoding='utf-8') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    t_readme()