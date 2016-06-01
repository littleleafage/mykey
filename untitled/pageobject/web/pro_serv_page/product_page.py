# -*- coding: utf-8 -*-
# 其它支出类型模块功能

from common.basepage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from common.menu_locator import Menu
from common.menu_locator import FinanceData
from common.menu_locator import ProductData
import time


class ProductPage(BasePage):

    def get_route(self):
        self.click_item(*Menu.SETTING)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductData.PRO_SER))
        self.click_item(*ProductData.PRO_SER)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductData.PRODUCT))
        self.click_item(*ProductData.PRODUCT)
        time.sleep(0.5)

    def search(self, value):
        self.input_value(value, *ProductData.SEARCH_KEY)
        # self.input_value(*ProductData.SEARCH_CAR_MODELS)
        # self.DRIVER.find_element(*ProductData.SEARCH_CAR_MODELS).send_keys(Keys.ENTER)
        self.click_item(*ProductData.SEARCH_BTN)
        time.sleep(0.5)

    def init_data(self, value):
        if self.check_data(value):
            self.delete_data()
        else:
            pass

    def check_data(self, value):  # 检查数据
        self.search(value)
        try:
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductData.CHECK_LINE))
            return True
        except TimeoutException:
            return False

    def delete_data(self):
        self.click_item(*ProductData.DELETE_ICON)
        self.switch()
        time.sleep(0.5)

    def add_data(self, value):  # 添加
        self.click_item(*FinanceData.ADD_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductData.PRODUCT_NAME))
        self.input_value(value, *ProductData.PRODUCT_NAME)
        self.input_value('20000', *FinanceData.INIT_DATA)
        self.input_value(u'', *FinanceData.COMMENT)
        self.click_item(*FinanceData.SAVE_BTN2)
        time.sleep(0.5)

    def update_data(self, value, value2):
        self.search(value)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.UPDATE_BTN))
        self.click_item(*FinanceData.UPDATE_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinanceData.INPUT_VALUE))
        self.input_value(value2, *FinanceData.INPUT_VALUE)
        self.click_item(*FinanceData.SAVE_BTN)
        time.sleep(0.5)
