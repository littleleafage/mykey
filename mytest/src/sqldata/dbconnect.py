#coding=utf-8

import MySQLdb

class dbConnect(object):

    def dbconnce(self):
        db = MySQLdb.connect(host="192.168.1.211", user="root", passwd="123456", db="cheche2", charset="utf8")
        return db


