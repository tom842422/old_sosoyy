#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 12:34
# @Author  : 习惯
# @File    : read_file.py
# @Software: PyCharm
import configparser
import os


class ReadIni:
    """

    """
    ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'setting.ini')

    def __init__(self, hosttype):
        # 接口类型
        self.hosttype = hosttype

    def read_ini(self):
        conf = configparser.ConfigParser()
        conf.read(self.ini_path, encoding='utf8')
        # 根据接口类型返回对应的host
        return conf['host'][self.hosttype]


if __name__ == '__main__':
    r = ReadIni('对接接口').read_ini()
    print(r)
