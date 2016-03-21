#coding=utf-8
'''
存放公用的方法
by：yewen
data_added：2016-02-25
'''
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import  Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

global G_WEBDRIVER,G_BROWSERTYPE,DRIVER


class WebDriverHelp(object):
    '''
    主要完成页面的基本操作，如打开指定的URL，对页面上的元素进行操作等
    '''

    def __init__(self, btype="close", atype="firefox", ctype="local"):
        '''
        打开对应的浏览器
        :param btype: 开关参数，如果为close就关闭浏览器
        :param atype: 浏览器的类型，如chrome，firefox，ie
        :param ctype: 打开本地或远程浏览器；local，本地；notlocal：远程
        :return:
        '''
        global DRIVER
        if btype == "open":
            if atype == "chrome":
                if ctype == "local":
                    DRIVER = webdriver.Chrome()
                    # DRIVER.maximize_window()
                elif ctype == "notlocal":
                    DRIVER = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.CHROME)
                    DRIVER.maximize_window()
            elif atype == "ie":
                if ctype == "local":
                    DRIVER = webdriver.Ie()
                    DRIVER.maximize_window()
                elif ctype == "notlocal":
                    DRIVER = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER)
                    DRIVER.maximize_window()
            elif atype == "firefox":
                if ctype == "local":
                    DRIVER = webdriver.Firefox()
                    DRIVER.maximize_window()
                elif ctype == "notlocal":
                    DRIVER = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
                    DRIVER.maximize_window()
        self.DRIVER = DRIVER

    def setup(self):

        '''
        测试URL
        :return:
        '''
        try:
            url = "http://s2.checheweike.com/erp"
            self.DRIVER.get(url)
        except NoSuchElementException:
            print "地址出错"

    def geturl(self, url):
        self.DRIVER.get(url)

    def clickitem(self, findby, elmethod):
        '''
        通过定制定位方法，在对应的项目上执行单击操作
        @param findby：定位方法
        @param elmethod：要定位元素的属性值
        '''
        self.findelement(findby, elmethod).click()

    def findelement(self, findby, elmethod):
        '''
        获取元素
        :param findby:定位方法，如：byid，byname，byclassname等
        :param elmethod:要定位元素的属性值，如：id，name，class name，xpath等
        :return:
        '''
        if findby == 'byid':
            return self.DRIVER.find_element_by_id(elmethod)
        elif findby == 'byname':
            return self.DRIVER.find_element_by_name(elmethod)
        elif findby == 'byclassname':
            return self.DRIVER.find_element_by_class_name(elmethod)
        elif findby == 'byxpath':
            return self.DRIVER.find_element_by_xpath(elmethod)
        elif findby == 'linktext':
            return self.DRIVER.find_element_by_link_text(elmethod)

    def gettext(self, findby, elmethod):
        '''
        通过定制定位方法，获取指定元素的文本
        @param findby：定位方法
        @param elmethod：要定位元素的属性值
        @return：返回获取到的元素文本
        '''
        return self.findelement(findby, elmethod).text

    def inputvalue(self, findby, elmenthod, value):
        '''
        在输入框中输入值
        :param findby: 定位方法
        :param elmenthod: 要定位元素的属性值
        :param value: 要给文本框输入的值
        :return:
        '''
        self.findelement(findby, elmenthod).send_keys(value)

    def isexist(self, findby, elmethod):
        '''
        判断元素是否存在
        :param findby:定位方法
        :param elmethod:要定位元素的属性值
        :return:
        '''
        try:
            self.findelement(findby, elmethod)
            return True
        except:
            return False

    def screenshot(self, imgname):
        '''
        截图
        :param imgname:图片文件名
        :return:
        '''
        self.DRIVER.save_screenshot("../screenshot/" + imgname)

    def selectvalue(self, findby, select, selectvalue):
        '''
        从下拉框中选择指定的项目
        :param findby: 定位方法
        :param select: 要执行选择操作的下拉框句柄
        :param selectvalue: 下拉框中要选择项的文本
        :return:
        '''
        select = Select(self.findelement(findby, select))
        select.select_by_visible_text(selectvalue)

    def switchto(self, type, elmethod):
        if type == 'iframe':
            iframe = self.DRIVER.find_element('id', elmethod)
            self.DRIVER.switch_to.frame(iframe)
        elif type == 'alert':
            self.DRIVER.switch_to.alert

    def teardown(self):
        '''
        关闭浏览器
        :return:
        '''
        self.DRIVER.quit()

    def uploadfile(self, findby, elmethod, value):
        '''
        上传文件
        :param elmethod:定位元素的属性值
        :param filepath:文件路径
        :return:
        '''
        self.findelement(findby, elmethod).send_keys(value)
