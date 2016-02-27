#coding=utf-8

import os
import unittest
from src.testcase.login.login import TestcaseLogin
from src.testcase.TestCase_Upload.uploadfile import TestCaseFile
import HTMLTestRunner

suite = unittest.TestSuite() #定义一个单元测试容器
suite.addTest(TestcaseLogin("testcase_login")) #将测试用例加入到测试容器中
suite.addTest(TestCaseFile("testcase_file"))

dir = os.getcwd()
#print dir
logfile= open(dir + "\log.html", 'wb') #测试报告存放位置
runner = HTMLTestRunner.HTMLTestRunner(stream=logfile, title=u'测试报告', description=u'报告详情')

runner.run(suite) #运行测试用例集
logfile.close() #关闭文件