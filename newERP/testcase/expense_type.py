# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from common.webdriver_help import WebDriverHelp
from pageobject.login.login import Login
from pageobject.web.expense_type import ExpenseType
from ddt import ddt, data, unpack


@ddt
class ExpenseType(unittest.TestCase):

    @data(("10008", "yewen", "ccwk0715"))
    @unpack
    def setUp(self, store_id, username, password):
        WebDriverHelp("open", "chrome", "local").setup()
        time.sleep(1)
        Login().login(store_id, username, password)

    @data()
    @unpack
    def test_expense_type(self, store_id, username, password):

        time.sleep(2)

    def tearDown(self):
        Login().logout()
