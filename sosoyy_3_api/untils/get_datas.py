#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 14:22
# @Author  : 习惯
# @File    : get_datas.py
# @Software: PyCharm

import os
from untils.read_file import Read_ini, Read_yaml
import configparser

print(Read_ini['host']['test_url'])
print(Read_yaml)


def get_datas():
    url = Read_ini['host']['test_url']
