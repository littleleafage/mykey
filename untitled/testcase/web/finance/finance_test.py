# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from ddt import ddt, data, unpack
from common.basepage import BasePage
from pageobject.login.login import Login
from pageobject.web.finance.finance_page import FinancePage
from common.menu_locator import FinanceMenu


@ddt
class FinanceTest(unittest.TestCase):

    def setUp(self):
        BasePage("open", "chrome", "local").setup()
        time.sleep(1)
        Login().login("10008", "yewen", "ccwk0715")

    @data((FinanceMenu.SETTLEMENT_TYPE, 'autotest', 'autotest1'),
          (FinanceMenu.EXPENSE_TYPE, 'autotest', 'autotest1'),
          (FinanceMenu.INCOME_TYPE, 'autotest', 'autotest1'))
    @unpack
    def test_finance_type(self, loc, value, value1):
        FinancePage().get_route(*loc)
        FinancePage().init_data(value)
        FinancePage().add_data()
        self.assertTrue(FinancePage().check_data(value))
        FinancePage().update_data(value, value1)
        FinancePage().init_data(value)
        time.sleep(0.5)

    @data((FinanceMenu.SETTLEMENT_ACCOUNT, 'autotest', 'autotest1'))
    @unpack
    def test_settlement_account(self, loc, value):
        FinancePage().get_route(*loc)
        FinancePage().init_data(value)

    def tearDown(self):
        Login().logout()