# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/22 19:33
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @File : r2_https.py
# @Project : py-learn

import requests


def t01():
    url = r'https://www.12306.cn/index/'
    res = requests.get(url=url)
    print(res.text)


if __name__ == '__main__':
    t01()
