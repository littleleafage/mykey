#coding=utf-8
'''
存放具体的操作功能块，比如登录，退出等等
'''
import time
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.data_operations import DataOperations
class QT_Operations(object):

    def login(self):
        WebDriverHelp("open", "chrome", "local").setup("http://s2.checheweike.com/erp")
        data = DataOperations("testcase_login.xml")
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
        '''WebDriverHelp().clickitem("bypath", user_btn)
        time.sleep(0.5)
        WebDriverHelp().clickitem("bypath", logout_btn)
        time.sleep(1)'''
        WebDriverHelp().geturl(url)

    def upload(self, xpath):
        '''
        微信互动>>群发功能>>素材管理，上传图片
        :param xpath:
        :param value:
        :param axpath:
        :param findby:
        :return:
        '''
        for m in xpath:
            if WebDriverHelp().isexist("byxpath", m):
                WebDriverHelp().clickitem("byxpath", m)
                time.sleep(1)
            else:
                print m + "不存在"

    def uploadimg(self, findby, uploadbtn):
        WebDriverHelp().uploadfile(findby, uploadbtn)


