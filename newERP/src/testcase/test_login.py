# -*- coding: utf-8 -*-
'''
登录测试
date_added：2016-03-18
'''
from src.common_data.login_data import LoginData
from src.common_functions.qt_operations import Operations
from src.common_functions.webdriver_help import WebDriverHelp
import time
import unittest


class Login(unittest.TestCase):

    def setUp(self):
        WebDriverHelp('open', 'chrome', 'local').setup()

    def test_login(self):
        Operations().login()
        login_user = WebDriverHelp().get_text('xpath', '//*[@id="header-nav-user"]/div/a/span')  # 获取登录后的用户名
        username = LoginData('login').get_username('username')  # 登陆用户
        if login_user == username:
            print '登录成功'
        else:
            print '登陆用户错误'
            WebDriverHelp().screen_shot(1, 'login-user.png')
        time.sleep(0.5)
        Operations().logout()

    def tearDown(self):
        WebDriverHelp().teardown()

