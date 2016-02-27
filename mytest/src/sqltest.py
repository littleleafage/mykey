import sys
sys.path.append("/src/sqldata")
from src.sqldata.sqloperation import sqlOperation
from src.sqldata import *

class sqlTest(object):
    def sql_test(self):

        data = sqlOperation().sql_select("select name,age from user where age=123456")

        for m in data:
            print m

if __name__ == "__main__":
    sqlTest().sql_test()