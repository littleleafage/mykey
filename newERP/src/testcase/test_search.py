# -*- coding: utf-8 -*-
'''
数据查询
'''
import time
import unittest
from src.common_data.order_search import OrderList
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
            WebDriverHelp().geturl('http://192.168.1.111/ccwk/erp/#/order/list')
            # WebDriverHelp().click_item('link_text', 'ERP')
            # WebDriverHelp().click_item('link_text', u'汽修开单')
            # time.sleep(0.5)
            # WebDriverHelp().click_item('link_text', u"工单")
            time.sleep(0.5)
            WebDriverHelp().click_item('xpath', OrderList('list').get_advanced_btn())
        except NoSuchElementException:
            pass

        Operations().search()
        time.sleep(0.5)

        # Operations().logout()

    # def tearDown(self):
    #     WebDriverHelp().teardown()

