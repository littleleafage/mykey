# -*- coding: utf-8 -*-
# 登录登出模块功能
from common.basepage import BasePage
from common.menu_locator import LoginData
import time


class Login(BasePage):

    def login(self, store_id, username, password):
        self.input_value(store_id, *LoginData.STORE_ID)
        self.input_value(username, *LoginData.USERNAME)
        self.input_value(password, *LoginData.PASSWORD)
        self.click_item(*LoginData.LOGIN_BTN)
        time.sleep(0.5)

    def logout(self):
        self.geturl("http://www.checheweike.com/web/index.php?route=common/logout")
        time.sleep(0.5)
        self.teardown()

    def verify_page(self):
        value = self.get_page_title()
        if value == LoginData.LOG_PAGE_TITLE:
            return True
        else:
            raise AssertionError('Login page is wrong')

    def verify_success_login(self):
        if self.is_element_displayed(*LoginData.LOGIN_USER):
            return True
        else:
            raise AssertionError('Failed to login')

