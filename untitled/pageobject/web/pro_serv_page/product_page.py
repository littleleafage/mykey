# -*- coding: utf-8 -*-
# 其它支出类型模块功能

from common.basepage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from common.menu_locator import Menu
from common.menu_locator import FinancePath
from common.menu_locator import ProductPath
import time


class ProductPage(BasePage):

    def get_route(self):
        self.click_item(*Menu.SETTING)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.PRO_SER))
        self.click_item(*ProductPath.PRO_SER)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.PRODUCT))
        self.click_item(*ProductPath.PRODUCT)
        time.sleep(0.5)

    def search(self, value):
        self.input_value(value, *ProductPath.SEARCH_KEY)
        # self.input_value(*ProductPath.SEARCH_CAR_MODELS)
        # self.DRIVER.find_element(*ProductPath.SEARCH_CAR_MODELS).send_keys(Keys.ENTER)
        self.click_item(*ProductPath.SEARCH_BTN)
        time.sleep(0.5)

    def init_data(self, value):
        if self.check_data(value):
            self.delete_data()
        else:
            pass

    def check_data(self, value):  # 检查数据
        self.search(value)
        try:
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.CHECK_LINE))
            return True
        except TimeoutException:
            return False

    def delete_data(self):
        self.click_item(*ProductPath.DELETE_ICON)
        self.switch()
        time.sleep(0.5)

    def add_data(self, value):  # 添加
        self.click_item(*FinancePath.ADD_BTN)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.PRODUCT_NAME))
        self.input_value(value, *ProductPath.PRODUCT_NAME)
        self.input_value(u'其它工具', *ProductPath.PRODUCT_TYPE)
        self.input_value(u'', *ProductPath.PRODUCT_MODEL)
        self.input_value(u'', *ProductPath.PRODUCT_BARCODE)
        self.input_value(u'', *ProductPath.PRODUCT_QUANTITY_LIMIT)
        self.input_value(u'', *ProductPath.PURCHASE_PRICE)
        self.input_value(u'', *ProductPath.PRODUCT_PRICE)
        self.input_value(u'', *ProductPath.PRODUCT_VIP_PRICE)
        self.input_value(u'', *ProductPath.CAR_MODELS)
        self.click_item(*ProductPath.HIGH_SET)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.CREDITS_RATIO))
        self.input_value(20, *ProductPath.CREDITS_RATIO)
        self.input_value(u'', *ProductPath.ATTR1)
        self.input_value(u'', *ProductPath.ATTR2)
        self.input_value(u'', *ProductPath.ATTR3)
        self.input_value(u'', *ProductPath.COMMENT)
        self.click_item(*ProductPath.SAVE_BTN)
        time.sleep(0.5)

    def update_data(self, value, value2):
        self.search(value)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.UPDATE_ICON))
        self.click_item(*FinancePath.UPDATE_ICON)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(FinancePath.PRODUCT_NAME))
        self.input_value(value2, *ProductPath.PRODUCT_PRICE)
        self.click_item(*ProductPath.SAVE_BTN)
        time.sleep(0.5)

    def delete_datas(self, value):
        self.add_data(value)
        self.search(value)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(ProductPath.CHECK_BOX_ALL))
        self.click_item(*ProductPath.CHECK_BOX_ALL)
        self.click_item(*ProductPath.DELETE_BTN)
        self.switch()
        time.sleep(0.5)
