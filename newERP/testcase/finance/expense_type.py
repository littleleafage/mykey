# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from ddt import ddt, data, unpack

from common.webdriver_help import WebDriverHelp
from pageobject.login.login import Login
from pageobject.web.finance.finance import FinanceType


@ddt
class FinanceTest(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup()
        time.sleep(1)
        Login().login("10008", "yewen", "ccwk0715")

    @data(('.//*[@id="menus"]/li[8]/ul/li[2]/a', 'autotest', 'autotest1'),
          ('.//*[@id="menus"]/li[8]/ul/li[3]/a', 'autotest', 'autotest1'),
          ('.//*[@id="menus"]/li[8]/ul/li[4]/a', 'autotest', 'autotest1'))
    @unpack
    def test_finance_type(self, path, value, value1):
        FinanceType().get_route(path)
        FinanceType().init_data(value)
        FinanceType().add_data()
        self.assertTrue(FinanceType().check_data(value))
        FinanceType().update_data(value, value1)
        FinanceType().init_data(value)
        time.sleep(1)

    @data(('.//*[@id="menus"]/li[8]/ul/li[1]/a', 'autotest', 'autotest1'))
    @unpack
    def test_settlement_account(self, path):
        FinanceType().get_route(path)

    def tearDown(self):
        Login().logout()
