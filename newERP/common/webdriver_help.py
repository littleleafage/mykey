# -*- coding: utf-8 -*-
"""
存放公用的方法
"""
from selenium import webdriver
from selenium.webdriver.support.ui import  Select
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui

global G_WEBDRIVER, G_BROWSERTYPE, DRIVER


class WebDriverHelp(object):
    """
    主要完成页面的基本操作，如打开指定的URL，对页面上的元素进行操作等
    """
    def __init__(self, btype="close", atype="firefox", ctype="local"):
        """
        打开对应的浏览器
        :param btype: 开关参数，如果为close就关闭浏览器
        :param atype: 浏览器的类型，如chrome，firefox，ie
        :param ctype: 打开本地或远程浏览器；local，本地；notlocal：远程
        :return:
       """
        global DRIVER
        if btype == "open":
            if atype == "chrome":
                if ctype == "local":
                    DRIVER = webdriver.Chrome()
                    #DRIVER.maximize_window()
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
            elif atype == 'htmlunit':
                if ctype == "local":
                    DRIVER = webdriver.HtmlUnitDriver()
                    DRIVER.maximize_window()
                elif ctype == "notlocal":
                    DRIVER = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
                    DRIVER.maximize_window()
        self.DRIVER = DRIVER

    def setup(self):
        """
        打开url
        :return:
       """
        try:
            self.DRIVER.get('https://www.checheweike.com/web')
        except NoSuchElementException:
            print "地址出错"

    def teardown(self):
        """
        关闭浏览器
        :return:
        """
        self.DRIVER.quit()

    def geturl(self, url):
        """
        打开指定的网址
        :param url: 要打开的网址
        :return:
        """
        self.DRIVER.get(url)

    def check(self, how, what, value):
        """
        :param how:
        :param what:
        :param value:
        :return:
        """
        text = self.get_text(how, what)
        if text == value:
            print text
            return True
        else:
            return False

    def click_item(self, how, what):
        """
        在对应的项目上执行单击操作
        @param how：定位方法
        @param what：要定位元素的属性值
        """
        self.find_element(how, what).click()

    def find_element(self, how, what):
        """
        定位元素
        :param how:定位方法，如：byid，byname，byclassname等
        :param what:要定位元素的属性值，如：id，name，class name，xpath等
        :return:
        """
        if how == 'id':
            return self.DRIVER.find_element_by_id(what)
        elif how == 'name':
            return self.DRIVER.find_element_by_name(what)
        elif how == 'xpath':
            return self.DRIVER.find_element_by_xpath(what)
        elif how == 'class_name':
            return self.DRIVER.find_element_by_class_name(what)
        elif how == 'link_text':
            return self.DRIVER.find_element_by_link_text(what)

    def get_text(self, how, what):
        """
        获取指定元素的文本
        @param how：定位方法
        @param what：要定位元素的属性值
        @return：返回获取到的元素文本
        """
        try:
            return self.find_element(how, what).text
        except AttributeError:
            raise AttributeError()

    def get_page_title(self):
        return self.DRIVER.title

    def input_clear(self, how, what):
        """
        清空input输入框
        :param how:
        :param what:
        :return:
        """
        self.find_element(how, what).clear()

    def input_value(self, how, what, value):
        """
        在输入框中输入值
        :param how: 定位方法
        :param what: 要定位元素的属性值
        :param value: 要给文本框输入的值
        :return:
        """
        inpu = self.find_element(how, what)
        inpu.send_keys(value)

    def refresh_page(self):  # 刷新页面
        self.DRIVER.refresh()

    def is_element_displayed(self, how, what):
        return self.find_element(how, what).is_displayed()

    def is_element_enabled(self, how, what):
        return self.find_element(how, what).is_enabled()

    def is_element_selected(self, how, what):
        return self.find_element(how, what).is_selected()

    def screen_shot(self, file_type, value):
        """
        截图
        :param file_type:截图类型，0为结果截图，1为错误截图
        :param value:图片文件名
        :return:
        """
        if file_type == 0:
            self.DRIVER.save_screenshot("../screenshot/result/" + value)
        elif file_type == 1:
            self.DRIVER.save_screenshot("../screenshot/error/" + value)

    def select_value(self, how, what, value):
        """
        从下拉框中选择指定的项目
        :param how: 定位方法
        :param what: 要执行选择操作的下拉框句柄
        :param value: 下拉框中要选择项的文本
        :return:
        """
        select = Select(self.find_element(how, what))
        select.select_by_visible_text(value)

    def switch(self):
        self.DRIVER.switch_to.alert.accept()

    def upload_file(self, how, what, value):
        """
        上传文件
        :param how:定位方法
        :param what:定位元素的属性值
        :param value:文件路径
        :return:
        """
        # self.DRIVER.execute_script(js)
        self.find_element(how, what).send_keys(value)

    def wait_for_element(self):
        ui.WebDriverWait(self.DRIVER, 10).until(ec.presence_of_element_located((By.CLASS_NAME, self.errorMsg)))





