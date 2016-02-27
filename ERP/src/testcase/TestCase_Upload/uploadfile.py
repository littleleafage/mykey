#coding=utf-8
'''
退出登录测试
'''
import time
import unittest

from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.data_operations import DataOperations
from src.common_functions.qt_operations import QT_Operations
from selenium.common.exceptions import WebDriverException

class TestCaseFile(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup() #本地用chrome浏览器打开后台地址
    def testcase_file(self):
        dataoper = DataOperations("TestCase_QT_Login.xml")
        QT_Operations().login(dataoper.read_xml('login', 0, 'storeid'), dataoper.read_xml('login', 0, 'username'), dataoper.read_xml('login', 0, 'password'), dataoper.read_xml('login', 0, "loginbtn"))
        time.sleep(1)
        WebDriverHelp().geturl(dataoper.read_xml('menu', 0, "service-url"))
        time.sleep(1)
        WebDriverHelp().clickitem("byxpath", dataoper.read_xml('menu', 0, "modify"))
        time.sleep(1)
        WebDriverHelp().switoiframe("xubox_iframe")
        time.sleep(1)
        WebDriverHelp().inputvalue("byname", "name", "jkslkk")
        time.sleep(13)

    # def tearDown(self):
    #     WebDriverHelp().teardown() #关闭浏览器

