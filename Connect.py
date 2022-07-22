import os

import requests
import yaml

# "secretKey":"B5599595-21CB-0C45-D491-04EA48DC235D"

connect_path = os.path.abspath(".")
yaml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'connect.yaml')


def read_yaml():
    with open(yaml_path, 'r', encoding='utf-8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        return res

def connect(yaml_data):
    print(res)
    if uri == '/RebateAgreement/RebateReceipt':
        # data =
    r = requests.post(url=f'http://192.168.1.12:9999/Api' + {uri}, data=)


if __name__ == '__main__':
    print(read_yaml()())