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
        list_xpath = OrderList('list').get_search()
        list_value = OrderList('list_data').get_search()
        try:
            length = len(list_xpath)
            data_length = len(list_value)
            for i in range(0, length-2, 1):
                for j in range(i, data_length, 1):
                    if i == j:
                        try:
                            WebDriverHelp().input_value('xpath', list_xpath[i], list_value[j])
                        except:
                            WebDriverHelp().select_value('xpath', list_xpath[i], list_value[j])
                        WebDriverHelp().click_item('class_name', list_xpath[length-1])
                        time.sleep(0.3)
                        WebDriverHelp().screen_shot(0, 'Search-result' + str(i) + '.png')
        except:
            WebDriverHelp().screen_shot(1, 'Order-list.png')  # 截取工单列表

