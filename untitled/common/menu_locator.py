# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


# 菜单
class Menu(object):
    CRM = (By.XPATH, "/html/body/div[1]/article/section/ul/li[1]/a")
    ERP = (By.XPATH, "/html/body/div[1]/article/section/ul/li[2]/a")
    SETTING = (By.XPATH, "/html/body/div[1]/article/section/ul/li[3]/a")
    USER_PROFILE = (By.XPATH, "/html/body/div[1]/article/section/ul/li[4]/a")


class SystemMenu(object):
    SYSTEM = (By.XPATH, "//*[@id='menus']/li[1]/a")  # 系统
    GUIDE = (By.XPATH, "//*[@id='menus']/li[1]/ul/li[1]/a")  # 设置向导
    SYSTEM_INFO = (By.XPATH, "//*[@id='menus']/li[1]/ul/li[2]/a")  # 系统信息
    VIDEO = (By.XPATH, "//*[@id='menus']/li[1]/ul/li[3]/a")  # 操作视频


class OrderMenu(object):
    ORDER = (By.XPATH, "//*[@id='menus']/li[2]/a")  # 工单相关
    CHECK_STAND = (By.XPATH, "//*[@id='menus']/li[2]/ul/li[1]/a")  # 收银设置
    ORDER_SET = (By.XPATH, "//*[@id='menus']/li[2]/ul/li[2]/a")  # 工单设置
    QR_CODE = (By.XPATH, "//*[@id='menus']/li[2]/ul/li[3]/a")  # 收银二维码
    INVOICE = (By.XPATH, "//*[@id='menus']/li[2]/ul/li[4]/a")  # 单据打印


class ProSerMenu(object):
    PRO_SER = (By.XPATH, "//*[@id='menus']/li[3]/a")  # 配件与服务
    PRODUCT = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[1]/a")  # 配件
    SERVICE = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[2]/a")  # 服务项目
    ADDITIONAL_EXPENSE = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[3]/a")  # 附加费用
    COMBO = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[3]/a")  # 服务套餐


class UserMenu(object):
    USER_MENU = (By.XPATH, "//*[@id='menus']/li[4]/a")  # 员工
    USER = (By.XPATH, "//*[@id='menus']/li[4]/ul/li[1]/a")  # 员工
    USER_GROUP = (By.XPATH, "//*[@id='menus']/li[4]/ul/li[2]/a")  # 权限组
    LOGIN_LOG = (By.XPATH, "//*[@id='menus']/li[4]/ul/li[3]/a")  # 登录记录


class CommissionMenu(object):
    COMMISSION = (By.XPATH, "//*[@id='menus']/li[5]/a")  # 绩效
    TECHNICIAN_LEVEL = (By.XPATH, "//*[@id='menus']/li[5]/ul/li[1]/a")  # 技师等级
    COMMISSION_SERVICE = (By.XPATH, "//*[@id='menus']/li[5]/ul/li[2]/a")  # 项目提成
    COMMISSION_PRODUCT = (By.XPATH, "//*[@id='menus']/li[5]/ul/li[3]/a")  # 配件提成
    COMMISSION_RECHARGE = (By.XPATH, "//*[@id='menus']/li[5]/ul/li[4]/a")  # 充值提成
    COMMISSION_COMBO = (By.XPATH, "//*[@id='menus']/li[5]/ul/li[5]/a")  # 套餐提成


class WarehouseMenu(object):
    WAREHOUSE_STOCK = (By.XPATH, "//*[@id='menus']/li[6]/a")  # 库房
    SUPPLIER = (By.XPATH, "//*[@id='menus']/li[6]/ul/li[1]/a")  # 供应商
    SUPPLIER_TYPE = (By.XPATH, "//*[@id='menus']/li[6]/ul/li[2]/a")  # 供应商类型
    WAREHOUSE = (By.XPATH, "//*[@id='menus']/li[6]/ul/li[3]/a")  # 仓库
    INIT_STOCK = (By.XPATH, "//*[@id='menus']/li[6]/ul/li[4]/a")  # 期初库存
    UNIT = (By.XPATH, "//*[@id='menus']/li[6]/ul/li[5]/a")  # 单位


class CustomerMenu(object):
    CUSTOMER = (By.XPATH, "//*[@id='menus']/li[7]/a")  # 客户
    VIP_LEVEL = (By.XPATH, "//*[@id='menus']/li[7]/ul/li[1]/a")  # 会员等级
    CUSTOMER_TAG = (By.XPATH, "//*[@id='menus']/li[7]/ul/li[2]/a")  # 客户标签
    CUSTOMER_SOURCE = (By.XPATH, "//*[@id='menus']/li[7]/ul/li[3]/a")  # 客户来源


class FinanceMenu(object):
    FINANCE = (By.XPATH, "//*[@id='menus']/li[8]/a")  # 财务
    SETTLEMENT_ACCOUNT = (By.XPATH, "//*[@id='menus']/li[8]/ul/li[1]/a")  # 结算账户
    SETTLEMENT_TYPE = (By.XPATH, "//*[@id='menus']/li[8]/ul/li[2]/a")  # 结算方式
    EXPENSE_TYPE = (By.XPATH, "//*[@id='menus']/li[8]/ul/li[3]/a")  # 支出类型
    INCOME_TYPE = (By.XPATH, "//*[@id='menus']/li[8]/ul/li[4]/a")  # 收入类型
    INIT_RECEIVABLE = (By.XPATH, "//*[@id='menus']/li[8]/ul/li[5]/a")  # 应收期初
    INIT_PAYABLE = (By.XPATH, "//*[@id='menus']/li[8]/ul/li[6]/a")  # 应付期初


class StoreMenu(object):
    STORE = (By.XPATH, "//*[@id='menus']/li[9]/a")  # 分店设置


class ImportMenu(object):
    DATA_IMPORT = (By.XPATH, "//*[@id='menus']/li[10]/a")  # 数据导入


# 数据
class LoginData(object):
    STORE_ID = (By.NAME, "store_id")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CLASS_NAME, "login-btn")
    LOGIN_USER = (By.ID, "top-user-logout")
    LOG_PAGE_TITLE = u'车车云智慧系统-商户登录'


class FinanceData(object):
    SEARCH = (By.XPATH, "/html/body/div[1]/div[2]/div/article/header/div/div/input")  # 查询输入框
    CHECK_LINE = (By.XPATH, "//*[@id='data-table']/tbody/tr/td[2]")  # 用于比对查询结果
    DELETE_BTN = (By.XPATH, "//*[@id='data-table']/tbody/tr/td[1]/span[2]/a")  # 删除按钮
    ADD_BTN = (By.XPATH, "/html/body/div[1]/div[2]/div/article/header/div/a")  # 添加按钮
    UPDATE_BTN = (By.XPATH, "//*[@id='data-table']/tbody/tr/td[1]/span[1]/a")  # 更新按钮
    SAVE_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[1]")  # 保存按钮
    INPUT_VALUE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul/li/div[2]/input")  # 类型/方式输入框
    # 结算账户页面的名称和门店搜索框
    ACCOUNT_NAME_SEARCH = (By.XPATH, "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul/li[1]/div/input")
    ACCOUNT_STORE_SEARCH = (By.XPATH,
                            "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul/li[2]/div[2]/select")





