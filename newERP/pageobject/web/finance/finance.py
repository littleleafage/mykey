# -*- coding: utf-8 -*-
# 其它支出类型模块功能

from common.webdriver_help import WebDriverHelp
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import time


class FinanceType(WebDriverHelp):

    locator = 'xpath'
    setting_path = '/html/body/div[1]/article/section/ul/li[3]/a'
    finance_path = '//*[@id="menus"]/li[8]/a'
    search_path = '/html/body/div[1]/div[2]/div/article/header/div/div/input'
    check_line = '//*[@id="data-table"]/tbody/tr/td[2]'
    delete_btn = '//*[@id="data-table"]/tbody/tr/td[1]/span[2]/a'
    add_btn = '/html/body/div[1]/div[2]/div/article/header/div/a'
    update_btn = '//*[@id="data-table"]/tbody/tr/td[1]/span[1]/a'
    save_btn = '/html/body/div[1]/div/div/div[3]/button[1]'
    input_path = '/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input'

    def get_route(self, path):
        # self.geturl('http://www.checheweike.com/web/index.php?route=common/index#/expense_type/list')
        self.click_item(self.locator, self.setting_path)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.finance_path)))
        self.click_item(self.locator, self.finance_path)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, path)))
        self.click_item(self.locator, path)
        time.sleep(1)

    def search(self, value):
        # self.input_clear('xpath', self.search_path)
        self.input_value(self.locator, self.search_path, value)
        self.DRIVER.find_element(self.locator, self.search_path).send_keys(Keys.ENTER)
        time.sleep(0.5)

    def init_data(self, value):
        if self.check_data(value):
            self.delete_data()
        else:
            pass

    def check_data(self, value):  # 检查数据
        self.search(value)
        try:
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.check_line)))
            return True
        except TimeoutException:
            return False

    def delete_data(self):
        self.click_item(self.locator, self.delete_btn)
        self.switch()
        time.sleep(0.5)

    def add_data(self):  # 添加
        self.click_item(self.locator, self.add_btn)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.input_path)))
        self.input_value(self.locator, self.input_path, 'autotest')
        self.click_item(self.locator, self.save_btn)
        time.sleep(0.5)

    def update_data(self, value, value2):
        self.search(value)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.update_btn)))
        self.click_item(self.locator, self.update_btn)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.input_path)))
        self.input_value(self.locator, self.input_path, value2)
        self.click_item(self.locator, self.save_btn)
        time.sleep(0.5)
