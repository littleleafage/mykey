#coding=utf-8
from src.common_functions.dbopera import sqlOpera

class sqlTest(object):

    def sqltest(self):
        data = sqlOpera().sql_select("select name from other_income_type")
        list = []
        for m in data:
            print m[0]
            list.append(m[0])

        print list

if __name__ == "__main__":
    sqlTest().sqltest()