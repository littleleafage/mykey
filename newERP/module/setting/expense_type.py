# -*- coding: utf-8 -*-
# 其它支出类型模块功能

from common.webdriver_help import WebDriverHelp
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import Keys
import time


class ExpenseType(object):

    def get_route(self):
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/article/section/ul/li[3]/a')
        time.sleep(0.5)
        WebDriverHelp().click_item('xpath', '//*[@id="menus"]/li[8]/a')
        time.sleep(0.5)
        WebDriverHelp().click_item('xpath', '//*[@id="menus"]/li[8]/ul/li[3]/a')
        time.sleep(0.5)

    def search(self, how, what, value):
        WebDriverHelp().input_clear(how, what)
        WebDriverHelp().input_value(how, what, value)
        WebDriverHelp().input_value(how, what, Keys.ENTER)

    def check_data(self, value):  # 检查数据
        self.search('xpath', '/html/body/div[1]/div[2]/div/article/header/div/div/input', value)
        time.sleep(0.5)
        try:
            result = WebDriverHelp().check('xpath', '//*[@id="data-table"]/tbody/tr/td[2]', value)
            if result:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def delete_data(self, value):
        result = self.check_data(value)
        if result:
            WebDriverHelp().click_item('xpath', '//*[@id="data-table"]/tbody/tr/td[1]/span[2]/a')
            WebDriverHelp().switch()
            time.sleep(1)
        else:
            pass

    def add_data(self):  # 添加
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/div[2]/div/article/header/div/a')
        time.sleep(0.5)
        WebDriverHelp().input_value('xpath', '/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input', 'autotest')
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/div/div/div[3]/button[1]')
        time.sleep(1)
        result = self.check_data('autotest')
        if result:
            pass
        else:
            print 'result is wrong'
        time.sleep(0.5)

    def update_data(self):
        self.search('xpath', '/html/body/div[1]/div[2]/div/article/header/div/div/input', 'autotest')
        time.sleep(0.5)
        WebDriverHelp().click_item('xpath', '//*[@id="data-table"]/tbody/tr/td[1]/span[1]/a')
        time.sleep(0.5)
        WebDriverHelp().input_clear('xpath', '/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input')
        WebDriverHelp().input_value('xpath', '/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input', 'autotest')
        WebDriverHelp().click_item('xpath', '/html/body/div[1]/div/div/div[3]/button[1]')
        time.sleep(1)
        result = self.check_data('autotest')
        if result:
            pass
        else:
            print 'result is wrong'




