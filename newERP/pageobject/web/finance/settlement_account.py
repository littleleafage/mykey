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
    # expense_path = '//*[@id="menus"]/li[8]/ul/li[3]/a'
    search_path = '/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul/li[1]/div/input'
    check_line = '//*[@id="data-table"]/tbody/tr/td[2]'
    delete_btn = '//*[@id="data-table"]/tbody/tr/td[1]/span[2]/a'
    add_btn = '/html/body/div[1]/div[2]/div/article/header/div/a'
    update_btn = '//*[@id="data-table"]/tbody/tr/td[1]/span[1]/a'
    save_btn = '/html/body/div[1]/div/div/div[3]/button[2]'
    input_name = '/html/body/div[1]/div/div/div[2]/form/div/ul[1]/li[1]/div/input'
    select_type = '/html/body/div[1]/div/div/div[2]/form/div/ul[2]/li/div/label[1]/input'
    bank_name = '/html/body/div[1]/div/div/div[2]/form/div/ul[3]/li/div/input'
    bank_number = '/html/body/div[1]/div/div/div[2]/form/div/ul[4]/li/div/input'
    init_money = '/html/body/div[1]/div/div/div[2]/form/div/ul[5]/li/div/input'
    comment = '/html/body/div[1]/div/div/div[2]/form/div/ul[7]/li/div/textarea'

    def get_route(self, path):
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
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.input_name)))
        self.input_value(self.locator, self.input_name, 'autotest')
        self.input_value(self.locator, self.bank_name, u'中行')
        self.input_value(self.locator, self.bank_number, '6134545464')
        self.input_value(self.locator, self.init_money, '32222')
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





