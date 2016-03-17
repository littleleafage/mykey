#coding=utf-8
'''
获取工单列表的参数
'''
from src.common_functions.file_oper import FileOpera


class OrderList(object):
    global DATA_OPERA, NODE

    def __init__(self, node):
        data_opera = FileOpera('order_list.xml')
        self.DATA_OPERA = data_opera
        self.NODE = node

    def get_advanced_btn(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'open_advanced_search')

    def get_license(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'car_license')

    def get_company(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'company')

    def get_bus_type(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'business_type')

    def get_receiver(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'receiver')

    def get_date_start(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'bill_date_start')

    def get_date_end(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'bill_date_end')

    def get_bill_no(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'no')

    def get_stock_status(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'stock_status')

    def get_audited(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'is_audited')

    def get_sub_store(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'sub_store')

    def get_search_btn(self):
        return self.DATA_OPERA.read_xml(self.NODE, 0, 'search_btn')





