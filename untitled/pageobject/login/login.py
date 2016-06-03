# -*- coding: utf-8 -*-
# 登录登出模块功能
from common.basepage import BasePage
from common.menu_locator import LoginPath
import selenium.webdriver.support.expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
import time


class Login(BasePage):

    def login(self, store_id, username, password):
        try:
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(LoginPath.LOGIN_BTN))
            self.input_value(store_id, *LoginPath.STORE_ID)
            self.input_value(username, *LoginPath.USERNAME)
            self.input_value(password, *LoginPath.PASSWORD)
            self.click_item(*LoginPath.LOGIN_BTN)
            time.sleep(0.5)
        except:
            raise TimeoutException(u'未找到登录按钮')

    def logout(self):
        try:
            self.geturl("http://www.checheweike.com/web/index.php?route=common/logout")
            ui.WebDriverWait(self.DRIVER, 3).until(ec.visibility_of_element_located(LoginPath.LOGIN_BTN))
            self.teardown()
        except:
            raise TimeoutException(u'未正确退出系统')

    def verify_page(self):
        value = self.get_page_title()
        if value == LoginPath.LOG_PAGE_TITLE:
            return True
        else:
            raise AssertionError('Login page is wrong')

    def verify_success_login(self):
        if self.is_element_displayed(*LoginPath.LOGIN_USER):
            return True
        else:
            raise AssertionError('Failed to login')

