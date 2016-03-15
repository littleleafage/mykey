#coding=utf-8
'''
登录模块
'''
import time
from src.common_functions.webdriver_help import WebDriverHelp

class LoginClass(object):

    def login(self, url, logindata):

        WebDriverHelp().geturl(url)
        for i in range(len(logindata)):
            temp = logindata[i]
            try:
                WebDriverHelp().inputvalue(temp[0], temp[1], temp[2])
            except:
                WebDriverHelp().clickitem(temp[0], temp[1])
            time.sleep(0.5)

    def logout(self):

        WebDriverHelp().geturl('')
        time.sleep(0.5)