#coding=utf-8
'''
存放具体的操作功能块，比如登录，退出等等
'''
import time
import demjson
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.data_operations import DataOperations
class QT_Operations(object):

    def login(self):
        dataoper = DataOperations("TestCase_QT_Login.xml")
        store = ["byname", "store_id", dataoper.read_xml('login', 0, 'storeid')]
        username = ["byname", "username", dataoper.read_xml('login', 0, 'username')]
        password = ["byname", "password", dataoper.read_xml('login', 0, 'password')]
        loginbtn = ['byclassname', 'login-btn']
        logindata = []
        logindata.append(store)
        logindata.append(username)
        logindata.append(password)
        logindata.append(loginbtn)
        for i in range(len(logindata)):
            temp = logindata[i]
            try:
                WebDriverHelp().inputvalue(temp[0],temp[1],temp[2])
            except:
                WebDriverHelp().clickitem(temp[0], temp[1])
            time.sleep(0.5)

    def logout(self, url):
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

    def getstock(self, url):
        WebDriverHelp().geturl(url)
        data = WebDriverHelp().gettext('byxpath', '/html/body')
        json = demjson.decode(data)
        result = json['products']
        return result


