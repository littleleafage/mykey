# -*- coding: utf-8 -*-
from pageobject.login.login import Login
from common.webdriver_help import WebDriverHelp
from ddt import ddt, data, unpack
import unittest


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup()

    @data(('***', '******', '*****'))  # 登录帐号
    @unpack
    def test_login(self, store_id, username, password):
        # self.assertTrue(Login().verify_page())
        Login().login(store_id, username, password)
        self.assertTrue(Login().verify_success_login())

    def tearDown(self):
        Login().logout()

if __name__ == '__main__':
    unittest.main(verbosity=2)

