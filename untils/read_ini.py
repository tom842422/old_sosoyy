#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 12:34
# @Author  : 习惯
# @File    : read_file.py
# @Software: PyCharm
import configparser
import os
import yaml

ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'setting.ini')
print(ini_path)

# class ReadIni:
#     ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'config','setting.ini')
#     def

# def get_datas(file_neme, Document_type):
#     path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', file_neme)
#     if 'yaml' in file_neme:
#         with open(path, 'r', encoding='utf8') as f:
#             r_yaml = yaml.load(f, Loader=yaml.FullLoader)
#             return r_yaml
#     elif 'ini' in file_neme:
#         conf = configparser.ConfigParser()
#         conf.read(path, encoding='utf8')
#         return conf
#     else:
#         print('无法处理的文件类型')
#



# if __name__ == '__main__':
#     r =
#     print(r)
