# -*- coding: utf-8 -*-
from common.basepage import BasePage
from common.menu_locator import Menu
from common.menu_locator import SystemMenu
import time


class System(BasePage):

    def get_system(self):
        self.click_items(*Menu.SETTING)
        time.sleep(2)
        self.click_items(*SystemMenu.SYSTEM_INFO)
