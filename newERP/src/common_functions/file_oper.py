# -*- coding: utf-8 -*-
'''
对测试数据进行读取操作
'''
from xml.dom import minidom
from xml.etree import ElementTree as ET


class FileOpera(object):

    def __init__(self, filename):
        '''
        初始化xml文档
        :param filename:
        :return:
        '''
        global DOC,CONN
        DOC = ET.parse("G:\\webdriver\\newERP\\src\\testdata\\" + filename)

    def read_xml(self, ftagname):
        '''
        从指定的文件中读取指定节点的值
        :param ftagname: 节点的路径，如：login/username
        :return:返回节点的值
        '''
        path = './' + ftagname
        root = DOC.findall(path)
        for child in root:
            return child.text

    def readxml_length(self, ftagname):
        path = './' + ftagname
        root = DOC.findall(path)
        length = ''
        for child in root:
            length = len(child.getchildren())

        return length

    def read_texts(self, ftagname):
        path = './' + ftagname
        root = DOC.findall(path)
        text = []
        for childs in root:
            for child in childs.getchildren():
                text.append(child.text)

        return text

if __name__ == '__main__':
    list_data = FileOpera('order_list.xml').read_texts('list')
    length = len(list_data)
    print length
    for i in range(0, length-2, 1):
        print list_data[i]

