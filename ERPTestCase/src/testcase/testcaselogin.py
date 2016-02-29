#coding=utf-8
import time
import unittest
from src.common_functions.data_opera import DataOpera
from src.common_functions.qt_opera import QT_Opera
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.dbopera import sqlOpera

class TestCaseLogin(unittest.TestCase):

    def testcase_login(self):
        '''
        测试登录及登出
        :return:
        '''
        QT_Opera().login()
        WebDriverHelp().geturl("http://s2.checheweike.com/erp/index.php?route=sale/sales/insert")
        data = sqlOpera().sql_select("select mobile from vip_user where name='叶雯'")
        WebDriverHelp().inputvalue('byid', 'appendedInputButtons', data[0])
        WebDriverHelp().clickitem('byxpath', '//*[@id="tab-general"]/div[2]/div[2]/button[1]')


    # def testcase_logout(self):
    #     self.testcase_login()
    #     data = DataOpera("testcase_login.xml")
    #     logouturl = data.read_xml('login', 0, 'logouturl')
    #     QT_Opera().logout(logouturl)

    # def tearDown(self):
    #     WebDriverHelp().teardown()
