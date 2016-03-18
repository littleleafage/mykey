# -*- coding: utf-8 -*-
'''
获取登录的参数
'''
from src.common_functions.file_oper import FileOpera


class LoginData(object):
    global DATA_OPERA, NODE

    def __init__(self, first_node):
        data_opera = FileOpera('login_data.xml')
        self.DATA_OPERA = data_opera
        self.NODE = first_node

    def get_store_id(self, tag_node):
        path = self.NODE + '/' + tag_node  # 节点的路径,如：login/username
        return self.DATA_OPERA.read_xml(path)

    def get_username(self, tag_node):
        path = self.NODE + '/' + tag_node
        return self.DATA_OPERA.read_xml(path)

    def get_password(self, tag_node):
        path = self.NODE + '/' + tag_node
        return self.DATA_OPERA.read_xml(path)

    def get_login_btn(self, tag_node):
        path = self.NODE + '/' + tag_node
        return self.DATA_OPERA.read_xml(path)

    def get_logout_url(self, tag_node):
        path = self.NODE + '/' + tag_node
        return self.DATA_OPERA.read_xml(path)



