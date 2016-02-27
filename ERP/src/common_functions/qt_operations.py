#coding=utf-8
'''
存放具体的操作功能块，比如登录，退出等等
'''
import time
from src.common_functions.webdriver_help import WebDriverHelp
class QT_Operations(object):

    def login(self, store_id, userName, password, login_btn):
        WebDriverHelp().inputvalue('byname', 'store_id', store_id)
        WebDriverHelp().inputvalue('byname', 'username', userName)
        WebDriverHelp().inputvalue('byname', 'password', password)
        time.sleep(0.5)
        WebDriverHelp().clickitem("byxpath", login_btn)
        time.sleep(2)

    def logout(self, url):
        '''WebDriverHelp().clickitem("bypath", user_btn)
        time.sleep(0.5)
        WebDriverHelp().clickitem("bypath", logout_btn)
        time.sleep(1)'''
        WebDriverHelp().geturl(url)

    def upload(self, findby, xpath, uploadbtn):
        '''
        微信互动>>群发功能>>素材管理，上传图片
        :param xpath:
        :param value:
        :param axpath:
        :param findby:
        :return:
        '''
        for m in xpath:
            if WebDriverHelp().isexite(m):
                WebDriverHelp().clickitem("byxpath", m)
                time.sleep(1)
            else:
                print(m + "不存在")
        WebDriverHelp().uploadfile(findby, uploadbtn)


