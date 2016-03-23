# -*- coding: utf-8 -*-
'''
数据查询
'''
import time
import unittest
from src.common_data.get_xml_text import GetXmlText
from src.common_functions.qt_operations import Operations
from src.common_functions.webdriver_help import WebDriverHelp
from selenium.common.exceptions import NoSuchElementException


class Search(unittest.TestCase):

    def setUp(self):
        WebDriverHelp('open', 'chrome', 'local').setup()

    def test_search(self):

        Operations().login()
        time.sleep(0.5)
        try:
            WebDriverHelp().click_item('link_text', 'ERP')
            time.sleep(1.5)
            WebDriverHelp().click_item('xpath', '/html/body/aside/div/ul/li[4]/a')
            time.sleep(0.5)
            WebDriverHelp().click_item('xpath', '/html/body/div/div/section/ul/li[1]/a')
            time.sleep(0.5)
        except NoSuchElementException:
            pass

        Operations().search('rep_purchase.xml', 'Search-Purchase', 'purchase', 'pur_data')
        time.sleep(0.5)

        # Operations().logout()

    # def tearDown(self):
    #     WebDriverHelp().teardown()

