import code
import os
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
        res = requests.post(url=url, json=data, headers={"Content-Type": "application/json"})
        return res


if __name__ == '__main__':
    host_type = input('请输入接口类型:')
    file_name = input('请输入单据类型:')
    r = RTS(hosttype=host_type, filename=file_name).rts()
    print(r, '\n', r.json())
    time.sleep(20)
    code.interact(banner="", local=locals())
