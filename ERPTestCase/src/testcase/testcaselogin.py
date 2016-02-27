#coding=utf-8
import time
import unittest
from src.common_functions.data_opera import DataOpera
from src.common_functions.qt_opera import QT_Opera
from src.common_functions.webdriver_help import WebDriverHelp

class TestCaseLogin(unittest.TestCase):
    def setUp(self):

        WebDriverHelp("open", "chrome", "local").setup("http://s2.checheweike.com/erp")

    def testcase_login(self):
        '''
        测试登录及登出
        :return:
        '''
        data = DataOpera("testcase_login.xml")
        storeid = data.read_xml('login', 0, 'storeid')
        username = data.read_xml('login', 0, 'username')
        password = data.read_xml('login', 0, 'password')
        loginbtn = data.read_xml('login', 0, 'loginbtn')
        loginuser = data.read_xml('login', 0, 'checkusername')
        try:
            QT_Opera().login(storeid, username, password, loginbtn)
            self.assertEqual(WebDriverHelp().gettext("byxpath", loginuser), username)#判断登录用户是否正确
            print 'succeed'
        except:
            WebDriverHelp().screenshot("loginerr.jpg")
            print 'failed to login'
    # def testcase_logout(self):
    #     self.testcase_login()
    #     data = DataOpera("testcase_login.xml")
        logouturl = data.read_xml('login', 0, 'logouturl')
        QT_Opera().logout(logouturl)

    def tearDown(self):
        WebDriverHelp().teardown()
