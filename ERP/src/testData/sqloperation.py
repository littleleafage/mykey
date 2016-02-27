#coding=utf-8
'''
数据库的相关操作  The operations of database
'''
from src.testData.dbconnect import dbConnect

class sqlOperation(object):
    def sql_select(self,sql):
        db = dbConnect().dbconnce()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        return data
        db.close()

if __name__ == "__main__":
    sqlOperation().sql_select()