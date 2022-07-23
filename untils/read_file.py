#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 12:34
# @Author  : 习惯
# @File    : read_file.py
# @Software: PyCharm
import configparser
import os
import yaml


yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'manufacturing_data.yaml')
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'setting.ini')


def read_yaml():
    with open(yaml_path, 'r', encoding='utf8') as f:
        r_yaml = yaml.load(f, Loader=yaml.FullLoader)
        return r_yaml


def read_ini():
    conf = configparser.ConfigParser()
    conf.read(ini_path, encoding='utf8')
    return conf


Read_ini = read_ini()
Read_yaml = read_yaml()
