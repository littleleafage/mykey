# -*- coding: utf-8 -*-
# 结算账户模块功能

from common.basepage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from common.menu_locator import Menu
from common.menu_locator import FinanceMenu
from common.menu_locator import FinancePath
from pageobject.web.finance_page.finance_page import FinancePage
import time


class SettlementAccountPage(FinancePage):

    def get_route(self, *loc):
        self.click_item(*Menu.SETTING)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, FinanceMenu.FINANCE[1])))
        self.click_item(*FinanceMenu.FINANCE)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(loc))
        self.click_item(*loc)
        time.sleep(0.5)

    def search(self, value):
        self.input_value(value, *FinancePath.ACCOUNT_NAME_SEARCH)
        self.DRIVER.find_element(*FinancePath.ACCOUNT_NAME_SEARCH).send_keys(Keys.ENTER)
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
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.ACCOUNT_NAME))
        self.input_value('autotest', *FinancePath.ACCOUNT_NAME)
        self.input_value('20000', *FinancePath.INIT_DATA)
        self.input_value(u'', *FinancePath.COMMENT)
        self.click_item(*FinancePath.SAVE_BTN2)
        time.sleep(0.5)

    def update_data(self, value):
        self.search(value)
        self.click_item(*FinancePath.UPDATE_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.ACCOUNT_NAME))
        self.click_item(*FinancePath.BANK_TYPE)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.BANK_NAME))
        self.input_value(u'中行', *FinancePath.BANK_NAME)
        self.input_value(u'24545345', *FinancePath.BANK_CARD)
        self.click_item(*FinancePath.SAVE_BTN2)
        time.sleep(0.5)
