# -*- coding: utf-8 -*-
from common.webdriver_help import WebDriverHelp
from common.menu_locator import Menu
from common.menu_locator import SystemMenu
import time


class System(WebDriverHelp):

    def get_system(self):
        self.click_items(*Menu.SETTING)
        time.sleep(2)
        # self.click_items(*SystemMenu.GUIDE)
        self.click_items(*SystemMenu.SYSTEM_INFO)
