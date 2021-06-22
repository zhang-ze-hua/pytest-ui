from selenium.webdriver.remote.webdriver import WebDriver
from locator.pwd_change import PwdChangeLocator
from common.base_page import BasePage


class PwdChangePage(BasePage):
    """修改密码页面"""

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.driver.implicitly_wait(15)

    def input_pwd(self, old_pwd, new_pwd, confirm_pwd):
        self.input_text(PwdChangeLocator.old_pwd, old_pwd, "输入原密码")
        self.input_text(PwdChangeLocator.new_pwd, new_pwd, "输入新密码")
        self.input_text(PwdChangeLocator.confirm_pwd, confirm_pwd, "输入确认密码")
        self.click_element(PwdChangeLocator.button_confirm, "点击确定")

    def get_error_info(self):
        """获取失败的页面提示信息"""
        return self.get_element_text(PwdChangeLocator.old_pwd_empty, '原密码不能为空')

    def get_alert_error_info(self):
        """获取失败的弹窗提示信息"""
        ele = self.wait_element_presence(PwdChangeLocator.old_pwd_error, '原密码不正确')
        return ele.text

    def get_alert_pass_info(self):
        """获取成功的弹窗提示信息"""
        ele = self.wait_element_presence(PwdChangeLocator.pwd_change_pass, '密码修改成功')
        return ele.text
