#coding=utf-8
from selenium import webdriver
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
print driver.title

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    element = driver.execute_script("return $('.cheese')[0]")
    # You should see "cheese! - Google Search"
    print element

finally:
    driver.quit()

# driver = webdriver.Chrome()
# driver.get('http://s2.checheweike.com/erp')
# driver.find_element_by_name('store_id').send_keys('10054')
# driver.find_element_by_name('username').send_keys('yewen')
# driver.find_element_by_name('password').send_keys('ccwk0715')
# driver.find_element_by_class_name('login-btn').click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='menu-stock']/a").click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-stock"]/ul/li[1]/a').click()
# time.sleep(1)
# ele = driver.find_elements_by_xpath("//*[@id='data-table']/thead/tr/th")
# list = []
# for i in ele:
#     list.append(i.text)
# for m in list:
#     print m
# print time.localtime(time.time())
