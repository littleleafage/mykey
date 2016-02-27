#coding=utf-8
'''
具体的功能模块，如登录，退出等
by：yewen
data_added：2016-02-25
'''
import time
from src.common_functions.webdriver_help import WebDriverHelp

class QT_Opera(object):

    def login(self, storeid, username, password, loginbtn):
        WebDriverHelp().inputvalue('byname', 'store_id', storeid)
        WebDriverHelp().inputvalue('byname', 'username', username)
        WebDriverHelp().inputvalue('byname', 'password', password)
        time.sleep(0.5)
        WebDriverHelp().clickitem("byxpath", loginbtn)
        time.sleep(3)

    def logout(self, url):
        WebDriverHelp().setup(url)
        time.sleep(2)