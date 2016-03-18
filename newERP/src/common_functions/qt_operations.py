# -*- coding: utf-8 -*-
'''
存放具体的操作功能块，比如登录，退出等等
'''
import time
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_data.login_data import LoginData
from selenium.common.exceptions import NoSuchElementException as NSEE
from src.common_data.order_search import OrderList


class Operations(object):

    def login(self):
        try:
            login_data = LoginData('login')
            WebDriverHelp().input_value("name", "store_id", login_data.get_store_id('store_id'))
            WebDriverHelp().input_value("name", "username", login_data.get_username('username'))
            WebDriverHelp().input_value("name", "password", login_data.get_password('password'))
            WebDriverHelp().click_item('class_name', login_data.get_login_btn('login_btn'))
            time.sleep(1)
        except NSEE:
            WebDriverHelp().screen_shot(1, 'login.png')


    def logout(self):
        url = LoginData('logout').get_logout_url('logout_url')
        WebDriverHelp().geturl(url)
        time.sleep(1)

    def search(self):
        '''
        工单列表查询
        :param orderdata: 元素信息
        :return:
        '''
        list_xpath = OrderList('list')
        list_value = OrderList('list_data')
        try:
            WebDriverHelp().input_value('xpath', list_xpath.get_license('car_license'), list_value.get_license('car_license'))
            WebDriverHelp().input_value('xpath', list_xpath.get_company('company'), list_value.get_company('company'))
            WebDriverHelp().select_value('xpath', list_xpath.get_bus_type('business_type'), list_value.get_bus_type('business_type'))  # 下拉列表
            WebDriverHelp().select_value('xpath', list_xpath.get_receiver('receiver'), list_value.get_receiver('receiver'))
            WebDriverHelp().input_value('xpath', list_xpath.get_date_start('bill_date_start'), list_value.get_date_start('bill_date_start'))
            WebDriverHelp().input_value('xpath', list_xpath.get_date_end('bill_date_end'), list_value.get_date_end('bill_date_end'))
            WebDriverHelp().input_value('xpath', list_xpath.get_bill_no('no'), list_value.get_bill_no('no'))
            WebDriverHelp().select_value('xpath', list_xpath.get_stock_status('stock_status'), list_value.get_stock_status('stock_status'))
            WebDriverHelp().select_value('xpath', list_xpath.get_audited('is_audited'), list_value.get_audited('is_audited'))
            WebDriverHelp().select_value('xpath', list_xpath.get_sub_store('sub_store'), list_value.get_sub_store('sub_store'))
            WebDriverHelp().click_item('xpath', list_xpath.get_search_btn('search_btn'))
        except:
            WebDriverHelp().screen_shot(1, 'Order-list.png')  # 截取工单列表

