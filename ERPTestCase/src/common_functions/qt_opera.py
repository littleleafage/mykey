#coding=utf-8
'''
具体的功能模块，如登录，退出等
by：yewen
data_added：2016-02-25
'''
import time
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.data_opera import DataOpera

class QT_Opera(object):

    def login(self):
        WebDriverHelp("open", "chrome", "local").setup("http://s2.checheweike.com/erp")
        data = DataOpera("testcase_login.xml")
        storeid = data.read_xml('login', 0, 'storeid')
        username = data.read_xml('login', 0, 'username')
        password = data.read_xml('login', 0, 'password')
        loginbtn = data.read_xml('login', 0, 'loginbtn')
        WebDriverHelp().inputvalue('byname', 'store_id', storeid)
        WebDriverHelp().inputvalue('byname', 'username', username)
        WebDriverHelp().inputvalue('byname', 'password', password)
        time.sleep(0.5)
        WebDriverHelp().clickitem("byxpath", loginbtn)
        time.sleep(1)

    def logout(self, url):
        WebDriverHelp().setup(url)
        time.sleep(2)