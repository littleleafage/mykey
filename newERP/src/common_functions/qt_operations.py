#coding=utf-8
'''
存放具体的操作功能块，比如登录，退出等等
'''
import time
import demjson
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_data.login import Login


class Operations(object):

    def login(self):
        login_data = []
        store_id = ["name", "store_id", Login().get_store_id()]
        username = ["name", "username", Login().get_username()]
        password = ["name", "password", Login().get_password()]
        login_btn = ['class_name', Login().get_login_btn()]
        login_data.append(store_id)
        login_data.append(username)
        login_data.append(password)
        login_data.append(login_btn)
        for i in range(len(login_data)):
            temp = login_data[i]
            try:
                try:
                    WebDriverHelp().input_value(temp[0], temp[1], temp[2])
                except:
                    WebDriverHelp().click_item(temp[0], temp[1])
                    time.sleep(0.5)
            except:
                WebDriverHelp().screen_shot(1, 'login.png')

    def logout(self):
        url = Login().get_logout_url()
        WebDriverHelp().geturl(url)

    def upload(self, xpath):
        '''
        微信互动>>群发功能>>素材管理，上传图片
        :param xpath:xpath列
        :return:
        '''
        for m in xpath:
            if WebDriverHelp().is_exist("byxpath", m):
                WebDriverHelp().click_item("byxpath", m)
                time.sleep(1)
            else:
                print m + "不存在"

    def uploadimg(self, findby, uploadbtn):
        WebDriverHelp().upload_file(findby, uploadbtn)

    def getstock(self, url):
        '''
        获取盘点和库存数量
        :param url: json数据链接
        :return:
        '''
        WebDriverHelp().geturl(url)
        data = WebDriverHelp().get_text('byxpath', '/html/body')
        json = demjson.decode(data)
        result = json['products']
        return result

    def search(self, data):
        '''
        工单列表查询
        :param orderdata: 元素信息
        :return:
        '''
        length = len(data)
        for i in range(length-1):
            temp = data[i]
            try:
                try:
                    WebDriverHelp().input_value('xpath', temp[0], temp[1])  # 清空输入框并输入
                except:
                    WebDriverHelp().select_value('xpath', temp[0], temp[1])  # 下拉框输入
                btn = data[length-1]
                WebDriverHelp().click_item('class_name', btn[0])  # 查询
                time.sleep(0.5)
                img_name = 'Search-result%d.png' % i
                WebDriverHelp().screen_shot(0, img_name)
            except:
                WebDriverHelp().screen_shot(1, 'Order-list.png')  # 截取工单列表

