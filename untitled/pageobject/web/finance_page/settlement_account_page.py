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
from common.menu_locator import FinanceData
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
        self.input_value(value, *FinanceData.ACCOUNT_NAME_SEARCH)
        self.DRIVER.find_element(*FinanceData.ACCOUNT_NAME_SEARCH).send_keys(Keys.ENTER)
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
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.ACCOUNT_NAME))
        self.input_value('autotest', *FinanceData.ACCOUNT_NAME)
        self.input_value('20000', *FinanceData.INIT_DATA)
        self.input_value(u'', *FinanceData.COMMENT)
        self.click_item(*FinanceData.SAVE_BTN2)
        time.sleep(0.5)

    def update_data(self, value):
        self.search(value)
        self.click_item(*FinanceData.UPDATE_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.ACCOUNT_NAME))
        self.click_item(*FinanceData.BANK_TYPE)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.BANK_NAME))
        self.input_value(u'中行', *FinanceData.BANK_NAME)
        self.input_value(u'24545345', *FinanceData.BANK_CARD)
        self.click_item(*FinanceData.SAVE_BTN2)
        time.sleep(0.5)
