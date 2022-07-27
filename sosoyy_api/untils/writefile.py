import time

from sosoyy_api.untils.readini import ReadIni
from sosoyy_api.untils.readyaml import ReadYaml
from sosoyy_api.untils.rebateapitest import RTS


def writefile(host, fname):
    nt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    r_url = ReadIni(host).read_ini() + ReadYaml(fname).get_uri()
    r_data = ReadYaml(fname).get_datas()
    result = RTS(hosttype=host, filename=fname).rts()
    try:
        if fname in ['采购入库单', '采购退货单', '配送出库单', '零售销售单', '批发销售单', '付款单']:
            with open(f'{host}已写入数据.txt', 'a+', encoding='utf8') as f:
                f.write('\n' + fname + '    ' + nt + '\n' + r_url + '\n' + r_data + '\n')
            return print(f'成功\n接口类型：{host}\n单据类型：{fname}')
        else:
            with open(f'{host}已写入数据.txt', 'a+', encoding='utf8') as f:
                f.write('\n' + fname + '  ' + nt + '\n' + result.content.decode())
            return print(f'成功!\n接口类型：{host}\n返回的数据类型：{fname}')
    except Exception as e:
        with open(f'{host}已写入数据.txt', 'a+', encoding='utf8') as f:
            f.write(f'\n{e}\n{fname}  \n{r_url} \n{r_data}\n')
        return print(e)
