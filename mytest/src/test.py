#coding=utf-8

import time
import unittest
from selenium import webdriver
from src.common_functions.webdriver_help import WebDriverHelp


class test(unittest.TestCase):

    def test(self):
        WebDriverHelp("open", "chrome", "local").setup()
        time.sleep(1)
        # driver.maximize_window()
        # driver.set_window_position(100, 100, windowHandle='current') #设置当前窗口的位置
        # driver.set_window_size(800, 1000, windowHandle='current') #设置当前窗口的大小
        loginlist = [['byname', 'store_id', '10054'], ['byname', 'username', 'yewen'], ['byname', 'password', '123456']]
        WebDriverHelp().inputvalue(loginlist)
        # driver.find_element_by_name('store_id').send_keys('10054')
        # driver.find_element_by_name('username').send_keys('wzz')
        # driver.find_element_by_name('password').send_keys('123456')
        # driver.find_element_by_class_name('login-btn').click()
        time.sleep(1)
        # driver.find_element_by_xpath("//*[@id='navi-tabs']/a[1]").click()
        # time.sleep(0.5)
        # driver.find_element_by_xpath("//*[@id='menu-member']/a").click()
        # time.sleep(0.5)
        # driver.find_element_by_xpath("//*[@id='menu-member']/ul/li[2]/a").click()
        # time.sleep(1)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #将页面滚动到最底部 To scroll to the bottom of a page
        # time.sleep(5)
        # driver.get('http://s2.checheweike.com/store/index.php?route=member/vip_user')

        # content = driver.find_element_by_xpath('//*[@id="data-table"]/tbody/tr').text
        # j = json.loads(content)
        # print j


