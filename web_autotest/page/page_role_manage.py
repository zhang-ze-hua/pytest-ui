import time
from selenium.webdriver.remote.webdriver import WebDriver
from common.base_page import BasePage
from locator.role_manage_locator import RoleManageLocator


class RoleManagePage(BasePage):
    """角色管理页面"""

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.driver.implicitly_wait(15)

    def create_role(self, role_name, role_note):
        self.click_element(RoleManageLocator.button_create, "角色管理--点击新增")
        time.sleep(3)
        self.input_text(RoleManageLocator.alert_input_role_name, role_name, "角色管理--新增--输入角色名称")
        self.input_text(RoleManageLocator.alert_input_role_note, role_note, "角色管理--新增--输入备注")
        self.click_element(RoleManageLocator.alert_button_confirm, "角色管理--新增--点击确定")

    def modify_role(self, old_role_name, new_role_name, new_role_note):
        self.input_text(RoleManageLocator.input_role_name, old_role_name, "角色管理--输入角色名称")
        self.click_element(RoleManageLocator.button_query, "角色管理--点击查询")
        time.sleep(1)
        self.click_element(RoleManageLocator.button_modify, "角色管理--点击修改")
        time.sleep(1)
        self.input_text(RoleManageLocator.alert_input_role_name, new_role_name, "角色管理--新增--输入角色名称")
        time.sleep(5)
        self.input_text(RoleManageLocator.alert_input_role_note, new_role_note, "角色管理--新增--输入备注")
        time.sleep(5)
        self.click_element(RoleManageLocator.alert_button_confirm, "角色管理--新增--点击确定")

    def get_error_info(self):
        """获取失败的页面提示信息"""
        ele = self.wait_element_presence(RoleManageLocator.alert_role_name_empty, "角色名称不能为空")
        return ele.text
