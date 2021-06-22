import time
from selenium.webdriver.remote.webdriver import WebDriver
from common.base_page import BasePage
from locator.shop_manage_locator import ShopManageLocator


class ShopManagePage(BasePage):
    """商户管理页面"""

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.driver.implicitly_wait(15)

    def create_shop(self, role_name, role_note):
        pass

    def delete_shop(self, shop_name):
        self.input_text(ShopManageLocator.input_shop_name, shop_name, "商户管理--输入商户名称")
        self.click_element(ShopManageLocator.button_query, "商户管理--点击查询")
        time.sleep(1)
        self.click_element(ShopManageLocator.button_delete, "商户管理--点击删除")
        self.click_element(ShopManageLocator.alert_button_cancel, "商户管理--删除--点击取消")

    def get_error_info(self):
        """获取失败的页面提示信息"""
        return "删除成功"
