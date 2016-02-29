#coding=utf-8
import sys
sys.path.append("/src/sqldata")
from src.sqldata.sqloperation import sqlOperation

class sqlTest(object):
    def sql_test(self):
        data = sqlOperation().sql_select("select name from other_income_type")
        list = []
        for m in data:
            list.append(m[0])

        print list[0]

if __name__ == "__main__":
    sqlTest().sql_test()