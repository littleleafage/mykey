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
        WebDriverHelp("open", "chrome", "local").setup()
        data = DataOpera("testcase_login.xml")
        storeid = data.read_xml('login', 1, 'storeid')
        username = data.read_xml('login', 0, 'username')
        password = data.read_xml('login', 0, 'password')
        loginbtn = data.read_xml('login', 0, 'loginbtn')
        WebDriverHelp().inputvalue('byname', 'store_id', storeid)
        WebDriverHelp().inputvalue('byname', 'username', username)
        WebDriverHelp().inputvalue('byname', 'password', password)
        time.sleep(0.5)
        try:
            WebDriverHelp().clickitem("byxpath", loginbtn)
            time.sleep(1)
        except:
            WebDriverHelp().screenshot('login-err.png')

    def logout(self, url):
        WebDriverHelp().setup(url)
        time.sleep(2)

    def menu(self, menu_link):
        for i in range(len(menu_link)):
            temp = menu_link[i]
            try:
                WebDriverHelp().clickitem('linktext', temp)
                WebDriverHelp().screenshot('result/result-' + str(i) + '.png')
                time.sleep(0.3)
            except:
                WebDriverHelp().screenshot('screenshot/error-' + str(i) + '.png')


