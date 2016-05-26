# -*- coding: utf-8 -*-
# 测试用例
import time
import unittest

from common.webdriver_help import WebDriverHelp
from module.login.login import Login
from module.setting.expense_type import ExpenseType


class ERPTest(unittest.TestCase):

    def setUp(self):
        Login().login()
        time.sleep(1)

    def test_expense_type(self):
        ExpenseType().get_route()
        ExpenseType().delete_data('autotest')
        ExpenseType().add_data()
        ExpenseType().update_data()
        ExpenseType().delete_data('autotest')

    def tearDown(self):
        Login().logout()
        time.sleep(0.5)
        WebDriverHelp().teardown()
