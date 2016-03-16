#coding=utf-8
'''
存放具体的操作功能块，比如登录，退出等等
'''
import time
import demjson
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.file_oper import DataOperations
class QT_Operations(object):

    def login(self):
        dataoper = DataOperations('logindata.xml')
        store = ["byname", "store_id", dataoper.read_xml('login', 0, 'storeid')]
        username = ["byname", "username", dataoper.read_xml('login', 0, 'username')]
        password = ["byname", "password", dataoper.read_xml('login', 0, 'password')]
        loginbtn = ['byclassname', dataoper.read_xml('login', 0, 'loginbtn')]
        logindata = []
        logindata.append(store)
        logindata.append(username)
        logindata.append(password)
        logindata.append(loginbtn)
        for i in range(len(logindata)):
            temp = logindata[i]
            try:
                WebDriverHelp().inputvalue(temp[0], temp[1], temp[2])
            except:
                WebDriverHelp().clickitem(temp[0], temp[1])
            time.sleep(0.5)

    def logout(self):
        dataoper = DataOperations('logindata.xml')
        url = dataoper.read_xml('logout', 0, 'logouturl')
        WebDriverHelp().geturl(url)

    def upload(self, xpath):
        '''
        微信互动>>群发功能>>素材管理，上传图片
        :param xpath:xpath列
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
        '''
        获取盘点和库存数量
        :param url: json数据链接
        :return:
        '''
        WebDriverHelp().geturl(url)
        data = WebDriverHelp().gettext('byxpath', '/html/body')
        json = demjson.decode(data)
        result = json['products']
        return result

    def search(self, orderdata):
        '''
        工单列表查询
        :param orderdata: 元素信息
        :return:
        '''
        length = len(orderdata)
        for i in range(length-1):
            temp = orderdata[i]
            try:
                try:
                    WebDriverHelp().inputvalue(temp[0], temp[1], temp[2])  # 清空输入框并输入
                except:
                    WebDriverHelp().selectvalue(temp[0], temp[1], temp[2])  # 下拉框输入
                btn = orderdata[length-1]
                WebDriverHelp().clickitem(btn[0], btn[1])  # 查询
                time.sleep(0.5)
                imgname = 'searchresult%d.png' % i
                WebDriverHelp().screenshot(0, imgname)
            except:
                WebDriverHelp().screenshot(1, 'orderlist.png')  # 截取工单列表

