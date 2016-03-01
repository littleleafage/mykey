#coding=utf-8
from src.common_functions.dbopera import sqlOpera
import demjson

class sqlTest(object):

    def sqltest(self):
        data = sqlOpera().sql_select("select * from other_income_type")
        list = []
        length = len(data)
        i = 0
        while(i<length):
            list = data[i]
            for m in list:
                if m == u'生活费':
                    print m
            i = i + 1
if __name__ == "__main__":
    sqlTest().sqltest()