import time
from selenium.webdriver.remote.webdriver import WebDriver
from common.base_page import BasePage
from locator.voucher_manage_locator import VoucherManageLocator


class VoucherManagePage(BasePage):
    """商户管理页面"""

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.driver.implicitly_wait(15)

    def create_shop_voucher(self, voucher_name, shop_name):
        self.click_element(VoucherManageLocator.button_create, "代金券管理--点击新增")
        self.click_element(VoucherManageLocator.voucher_type, "代金券管理--点击代金券类型")
        time.sleep(3)
        self.click_element(VoucherManageLocator.voucher_shop, "代金券管理--点击商户券")
        self.click_element(VoucherManageLocator.alert_button_confirm, "代金券管理--点击确定")
        time.sleep(3)
        self.input_text(VoucherManageLocator.voucher_name, voucher_name, "代金券管理--输入代金券名称")
        self.input_text(VoucherManageLocator.voucher_draw_start_time, "2021-03-17 00:00:00", "代金券管理--输入券领取的开始时间")
        time.sleep(1)
        self.input_text(VoucherManageLocator.voucher_draw_end_time, "2021-03-18 00:00:00", "代金券管理--输入券领取的结束时间")
        time.sleep(1)
        self.click_element(VoucherManageLocator.voucher_name, "代金券管理--点击代金券名称")
        self.click_element(VoucherManageLocator.valid_time_type, "代金券管理--点击有效期类型")
        self.click_element(VoucherManageLocator.valid_time_type_day, "代金券管理--点击天数")
        self.input_text(VoucherManageLocator.valid_day, 7, "代金券管理--输入有效天数")
        self.input_text(VoucherManageLocator.grant_total, 100, "代金券管理--输入发放总量")
        self.input_text(VoucherManageLocator.actual_pay_money, "10.00", "代金券管理--输入实付金额")
        self.input_text(VoucherManageLocator.voucher_money, "30.00", "代金券管理--输入代金券面值")
        self.input_text(VoucherManageLocator.bank_cost, "5.00", "代金券管理--输入银行成本")
        self.input_text(VoucherManageLocator.people_buy_count, 1, "代金券管理--输入每人购买次数")
        self.click_element(VoucherManageLocator.button_choice, "代金券管理--点击选择")
        time.sleep(1)
        self.input_text(VoucherManageLocator.input_shop_name, shop_name, "代金券管理--输入商户名称")
        self.click_element(VoucherManageLocator.button_query_2, "代金券管理--点击查询")
        self.click_element(VoucherManageLocator.left_choice_box, "代金券管理--点击左侧选择框")
        self.click_element(VoucherManageLocator.button_keep, "代金券管理--点击保存")
        time.sleep(1)
        self.input_text(VoucherManageLocator.voucher_describe, "123qwe", "代金券管理--输入券的描述")
        self.click_element(VoucherManageLocator.button_submit, "代金券管理--点击提交审核")

    def get_alert_error_info(self):
        """获取失败的弹窗提示信息"""
        ele = self.wait_element_presence(VoucherManageLocator.alert_error_info, '代金券_页面弹窗错误提示')
        return ele.text
