#coding=utf8

from src.sqldata.dbconnect import dbConnect

class sqlOperation(object):
    def sql_select(self,sql):
        db = dbConnect().dbconnce()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def closedb(self):
        db = dbConnect().dbconnce()
        db.close()
