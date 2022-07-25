import traceback
from sosoyy_3_api.untils.read_yaml import ReadYaml

from sosoyy_3_api.rebateapitest import RTS
from sosoyy_3_api.untils.read_ini import ReadIni

if __name__ == '__main__':
    try:
        """ 对接接口/内部接口
         采购入库单/采购退货单/配送出库单/零售销售单/批发销售单/付款单"""
        r_url = ReadIni('对接接口').read_ini() + ReadYaml('批发销售单').get_uri()
        result = RTS(hosttype='对接接口', filename='批发销售单').rts()
        print(r_url)
        print()
        print(result, '\n', result.json())
    except Exception as e:
        print(e.args)
        print("========")
        print(traceback.format_exc())
