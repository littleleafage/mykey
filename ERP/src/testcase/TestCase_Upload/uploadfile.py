#coding=utf-8
'''
退出登录测试
'''
import time
import unittest

from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.data_operations import DataOperations
from src.common_functions.qt_operations import QT_Operations

class TestCaseFile(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup("houtai") #本地用chrome浏览器打开后台地址
    def testcase_file(self):
        filepath = "../../error/1.jpg"
        dataoper = DataOperations("TestCase_QT_Login.xml")
        QT_Operations().login(dataoper.read_xml('login', 0, 'storeid'), dataoper.read_xml('login', 0, 'username'), dataoper.read_xml('login', 0, 'password'), dataoper.read_xml('login', 0, "loginbtn"))
        time.sleep(1)
        loadpath = [dataoper.read_xml('weixin', 0, "crm"), dataoper.read_xml('weixin', 0, "wx"), dataoper.read_xml('weixin', 0, "qunfa"), dataoper.read_xml('weixin', 0, "sucaiguanli"), dataoper.read_xml('weixin', 0, "add")]

        try:
            QT_Operations().upload("byid", loadpath, dataoper.read_xml('weixin', 0, "uploadbtn"))
            print "上传成功"
        except:
            WebDriverHelp().screenshot('weixin_uploaderr.img')
            print "上传失败"
        time.sleep(4)


    def tearDown(self):
        WebDriverHelp().teardown() #关闭浏览器

