#coding=utf-8
'''
获取登录的参数
'''
from src.common_functions.file_oper import FileOpera


class Login(object):
    global DATA_OPERA

    def __init__(self):
        data_opera = FileOpera('login_data.xml')
        self.DATA_OPERA = data_opera

    def get_store_id(self):
        return self.DATA_OPERA.read_xml('login', 0, 'store_id')

    def get_username(self):
        return self.DATA_OPERA.read_xml('login', 0, 'username')

    def get_password(self):
        return self.DATA_OPERA.read_xml('login', 0, 'password')

    def get_login_btn(self):
        return self.DATA_OPERA.read_xml('login', 0, 'login_btn')

    def get_logout_url(self):
        return self.DATA_OPERA.read_xml('logout', 0, 'logout_url')



