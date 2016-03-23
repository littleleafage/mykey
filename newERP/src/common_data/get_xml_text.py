# -*- coding: utf-8 -*-
'''
获取工单列表的参数
'''
from src.common_functions.file_oper import FileOpera


class GetXmlText(object):
    global DATA_OPERA, NODE

    def __init__(self, filename, node):
        data_opera = FileOpera(filename)
        self.DATA_OPERA = data_opera
        self.NODE = node

    def get_search(self):
        path = self.NODE
        return self.DATA_OPERA.read_texts(path)

    def get_xml_text(self, tag_name):
        path = self.NODE + '/' + tag_name
        return self.DATA_OPERA.read_xml(path)



