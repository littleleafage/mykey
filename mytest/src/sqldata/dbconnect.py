import MySQLdb

class dbConnect(object):

    def dbconnce(self):
        db = MySQLdb.connect("localhost", "yewen", "123456", "test")
        return db

if __name__ == "__main":
    dbConnect().dbconnce()

