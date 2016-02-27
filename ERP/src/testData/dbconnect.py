'''
连接数据库 to connect database
'''
import MySQLdb

class dbConnect(object):

    def dbconnce(self):
        db = MySQLdb.connect("localhost", "yewen", "123456", "test")
        return db

