#coding=utf-8
'''
登录测试
'''
import time
import unittest
import demjson
from src.common_functions.data_operations import DataOperations
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.qt_operations import QT_Operations

class TestcaseLogin(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup() #本地用chrome浏览器打开后台地址

    def testcase_login(self):

        QT_Operations().login()
        time.sleep(2)
        # WebDriverHelp().geturl('http://s2.checheweike.com/erp/index.php?route=stock/count/insert')
        # time.sleep(1)
        # WebDriverHelp().selectvalue("byxpath", "//*[@id='content']/div/div[2]/form/div[2]/table/tbody/tr[1]/td[2]/select", u"销售退款")
        # time.sleep(1)

        # WebDriverHelp().geturl('http://s2.checheweike.com/erp/index.php?route=finance/expense/insert')
        # time.sleep(0.5)
        # WebDriverHelp().clickitem('byxpath', '//*[@id="content"]/div/div[2]/form/div[1]/div[1]/div')
        # WebDriverHelp().switoiframe('xubox_iframe')
        # time.sleep(0.5)
        # WebDriverHelp().doubleclick('byxpath', '//*[@id="dialog-container"]/div/div[2]/table/tbody/tr[1]/td[1]')
        # WebDriverHelp().clickitem('byid', 'tree_3span')
        # print WebDriverHelp().gettext('byxpath', '//*[@id="dialog-container"]/div/div[2]/table/tbody/tr[1]/td[1]')
        WebDriverHelp().clickitem('byxpath', '//*[@id="menu-checkstand"]/a/span')
        time.sleep(1)
        x = WebDriverHelp().getelements('//*[@id="menu-checkstand"]/ul/li')
        for i in range(1, len(x), 1):  # 点击收银台下的菜单
            xpath = '//*[@id="menu-checkstand"]/ul/li[%d]/a' % i
            WebDriverHelp().clickitem('byxpath', xpath)
            time.sleep(1)

        time.sleep(3)

    def tearDown(self):
        WebDriverHelp().teardown() #关闭浏览器
