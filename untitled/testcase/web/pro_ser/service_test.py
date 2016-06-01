# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from ddt import ddt, data, unpack
from common.basepage import BasePage
from pageobject.login.login import Login
from pageobject.web.finance_page.finance_page import FinancePage
from common.menu_locator import FinanceMenu
from pageobject.web.pro_serv_page.product_page import ProductPage


@ddt
class ProductTest(unittest.TestCase):

    def setUp(self):
        BasePage("open", "chrome", "local").setup()
        time.sleep(1)
        Login().login("10008", "yewen", "ccwk0715")

    @data(('autotest', 'autotest1'))
    @unpack
    def test_product(self, value, value1):
        ProductPage().get_route()
        ProductPage().init_data(value)
        # ProductPage().add_data(value)
        # self.assertTrue(ProductPage().check_data(value))
        # ProductPage().update_data(value)
        # ProductPage().init_data(value)
        time.sleep(0.5)

    def tearDown(self):
        Login().logout()
