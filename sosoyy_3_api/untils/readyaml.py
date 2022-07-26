#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 12:34
# @Author  : 习惯
# @File    : read_file.py
# @Software: PyCharm
import json
import os
import yaml


class ReadYaml:
    uri_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config_3',
                            'manufacturing_uri.yaml')
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config_3',
                             'manufacturing_data.yaml')

    def __init__(self, filename):
        # 单据类型
        self.filename = filename

    def get_uri(self):
        with open(self.uri_path, 'r', encoding='utf8') as f:
            uri = yaml.load(f, Loader=yaml.FullLoader)
        # 返回单据类型下的uri
        return uri[self.filename]

    def get_datas(self):
        with open(self.data_path, 'r', encoding='utf8') as f:
            data_yaml = yaml.load(f, Loader=yaml.FullLoader)[self.filename]
        # 返回单据类型下的测试数据，并进行编码处理，避免中文乱码
        return json.dumps(data_yaml, ensure_ascii=False)


if __name__ == '__main__':
    r_uri = ReadYaml(filename='采购退货单').get_uri()
    r_data = ReadYaml(filename='采购退货单').get_datas()
    print(r_data)
    print(r_uri)
