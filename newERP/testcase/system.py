# -*- coding: utf-8 -*-
import unittest, time
from common.webdriver_help import WebDriverHelp
from pageobject.login.login import Login
from pageobject.web.system import System


class SystemTest(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup()
        time.sleep(1)
        Login().login("10008", "yewen", "ccwk0715")

    def test_route(self):
        System().get_system()

if __name__ == '__main__':
    unittest.main(verbosity=2)

