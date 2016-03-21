# -*- coding: utf-8 -*-
import unittest
from src.common_functions.qt_opera import QT_Opera
from src.common_functions.webdriver_help import WebDriverHelp
from src.common_functions.file_oper import FileOpera


class TestMenu(unittest.TestCase):

    def setUp(self):
        QT_Opera().login()

    def test_menu(self):
        data = FileOpera('erpmenutext.xml').readxml_length('menu')
        QT_Opera().menu(data)

    def tearDown(self):
        WebDriverHelp().teardown()



