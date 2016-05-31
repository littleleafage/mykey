# -*- coding: utf-8 -*-
from testcase.finance.expense_type import FinanceTest
import unittest

if __name__ == '__main__':
    tests = unittest.TestSuite()
    tests.addTest(unittest.TestLoader().loadTestsFromTestCase(FinanceTest))
    unittest.TextTestRunner(verbosity=2).run(tests)
