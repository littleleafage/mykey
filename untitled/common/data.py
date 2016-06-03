# -*- coding: utf-8 -*-
"""
数据存放
"""


class FinanceData(object):
    SETTLEMENT_ACCOUNT = {'name': 'autotest', 'bank_name': u'中行', 'bank_no': '32454', 'init_money': 30,
                          'comment': u'备注信息'}  # 结算账户信息
    FINANCE_TYPE = {'name': 'autotest', 'update_name': 'autotest1'}  # 结算方式、支出、收入类型信息


class ProductServiceData(object):
    PRODUCT = {'name': 'autotest', 'type': '', 'no': '', 'unit': '', 'model': '', 'barcode': '', 'quanity_limit': 0,
               'purchase_price': '', 'price': '', 'vip_price': '', 'car_model': '', 'credits_radio': '', 'attr1': '',
               'attr2': '', 'attr3': '', 'comment': ''}  # 配件数据
