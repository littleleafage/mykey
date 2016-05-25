# -*- coding: utf-8 -*-
# 测试用例
from common.webdriver_help import WebDriverHelp
from model.login import Login
from model.expense_type import ExpenseType
import unittest, time


class ERPTest(unittest.TestCase):

    def setUp(self):
        Login().login()
        time.sleep(0.5)
        WebDriverHelp().check('xpath', '/html/body/div[1]/article/section/ul/li[1]/a/h3', 'CRM')

    def test_expense_type(self):
        ExpenseType().get_route()
        time.sleep(0.5)
        ExpenseType().delete_data('autotest')
        time.sleep(0.5)
        ExpenseType().add_data()
        time.sleep(0.5)
        ExpenseType().update_data()
        time.sleep(1)

    def tearDown(self):
        Login().logout()
        time.sleep(0.5)
        WebDriverHelp().teardown()
