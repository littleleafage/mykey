#coding=utf-8
'''
车品道盘点和库存余额中的数据不一致
找出不一致的数据
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
        today = time.strftime('%Y-%m-%d', time.localtime(time.time())) #获取当天日期
        for m in range(1, 2, 1):
            try:
                url1 = 'http://s2.checheweike.com/erp/index.php?route=catalog/product/ajax_gets_with_stock&current_page=1' \
                       '&limit=10000&page=1&page_size=10&status=1&warehouse_id=%d' %m #盘点数据
                url2 = 'http://s2.checheweike.com/erp/index.php?route=stock/balance/ajax_gets&date=%s&limit=10000' \
                       '&order=ASC&page=1&s_qkf=0&sort=ps.total_quantity&warehouse_ids=%d' %(today, m) #库存数据
            except:
                print '仓库ID：',m,'不存在'
            data1 = QT_Operations().getstock(url1) #盘点
            data2 = QT_Operations().getstock(url2) #库存余额

            for i in range(len(data1)): #获取盘点相应数据
                pd = data1[i]
                pdid = str(pd['product_id'])
                pdname = pd['name']
                pdyue = str(pd['stock_quantity'])

                for j in range(len(data2)): #库存数据
                    yue = data2[j]
                    yuid = str(yue['product_id'])
                    yuyu = str(yue['quantity'])
                    uc = str(yue['uc'])
                    try:
                        self.assertEqual(pdid, yuid)
                        try:
                            self.assertEqual(pdyue, yuyu)
                        except:
                            print '仓库ID:', m,'；', pdname, ',', uc, ':' ,pdyue,',',yuyu
                    except:
                        pass

    def tearDown(self):
        WebDriverHelp().teardown()

