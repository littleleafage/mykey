#coding=utf-8
'''
数据查询
'''
import unittest
from src.common_functions.qt_operations import QT_Operations
from src.common_functions.webdriver_help import WebDriverHelp
class Search(unittest.TestCase):

    def search(self):
        logindata = []
        QT_Operations().login(logindata)
        searchdata = []
        QT_Operations().search(searchdata)

        QT_Operations().logout('')

    def tearDown(self):
        WebDriverHelp().teardown()