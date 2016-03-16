#coding=utf-8
'''
数据查询
'''
import time
import unittest
from src.common_functions.file_oper import DataOperations
from src.common_functions.qt_operations import QT_Operations
from src.common_functions.webdriver_help import WebDriverHelp

class Search(unittest.TestCase):

    def setUp(self):
        WebDriverHelp('open', 'chrome', 'local').setup()

    def test_search(self):
        dataoper = DataOperations('orderlist.xml')
        QT_Operations().login()
        try:
            WebDriverHelp().geturl('http://192.168.1.111/ccwk/erp/index.php?route=order/order')
            time.sleep(0.5)
            WebDriverHelp().clickitem('byxpath', '')
        except:
            pass
        carlicense = ['byxpath', dataoper.read_xml('orderlist', 0, 'car_license'), dataoper.read_xml('orderlist', 0, 'license')]
        bustype = ['byxpath', dataoper.read_xml('orderlist', 0, 'business_type'), u'保险']
        searbtn = ['byclassname', dataoper.read_xml('orderlist', 0, 'search_btn')]
        searchdata = []
        searchdata.append(carlicense)
        searchdata.append(bustype)
        searchdata.append(searbtn)
        try:
            WebDriverHelp().inputclear(searchdata)
        except:
            pass
        QT_Operations().search(searchdata)
        time.sleep(0.5)

        QT_Operations().logout()

    def tearDown(self):
        WebDriverHelp().teardown()