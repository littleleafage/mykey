#coding=utf-8
'''
对测试数据进行读取操作
'''
from xml.dom import minidom

#global DOC,CONN

class DataOperations(object):

    def __init__(self, filename):
        '''
        初始化xml文档
        :param filename:
        :return:
        '''
        global DOC,CONN
        DOC = minidom.parse("../../testData/" + filename)

    def read_xml(self, ftagname, num, stagname):
        '''
        从指定的文件中读取指定节点的值
        :param ftagname: 起始节点的名称
        :param num: 取与起始节点相同的第num个节点
        :param stagname:起始节点下的二级节点
        :return:返回二级节点的值
        '''
        root = DOC.documentElement
        message = root.getElementsByTagName(ftagname)[num]
        return message.getElementsByTagName(stagname)[0].childNodes[0].nodeValue

    def readxml_attribute(self, ftagname, num, stagname,attributeName):
        '''
        从指定的文件中读取指定节点的属性
        :param ftagname: 起始节点的名称
        :param num: 取与起始节点相同的第num个节点
        :param stagname:起始节点下的二级节点
        :param attributeName:二级节点的属性名
        :return:返回二级节点的属性
        '''
        root = DOC.documentElement
        message = root.getElementsByTagName(ftagname)[num]
        return message.getElementsByTagName(stagname)[0].getAttribute(attributeName)