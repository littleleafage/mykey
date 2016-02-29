#coding=utf-8
'''
连接数据库，并返回数据库对象
by：yewen
data_added：2016-02-25
'''
import MySQLdb

class dbConnect(object):

    def dbconnect(self):
        return MySQLdb.connect(host="192.168.1.211", user="root", passwd="123456", db="cheche2", charset="utf8")
