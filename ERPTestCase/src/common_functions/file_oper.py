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
        DOC = ET.parse("../testdata/" + filename)

    def read_xml(self, ftagname):
        '''
        从指定的文件中读取指定节点的值
        :param ftagname: 节点的路径，如：login/username
        :return:返回节点的值
        '''
        path = './' + ftagname
        temp = []
        root = DOC.findall(path)
        for child in root:
            temp.append(child.text)
        return temp

    def readxml_length(self, ftagname):
        path = './' + ftagname
        root = DOC.findall(path)
        temp = []
        for child in root:
            for tem in child.getchildren():
                temp.append(tem.text)
                print tem
            # length = len(child.getchildren())

        return temp

if __name__ == '__main__':
    FileOpera('erpmenutext.xml').readxml_length('menu')
    # for m in data:
    #     print m

