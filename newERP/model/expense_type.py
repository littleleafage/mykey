# -*- coding: utf-8 -*-
# 登录登出模块功能

from common.webdriver_help import WebDriverHelp
from selenium.webdriver.common.action_chains import Keys
import time


class ExpenseType(object):

    def get_route(self):
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/article/section/ul/li[3]/a')
        time.sleep(0.5)
        WebDriverHelp().click_item('xpath', '//*[@id="menus"]/li[8]/a')
        time.sleep(0.5)
        WebDriverHelp().click_item('xpath', '//*[@id="menus"]/li[8]/ul/li[3]/a')

    def check_data(self, value):  # 检查数据
        WebDriverHelp().search('xpath', '/html/body/div[1]/div[2]/div/article/header/div/div/input', value)
        time.sleep(0.5)
        try:
            result = WebDriverHelp().check('xpath', '//*[@id="data-table"]/tbody/tr/td[2]', value)
            if result:
                return True
            else:
                return False
        except:
            pass

    def delete_data(self, value):
        result = self.check_data(value)
        if result:
            WebDriverHelp().click_item('xpath', '//*[@id="data-table"]/tbody/tr/td[1]/span[2]/a')
            WebDriverHelp().switch()
        else:
            pass

    def add_data(self):  # 添加
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/div[2]/div/article/header/div/a')
        time.sleep(0.5)
        WebDriverHelp().input_value('xpath', '/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input', 'autotest')
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/div/div/div[3]/button[1]')

    def update_data(self):
        WebDriverHelp().search('xpath', '/html/body/div[1]/div[2]/div/article/header/div/div/input', 'autotest')
        time.sleep(0.5)
        WebDriverHelp().click_item('xpath', '//*[@id="data-table"]/tbody/tr/td[1]/span[1]/a')
        time.sleep(0.5)
        WebDriverHelp().input_value('xpath', '/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input', 'autotest')
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/div/div/div[3]/button[1]')




