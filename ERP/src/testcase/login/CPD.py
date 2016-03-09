#coding=utf-8
'''
登录测试
'''
import time
import unittest
import demjson
from src.common_functions.data_operations import DataOperations
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.qt_operations import QT_Operations

class TestcaseLogin(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup() #本地用chrome浏览器打开后台地址

    def testcase_login(self):
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
        QT_Operations().login(logindata)
        for m in range(1,11,1):
            try:
                url1 = 'http://s2.checheweike.com/erp/index.php?route=catalog/product/ajax_gets_with_stock&current_page=1&limit=10000&page=1&page_size=10&status=1&warehouse_id=%d' %m
                url2 = 'http://s2.checheweike.com/erp/index.php?route=stock/balance/ajax_gets&date=2016-03-08&limit=10000&order=ASC&page=1&s_qkf=0&sort=ps.total_quantity&warehouse_ids=%d' %m
            except:
                print '仓库ID：',m,'不存在'
            data1 = QT_Operations().getstock(url1) #盘点
            data2 = QT_Operations().getstock(url2) #库存余额
            length1 = len(data1)
            length2 = len(data2)
            for i in range(length1): #盘点数据
                pd = data1[i]
                pdid = str(pd['product_id'])
                pdname = pd['name']
                pdyue = str(pd['stock_quantity'])
                for j in range(length2): #库存数据
                    yue = data2[j]
                    yuid = str(yue['product_id'])
                    yuyu = str(yue['quantity'])
                    try:
                        self.assertEqual(pdid, yuid)
                        try:
                            self.assertEqual(pdyue, yuyu)
                        except:
                            print '仓库ID:', m,'；',pdname,':' ,pdyue,',',yuyu
                    except:
                        pass

    def tearDown(self):
        WebDriverHelp().teardown()

