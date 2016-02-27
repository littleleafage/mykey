#coding=utf-8
'''
登录测试
'''
import time
import unittest

from src.common_functions.data_operations import DataOperations
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.qt_operations import QT_Operations

class TestcaseLogin(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup() #本地用chrome浏览器打开后台地址

    def testcase_login(self):
        dataoper = DataOperations("TestCase_QT_Login.xml")
        QT_Operations().login(dataoper.read_xml('login', 0, 'storeid'), dataoper.read_xml('login', 0, 'username'), dataoper.read_xml('login', 0, 'password'), dataoper.read_xml('login', 0, "loginbtn"))
        time.sleep(2)
        WebDriverHelp().geturl('http://s2.checheweike.com/erp/index.php?route=finance/other_income/insert')
        time.sleep(1)
        # WebDriverHelp().selectvalue("byxpath", "//*[@id='content']/div/div[2]/form/div[2]/table/tbody/tr[1]/td[2]/select", u"销售退款")
        # time.sleep(3)

        QT_Operations().logout(dataoper.read_xml('login', 0, 'logouturl')) #退出登录
        time.sleep(1)

    def tearDown(self):
        WebDriverHelp().teardown() #关闭浏览器

