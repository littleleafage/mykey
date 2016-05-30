# -*- coding: utf-8 -*-
from common.base_page import BasePage


class LoginPage(BasePage):

    def login(self, driver):
        self.driver = driver

