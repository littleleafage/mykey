#coding=utf-8
'''
德阳万佳：
出库单价和库存余额的单价不一致
找出不一致的数据
'''
import time
import unittest
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.qt_operations import QT_Operations

class TestcaseLogin(unittest.TestCase):

    def setUp(self):
        WebDriverHelp("open", "chrome", "local").setup() #本地用chrome浏览器打开后台地址

    def testcase_login(self):

        QT_Operations().login()
        today = time.strftime('%Y-%m-%d', time.localtime(time.time())) #获取当天日期
        for m in range(5, 6, 1):
            try:
                url1 = 'http://s2.checheweike.com/erp/index.php?route=catalog/product/ajax_gets_with_stock&' \
                       'current_page=1&limit=10000&page=1&page_size=10&status=1&warehouse_id=%d' % m  #盘点数据
                url2 = 'http://s2.checheweike.com/erp/index.php?route=stock/balance/ajax_gets&date=%s&limit=10000' \
                       '&order=ASC&page=1&s_qkf=0&sort=ps.total_quantity&warehouse_ids=%d' % (today, m) #库存数据
            except:
                print '仓库ID：',m,'不存在'
            data1 = QT_Operations().getstock(url1) #其它出库
            data2 = QT_Operations().getstock(url2) #库存余额

            for i in range(len(data1)): #获取出库相应数据
                pd = data1[i]
                pdid = str(pd['product_id'])
                pdname = pd['name']
                pdyue = str(pd['stock_quantity'])
                price = round(pd['unit_cost'], 2)
                pdprice = str(price)
                for j in range(len(data2)): #库存数据
                    yue = data2[j]
                    yuid = str(yue['product_id'])
                    ucint = round(yue['uc'], 2)
                    uc = str(ucint)
                    try:
                        self.assertEqual(pdid, yuid)
                        try:
                            self.assertEqual(pdprice, uc)  # 比较两边的库存单价
                        except:
                            print '仓库ID：', m, ';', pdname, '-', pdid, ':', pdprice, ',', uc
                    except:
                        pass

    def tearDown(self):
        WebDriverHelp().teardown()

