import requests
import time
import json
from untils.read_yaml import ReadYaml
from untils.read_ini import ReadIni
import yaml
import random
from untils.embellish_yaml import render


class RTS:
    def __init__(self, hosttype, filename):
        self.filename = filename
        self.hosttype = hosttype

    @render
    def rts(self):
        url = ReadIni(self.hosttype).read_ini() + ReadYaml(self.filename).get_uri()
        data_dict = ReadYaml(self.filename).get_datas()
        data = (json.dumps(data_dict, ensure_ascii=False))
        print(data)
        res = requests.post(url=url, params=data, headers={"Content-Type": "application/json"})
        return res


if __name__ == '__main__':
    r = RTS(hosttype='对接接口', filename='采购入库单').rts()
    print(r, '\n', r.json())
