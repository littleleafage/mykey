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
from common.menu_locator import FinancePath
import time


class FinancePage(BasePage):

    def get_route(self, *loc):
        # self.geturl('http://www.checheweike.com/web/index.php?route=common/index#/expense_type/list')
        self.click_item(*Menu.SETTING)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, FinanceMenu.FINANCE_MENU[1])))
        self.click_item(*FinanceMenu.FINANCE_MENU)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(loc))
        self.click_item(*loc)
        time.sleep(0.5)

    def search(self, value):
        self.input_value(value, *FinancePath.SEARCH)
        self.DRIVER.find_element(*FinancePath.SEARCH).send_keys(Keys.ENTER)
        time.sleep(0.5)

    def init_data(self, value):
        if self.check_data(value):
            self.delete_data()
        else:
            pass

    def check_data(self, value):  # 检查数据
        self.search(value)
        try:
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.CHECK_LINE))
            return True
        except TimeoutException:
            return False

    def delete_data(self):
        self.click_item(*FinancePath.DELETE_BTN)
        self.switch()
        time.sleep(0.5)

    def add_data(self):  # 添加
        self.click_item(*FinancePath.ADD_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.INPUT_VALUE))
        self.input_value('autotest', *FinancePath.INPUT_VALUE)
        self.click_item(*FinancePath.SAVE_BTN)
        time.sleep(0.5)

    def update_data(self, value, value2):
        self.search(value)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.UPDATE_BTN))
        self.click_item(*FinancePath.UPDATE_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.INPUT_VALUE))
        self.input_clear(*FinancePath.INPUT_VALUE)
        self.input_value(value2, *FinancePath.INPUT_VALUE)
        self.click_item(*FinancePath.SAVE_BTN)
        time.sleep(0.5)
