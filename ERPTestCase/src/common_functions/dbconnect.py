#coding=utf-8
'''
连接数据库，并返回数据库对象
by：yewen
data_added：2016-02-25
'''
import MySQLdb

class dbConnect(object):

    def dbconnect(self):
        return MySQLdb.connect("localhost", "yewen", "123456", "test")


if __name__ == "__main__":
    dbConnect().dbconnect()