# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class Commond(object):
    SAVE_BTN = (By.CLASS_NAME, ".btn.btn-primary")


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
    # 结算账户的路径
    SEARCH_BTN = (By.XPATH, "/html/body/div[1]/div[2]/div/article/section/form/div/div[2]/button")  # 结算账户查询按钮
    ACCOUNT_NAME_SEARCH = (By.XPATH, "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul/li[1]/div/input")
    ACCOUNT_STORE_SEARCH = (By.XPATH,
                            "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul/li[2]/div[2]/select")
    ACCOUNT_NAME = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[1]/li[1]/div/input")  # 账户名称
    CASH_TYPE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[2]/li/div/label[1]/input")  # 现金类型
    BANK_TYPE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[2]/li/div/label[2]/input")  # 银行卡类型
    OTHER_TYPE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[2]/li/div/label[3]/input")  # 其它类型
    BANK_NAME = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[3]/li/div/input")  # 银行名称
    BANK_CARD = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[4]/li/div/input")  # 银行帐号
    INIT_DATA = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[5]/li/div/input")  # 期初金额
    COMMENT = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/ul[7]/li/div/textarea")  # 备注
    SAVE_BTN2 = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")  # 结算账户的保存按钮


class ProductData(object):
    # 菜单
    PRO_SER = (By.XPATH, "//*[@id='menus']/li[3]/a")  # 配件与服务
    PRODUCT = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[1]/a")  # 配件
    SERVICE = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[2]/a")  # 服务项目
    ADDITIONAL_EXPENSE = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[3]/a")  # 附加费用
    COMBO = (By.XPATH, "//*[@id='menus']/li[3]/ul/li[3]/a")  # 服务套餐

    SEARCH_KEY = (By.XPATH,
                  "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul[1]/li[1]/div/input")  # 关键字输入框
    SEARCH_CAR_MODELS = (By.XPATH,
                     "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul[1]/li[2]/div/input")  # 使用车型查询框
    SEARCH_STATUS = (By.XPATH,
                     "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul[1]/li[3]/div/select")  # 状态搜索框
    SEARCH_ATTR = (By.XPATH,
                   "/html/body/div[1]/div[2]/div/article/section/form/div/div[1]/ul[2]/li[1]/div/input")  # 自定义搜索框
    ADD_BTN = (By.XPATH, "/html/body/div[1]/div[2]/div/article/header/div/a[3]")  # 添加按钮
    DELETE_BTN = (By.XPATH, "/html/body/div[1]/div[2]/div/article/header/div/a[4]")  # 删除按钮
    UPDATE_ICON = (By.XPATH, "//*[@id='data-table']/tbody/tr[1]/td[2]/span[1]/a")  # 更新图标按钮
    DELETE_ICON = (By.XPATH, "//*[@id='data-table']/tbody/tr[1]/td[2]/span[2]/a")  # 删除图标按钮
    SAVE_BTN = (By.CLASS_NAME, ".btn.btn-primary")  # 保存按钮
    SEARCH_BTN = (By.XPATH, "/html/body/div[1]/div[2]/div/article/section/form/div/div[2]/button")  # 查询按钮
    CHECK_LINE = (By.XPATH, "//*[@id='data-table']/tbody/tr[1]")
    # 配件添加、修改信息
    PRODUCT_NAME = (By.NAME, "name")  # 配件名称
    PRODUCT_TYPE = (By.ID, "choose-parts-category")  # 配件分类
    PRODUCT_NO = (By.NAME, "product_no")  # 配件编号
    UNIT = (By.XPATH, "html/body/div[1]/div/div/div[2]/form/div/div/div/div[1]/ul[2]/li[2]/div/select")  # 单位
    PRODUCT_MODEL = (By.NAME, "model")  # 配件型号
    PRODUCT_BARCODE = (By.NAME, "barcode")  # 配件条形码
    # 配件库存下限
    PRODUCT_QUANTITY_LIMIT = (By.XPATH,
                              "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[1]/ul[3]/li[2]/div/input")
    PURCHASE_PRICE = (By.XPATH,
                      "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[1]/ul[4]/li[1]/div/input")  # 预计采购价
    PRODUCT_PRICE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[1]/ul[4]/li[2]/div/input")  # 参考售价
    PRODUCT_VIP_PRICE = (By.XPATH,
                         "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[1]/ul[4]/li[3]/div/input")  # VIP会员价
    CAR_MODELS = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[1]/ul[5]/li/div/input")  # 适用车型
    HIGH_SET = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/ul/li[2]/a")  # 高级设置
    CREDITS_RATIO = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[2]/ul[1]/li[1]/div/input")  # 积分比率
    ATTR1 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[2]/ul[2]/li[1]/div/input")  # 自定义属性1
    ATTR2 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[2]/ul[2]/li[2]/div/input")  # 自定义属性2
    ATTR3 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[2]/ul[2]/li[3]/div/input")  # 自定义属性3
    COMMENT = (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/div/div/div[2]/ul[4]/li/div/textarea")  # 备注






