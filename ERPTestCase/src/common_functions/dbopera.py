#coding=utf-8
'''
数据库的操作
by：yewen
data_added：2016-02-25
'''
from src.common_functions.dbconnect import dbConnect

class sqlOpera(object):
    def sql_select(self,sql):
        db = dbConnect().dbconnce()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        return data
        db.close()

if __name__ == "__main__":
    sqlOpera().sql_select()