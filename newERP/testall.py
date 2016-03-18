# -*- coding: utf-8 -*-
'''
数据查询
'''
from src.common_functions.file_oper import FileOpera

print FileOpera('login_data.xml').read_xml('login/username')
# print FileOpera('login_data.xml').readxml_length('login_data.xml')
