# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/31 19:33


import requests
import urllib3

urllib3.disable_warnings()


def t01():
    """练习使用requests库"""
    url = r'https://www.12306.cn/index/'
    res = requests.get(url=url)
    print(res.text)


def t02():
    # url = 'https://www.cnblogs.com/yoyoketang/'
    url = 'https://www.cnblogs.com/yoyoketang/p/15752639.html'
    res = requests.get(url=url, verify=False) # InsecureRequestWarning
    # print(res.content)
    res_text = res.text
    print(res_text) # 类型： str


if __name__ == '__main__':
    t02()
