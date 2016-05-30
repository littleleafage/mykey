# -*- coding: utf-8 -*-


class BasePage(object):

    def __init__(self, driver, base_url, page_title):
        self.base_url = base_url
        self.page_title = page_title
        self.driver = driver
        self.verificationErrors = []
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 重写定义send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print u'%s 页面中未能找到%s元素' % (self, loc)

    # 定义script方法，用于执行js脚本
    def script(self, src):
        return self.driver.execute_script(src)

    # 重写teardown
    def teardown(self):
        self.driver.get('')
        self.driver.tearDown()
