from src.sqldata.dbconnect import dbConnect

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