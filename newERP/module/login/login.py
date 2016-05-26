# -*- coding: utf-8 -*-
# 登录登出模块功能
from selenium import webdriver
from selenium.webdriver.support.ui import  Select
from selenium.common.exceptions import NoSuchElementException
from common.webdriver_help import WebDriverHelp
import time


class Login(object):

    def login(self):
        WebDriverHelp('open', 'chrome', 'local').setup()
        WebDriverHelp().input_value('name', 'store_id', '10008')
        WebDriverHelp().input_value('name', 'username', 'yewen')
        WebDriverHelp().input_value('name', 'password', 'ccwk0715')
        WebDriverHelp().click_item('class_name', 'login-btn')
        time.sleep(0.5)
        result = WebDriverHelp().check('xpath', '/html/body/div[1]/article/section/ul/li[1]/a/h3', 'CRM')
        if result:
            print 'success to login'
        else:
            print 'failed to login'

    def logout(self):
        WebDriverHelp().geturl('https://www.checheweike.com/web/index.php?route=common/logout')
