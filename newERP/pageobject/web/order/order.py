# -*- coding: utf-8 -*-
# 其它支出类型模块功能

from common.webdriver_help import WebDriverHelp
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import time


class OrderSetting(WebDriverHelp):

    locator = 'xpath'
    setting_path = '/html/body/div[1]/article/section/ul/li[3]/a'
    order_path = '//*[@id="menus"]/li[2]/a'
    save_btn = '.btn.btn-primary'

    def get_route(self, path):
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.setting_path)))
        self.click_item(self.locator, self.setting_path)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, self.order_path)))
        self.click_item(self.locator, self.order_path)
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located((By.XPATH, path)))
        self.click_item(self.locator, path)
        time.sleep(0.5)

    def check_page(self):
        self.click_item('class_name', self.save_btn)
        self.refresh_page()
        ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(By.CLASS_NAME, self.save_btn))


