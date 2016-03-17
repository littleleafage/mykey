#coding=utf-8
'''
数据查询
'''
import time
import unittest
from src.common_data.order_list import OrderList
from src.common_functions.qt_operations import Operations
from src.common_functions.webdriver_help import WebDriverHelp


class Search(unittest.TestCase):

    def setUp(self):
        WebDriverHelp('open', 'chrome', 'local').setup()

    def test_search(self):

        Operations().login()
        try:
            WebDriverHelp().geturl('http://192.168.1.111/ccwk/erp/index.php?route=order/order')
            time.sleep(0.5)
            WebDriverHelp().click_item('xpath', OrderList().get_advanced_btn())
        except:
            pass
        search_data = []
        list_xpath = OrderList('list')
        list_data = OrderList('list_data')
        list_btn = OrderList('list_btn')
        car_license = [list_xpath.get_license(), list_data.get_license()]
        company = [list_xpath.get_company(), list_data.get_company()]
        bus_type = [list_xpath.get_bus_type(), list_data.get_bus_type()]  # 下拉列表
        receiver = [list_xpath.get_receiver(), list_data.get_receiver()]
        bill_start = [list_xpath.get_date_start(), list_data.get_date_start()]
        bill_end = [list_xpath.get_date_end(), list_data.get_date_end()]
        no = [list_xpath.get_bill_no(), list_data.get_bill_no()]
        stock_status = [list_xpath.get_stock_status(), list_data.get_stock_status()]
        audited = [list_xpath.get_audited(), list_data.get_audited()]
        sub_store = [list_xpath.get_sub_store(), list_data.get_sub_store()]
        sear_btn = [list_btn.get_search_btn()]
        search_data.append(car_license)
        search_data.append(company)
        search_data.append(bus_type)
        search_data.append(receiver)
        search_data.append(bill_start)
        search_data.append(bill_end)
        search_data.append(no)
        search_data.append(stock_status)
        search_data.append(audited)
        search_data.append(sub_store)
        search_data.append(sear_btn)

        Operations().search(search_data)
        time.sleep(0.5)

        Operations().logout()

    def tearDown(self):
        WebDriverHelp().teardown()

