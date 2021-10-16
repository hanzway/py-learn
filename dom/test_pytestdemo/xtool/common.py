# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/16 11:40
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @File : common.py
# @Project : py-learn
import os.path

import yaml

the_yml_path = os.path.join(os.path.dirname(os.path.dirname(__name__)), 'ymlres/data.yml')


def yml_data():
    with open(the_yml_path, 'rt', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data
