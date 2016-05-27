# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from common.webdriver_help import WebDriverHelp
from module.login.login import Login
from module.setting.expense_type import ExpenseType
from ddt import ddt, data, unpack


@ddt
class ERPTest(unittest.TestCase):

    def setUp(self):
        # Login().login()
        # time.sleep(1)
        WebDriverHelp("open", "chrome", "local").setup()

    @data(("10008", "yewen", "ccwk0715"), ("10008", "yewen", "ccwk1234"))
    @unpack
    def test_expense_type(self, store_id, username, password):
        WebDriverHelp().input_value('name', 'store_id', store_id)
        WebDriverHelp().input_value('name', 'username', username)
        WebDriverHelp().input_value('name', 'password', password)
        time.sleep(2)
        # ExpenseType().get_route()
        # ExpenseType().delete_data('autotest')
        # ExpenseType().add_data()
        # ExpenseType().update_data()
        # ExpenseType().delete_data('autotest')

    def tearDown(self):
        # Login().logout()
        # time.sleep(0.5)
        WebDriverHelp().teardown()
