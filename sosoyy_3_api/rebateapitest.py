import code
import os
import traceback

import requests
import time
import json
from past.builtins import raw_input
from sosoyy_3_api.untils.read_yaml import ReadYaml
from sosoyy_3_api.untils.read_ini import ReadIni
import yaml
import random
import json
import ast


class RTS:

    def __init__(self, hosttype, filename):
        """
        :param hosttype: 接口类型
        :param filename: 单据类型
        """
        self.filename = filename
        self.hosttype = hosttype

    def rts(self):
        # 读取并拼接成url
        url = ReadIni(self.hosttype).read_ini() + ReadYaml(self.filename).get_uri()
        # 读取测试数据
        data_dict = ReadYaml(self.filename).get_datas()
        # 序列化处理
        data = ast.literal_eval(data_dict)
        print()
        res = requests.post(url=url, json=data, headers={"Content-Type": "application/json"})
        return res


<<<<<<< HEAD


=======
>>>>>>> 95660efb742602ff5d550a3a30387fe13d6c9e8f
if __name__ == '__main__':
    re = ReadYaml('导出单据数据到json').get_datas()
    print()
    r = RTS(hosttype='对接接口', filename='导出单据数据到json').rts()
    print()
<<<<<<< HEAD
    print(r)
=======
    print(r)
>>>>>>> 95660efb742602ff5d550a3a30387fe13d6c9e8f
