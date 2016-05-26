# -*- coding: utf-8 -*-
from selenium import webdriver
from common.webdriver_help import WebDriverHelp

WebDriverHelp('open', 'chrome', 'local').setup()
WebDriverHelp().get_text('xpath', './/*[@id="form1"]/li[4]/input')
print 'somebody'
