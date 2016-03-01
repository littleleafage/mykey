# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re

def find_sec(secid):
    pa=re.compile(r'\w+')
    browser = webdriver.Firefox() # Get local session of firefox
    browser.get("http://bbs.byr.cn/#!section/%s "%secid) # Load page
    time.sleep(1) # Let the page load
    result=[]
    try:
        #获得版面名称和在线人数，形成列表
        board=browser.find_elements_by_class_name('title_1')
        ol_num=browser.find_elements_by_class_name('title_4')
        max_bindex=len(board)
        max_oindex=len(ol_num)
        assert max_bindex==max_oindex,'index not equivalent!'

        #版面名称有中英文，因此用正则过滤只剩英文的
        for i in range(1,max_oindex):
            board_en=pa.findall(board[i].text)
            result.append([str(board_en[0]),int(ol_num[i].text)])

        return result
    except NoSuchElementException:
        assert 0, "can't find element"

#打印分区5下面的所有板块的当前在线人数列表
print find_sec('5')