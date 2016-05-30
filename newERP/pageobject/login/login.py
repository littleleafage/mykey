# -*- coding: utf-8 -*-
# 登录登出模块功能
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from common.webdriver_help import WebDriverHelp
import time
from ddt import ddt, data, unpack


class Login(object):

    logout_url = 'https://www.checheweike.com/web/index.php?route=common/logout'
    store_id = 'store_id'
    username = 'username'
    password = 'password'
    login_btn = 'login-btn'
    page_title = u'车车云智慧系统-商户登录'
    login_verify = 'top-user-logout'

    def login(self, store_id, username, password):
        WebDriverHelp().input_value('name', self.store_id, store_id)
        WebDriverHelp().input_value('name', self.username, username)
        WebDriverHelp().input_value('name', self.password, password)
        WebDriverHelp().click_item('class_name', self.login_btn)
        time.sleep(0.5)

    def logout(self):
        WebDriverHelp().geturl(self.logout_url)
        time.sleep(0.5)
        WebDriverHelp().teardown()

    def verify_page(self):
        value = WebDriverHelp().get_page_title()
        if value == self.page_title:
            return True
        else:
            raise AssertionError('Login page is wrong')

    def verify_success_login(self):
        if WebDriverHelp().is_element_displayed('id', self.login_verify):
            return True
        else:
            raise AssertionError('Failed to login')

