#coding=utf-8
import time
import unittest
from src.common_functions.data_opera import DataOpera
from src.common_functions.qt_opera import QT_Opera
from src.common_functions.webdriver_help import WebDriverHelp
from src.testcase.testcaselogin import TestCaseLogin

class TestCaseUpload(unittest.TestCase):

    def testcase_upload(self):
        '''
        测试登录及登出
        :return:
        '''
        data = DataOpera("testcase_login.xml")
        QT_Opera().login()
        WebDriverHelp().geturl(data.read_xml('wx', 0, 'addurl'))
        time.sleep(1)
        WebDriverHelp().uploadfile('byid', 'file', 'G:\\webdriver\\ERPTestCase\\test.jpg')
        time.sleep(2)
        # WebDriverHelp().switchto('alert', '')
        # time.sleep(1)
        WebDriverHelp().clickitem('byxpath', "//*[@id='xubox_layer1']/div/span/a")

    def tearDown(self):
        WebDriverHelp().teardown()
