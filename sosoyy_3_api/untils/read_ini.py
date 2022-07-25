#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 12:34
# @Author  : 习惯
# @File    : read_file.py
# @Software: PyCharm
import configparser
import os


class ReadIni:
    ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'setting.ini')

    def __init__(self, hosttype):
        self.hosttype = hosttype

    def read_ini(self):
        conf = configparser.ConfigParser()
        conf.read(self.ini_path, encoding='utf8')
        res_host = conf['host'][self.hosttype]
        return res_host


if __name__ == '__main__':
    r = ReadIni('对接接口').read_ini()
    print(r)
