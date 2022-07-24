import requests
import time
import json
from untils.read_yaml import ReadYaml
from untils.read_ini import ReadIni


class RTS:
    def __init__(self, hosttype, filename):
        self.filename = filename
        self.hosttype = hosttype

    def rts(self):
        url = ReadIni(self.hosttype).read_ini() + ReadYaml(self.filename).get_uri()
        data = ReadYaml(self.filename).get_datas()
        r = requests.post(url=url, data=data)
        return r


if __name__ == '__main__':
    r = RTS(hosttype='对接接口', filename='采购入库单').rts()
    print(r)
