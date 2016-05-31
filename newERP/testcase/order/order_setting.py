# -*- coding: utf-8 -*-
import unittest, time
from common.webdriver_help import WebDriverHelp
from pageobject.login.login import Login
from pageobject.web.order.order import OrderSetting
from ddt import ddt, data, unpack


@ddt
class OrderSettingTest(unittest.TestCase):

    def setUp(self):
        WebDriverHelp('open', 'chrome', 'local').setup()
        time.sleep(0.5)
        Login().login('10008', 'yewen', 'ccwk0715')

    # 收银设置
    @data(('.//*[@id="menus"]/li[2]/ul/li[1]/a', 1), ('.//*[@id="menus"]/li[2]/ul/li[2]/a', 1),
          ('.//*[@id="menus"]/li[2]/ul/li[3]/a', 1), ('.//*[@id="menus"]/li[2]/ul/li[4]/a', 1))
    @unpack
    def test_check_stand(self, path, value):
        OrderSetting().get_route(path)
