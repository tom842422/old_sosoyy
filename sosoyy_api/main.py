from sosoyy_api.untils.writefile import writefile

if __name__ == '__main__':
    """ 
    hosttype：对接接口/内部接口
    filename：采购入库单/采购退货单/配送出库单/零售销售单/批发销售单/付款单/
    导出单据数据到excel/导出单据数据到json
    """
    re = writefile('对接接口', '配送出库单')
