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
        self.filename = filename
        self.hosttype = hosttype

    def rts(self):
        url = ReadIni(self.hosttype).read_ini() + ReadYaml(self.filename).get_uri()
        data_dict = ReadYaml(self.filename).get_datas()
        data = ast.literal_eval(data_dict)
        print()
        res = requests.post(url=url, json=data, headers={"Content-Type": "application/json"})
        return res




if __name__ == '__main__':
    re = ReadYaml('导出单据数据到json').get_datas()
    print()
    r = RTS(hosttype='对接接口', filename='导出单据数据到json').rts()
    print()
    print(r)