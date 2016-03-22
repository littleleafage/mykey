# -*- coding: utf-8 -*-
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

    # def get_length(self):
    #     path = self.NODE
    #     return self.DATA_OPERA.readxml_length(path)

    def get_search(self):
        path = self.NODE
        return self.DATA_OPERA.read_texts(path)

    def get_advanced_btn(self):
        path = self.NODE + '/open_advanced_search'
        return self.DATA_OPERA.read_xml(path)

    def get_license(self):
        path = self.NODE + '/car_license'
        return self.DATA_OPERA.read_xml(path)

    def get_company(self):
        path = self.NODE + '/company'
        return self.DATA_OPERA.read_xml(path)

    def get_bus_type(self):
        path = self.NODE + '/business_type'
        return self.DATA_OPERA.read_xml(path)

    def get_receiver(self):
        path = self.NODE + '/receiver'
        return self.DATA_OPERA.read_xml(path)

    def get_date_start(self):
        path = self.NODE + '/bill_date_start'
        return self.DATA_OPERA.read_xml(path)

    def get_date_end(self):
        path = self.NODE + '/bill_date_end'
        return self.DATA_OPERA.read_xml(path)

    def get_bill_no(self):
        path = self.NODE + '/no'
        return self.DATA_OPERA.read_xml(path)

    def get_sub_store(self):
        path = self.NODE + '/sub_store'
        return self.DATA_OPERA.read_xml(path)

    def get_search_btn(self):
        path = self.NODE + '/search_btn'
        return self.DATA_OPERA.read_xml(path)





