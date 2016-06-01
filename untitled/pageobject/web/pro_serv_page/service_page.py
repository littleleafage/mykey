# -*- coding: utf-8 -*-
# 其它支出类型模块功能

from common.basepage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from common.menu_locator import Menu
from common.menu_locator import FinanceMenu
from common.menu_locator import FinanceData
import time


class ServicePage(BasePage):

    def get_route(self, *loc):
        # self.geturl('http://www.checheweike.com/web/index.php?route=common/index#/expense_type/list')
        self.click_item(*Menu.SETTING)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, FinanceMenu.FINANCE[1])))
        self.click_item(*FinanceMenu.FINANCE)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(loc))
        self.click_item(*loc)
        time.sleep(0.5)

    def search(self, value):
        self.input_clear(*FinanceData.SEARCH)
        self.input_value(value, *FinanceData.SEARCH)
        self.DRIVER.find_element(*FinanceData.SEARCH).send_keys(Keys.ENTER)
        time.sleep(0.5)

    def init_data(self, value):
        if self.check_data(value):
            self.delete_data()
        else:
            pass

    def check_data(self, value):  # 检查数据
        self.search(value)
        try:
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.CHECK_LINE))
            return True
        except TimeoutException:
            return False

    def delete_data(self):
        self.click_item(*FinanceData.DELETE_BTN)
        self.switch()
        time.sleep(0.5)

    def add_data(self):  # 添加
        self.click_item(*FinanceData.ADD_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.INPUT_VALUE))
        self.input_value('autotest', *FinanceData.INPUT_VALUE)
        self.click_item(*FinanceData.SAVE_BTN)
        time.sleep(0.5)

    def update_data(self, value, value2):
        self.search(value)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.UPDATE_BTN))
        self.click_item(*FinanceData.UPDATE_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.INPUT_VALUE))
        self.input_clear(*FinanceData.INPUT_VALUE)
        self.input_value(value2, *FinanceData.INPUT_VALUE)
        self.click_item(*FinanceData.SAVE_BTN)
        time.sleep(0.5)
