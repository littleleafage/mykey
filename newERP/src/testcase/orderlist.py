#coding=utf-8
'''
工单列表
'''
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.qt_operations import QT_Operations
class orderList(object):

    def search(self):
        QT_Operations().search()