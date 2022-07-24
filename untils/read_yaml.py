#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 18:17
# @Author  : 习惯
# @File    : read_yaml.py
# @Software: PyCharm
import os
import yaml
import json


class ReadYaml:
    uri_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                            'manufacturing_uri.yaml')
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config',
                             'manufacturing_data.yaml')

    def __init__(self, filename):
        self.filename = filename

    def get_uri(self):
        with open(self.uri_path, 'r', encoding='utf8') as f:
            uri_yaml = yaml.load(f, Loader=yaml.FullLoader)
        uri = uri_yaml[self.filename]
        return uri

    def get_datas(self):
        with open(self.data_path, 'r', encoding='utf8') as f:
            data_yaml = yaml.load(f, Loader=yaml.FullLoader)
        datas = data_yaml[self.filename]
        return datas


if __name__ == '__main__':
    r_uri = ReadYaml('采购入库单').get_uri()
    r_data = ReadYaml('采购入库单').get_datas()
    print(r_uri)
    print(r_data)
