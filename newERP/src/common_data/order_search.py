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

    def get_length(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.readxml_length(path)

    def get_advanced_btn(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_license(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_company(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_bus_type(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_receiver(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_date_start(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_date_end(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_bill_no(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_stock_status(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_audited(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_sub_store(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)

    def get_search_btn(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)





