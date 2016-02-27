#coding=utf-8
import MySQLdb

db = MySQLdb.connect("localhost", "yewen", "123456", "test") #连接数据库
cursor = db.cursor()

sql = "select * from user"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    #print results
    for raw in results:
        print raw
except:
    print "error"

db.close()