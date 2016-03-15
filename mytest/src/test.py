#coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.zhihu.com/#signin")
driver.implicitly_wait(10)
account = driver.find_element_by_name('account')
account.send_keys('')
password = driver.find_element_by_name('password')
password.send_keys('')
# button = driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div[2]/form/div[3]/button')
# actions = ActionChains(driver)
# actions.move_to_element(button)
# actions.click(button)
driver.find_element_by_class_name('sign-button').click()
time.sleep(2)




