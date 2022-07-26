import time
from sosoyy_3_api.untils.readyaml import ReadYaml

from sosoyy_3_api.untils.rebateapitest import RTS
from sosoyy_3_api.untils.read_ini import ReadIni

if __name__ == '__main__':
    """ 
    hosttype：对接接口/内部接口
    filename：采购入库单/采购退货单/配送出库单/零售销售单/批发销售单/付款单/导出单据数据到excel/导出单据数据到json
    """
    host_1 = '对接接口'
    fname_1 = '配送出库单'
    host_2 = '对接接口'
    fname_2 = '零售销售单'
    r_url = ReadIni(host_1).read_ini() + ReadYaml(fname_1).get_uri()
    r_data = ReadYaml(fname_1).get_datas()
    result = RTS(hosttype=host_1, filename=fname_1).rts()
    time.time()
    print(r_url, '\n', result.json())
    nt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(f'{host_1}已写入数据.txt', 'a+', encoding='utf8') as f:
        f.write('\n' + fname_1 + '    ' + nt + '\n' + r_url + '\n' + r_data + '\n')
    print('**********************************华丽的分割线**********************************', end=' ')
    r_url = ReadIni(host_2).read_ini() + ReadYaml(fname_2).get_uri()
    r_data = ReadYaml(fname_2).get_datas()
    result = RTS(hosttype=host_2, filename=fname_2).rts()
    print(r_url, '\n', result.json())
    with open(f'{host_2}已写入数据.txt', 'a+', encoding='utf8') as f:
        f.write('\n' + fname_2 + '    ' + nt + '\n' + r_url + '\n' + r_data + '\n')
