#coding=utf-8
from src.common_functions.qt_operations import Operations
import unittest


class Login(unittest.TestCase):

    def test_login(self):
        Operations().login()
        self.assertEqual('', '', msg='')

