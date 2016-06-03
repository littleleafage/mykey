# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from ddt import ddt, data, unpack
from common.basepage import BasePage
from pageobject.login.login import Login
from pageobject.web.finance_page.finance_page import FinancePage
from common.menu_locator import FinancePath
from pageobject.web.finance_page.settlement_account_page import SettlementAccountPage


@ddt
class FinanceTest(unittest.TestCase):

    def setUp(self):
        BasePage("open", "chrome", "local").setup()
        time.sleep(1)
        Login().login("10008", "yewen", "ccwk0715")

    @data((FinancePath.SETTLEMENT_TYPE, 'autotest', 'autotest1'),
          (FinancePath.EXPENSE_TYPE, 'autotest', 'autotest1'),
          (FinancePath.INCOME_TYPE, 'autotest', 'autotest1'))
    @unpack
    def test_finance_type(self, loc, value, value1):
        FinancePage().get_route(*loc)
        FinancePage().init_data(value)
        FinancePage().add_data()
        self.assertTrue(FinancePage().check_data(value))
        FinancePage().update_data(value, value1)
        FinancePage().init_data(value)
        time.sleep(0.5)

    @data((FinanceMenu.SETTLEMENT_ACCOUNT, 'autotest'))
    @unpack
    def test_settlement_account(self, loc, value):
        SettlementAccountPage().get_route(*loc)
        SettlementAccountPage().init_data(value)
        SettlementAccountPage().add_data()
        self.assertTrue(SettlementAccountPage().check_data(value))
        SettlementAccountPage().update_data(value)
        SettlementAccountPage().init_data(value)
        time.sleep(0.5)

    def tearDown(self):
        Login().logout()
