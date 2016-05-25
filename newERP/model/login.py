# -*- coding: utf-8 -*-
'''
存放公用的方法
'''
from selenium import webdriver
from selenium.webdriver.support.ui import  Select
from selenium.common.exceptions import NoSuchElementException
from common.webdriver_help import WebDriverHelp

class Login(object):

    def login(self):
        WebDriverHelp('open', 'chrome', 'local').setup()
