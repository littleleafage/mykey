#coding=utf-8
from src.testcase.testcaselogin import TestCaseLogin
import HTMLTestRunner
import os
import unittest

suite = unittest.TestSuite()
suite.addTest(TestCaseLogin("testcase_login"))
# suite.addTest(TestCaseLogin("testcase_logout"))

dir = os.getcwd()
#print dir
logfile= open(dir + "\log.html", 'wb') #测试报告存放位置
runner = HTMLTestRunner.HTMLTestRunner(stream=logfile, title=u'测试报告', description=u'报告详情')

runner.run(suite) #运行测试用例集
logfile.close() #关闭文件

