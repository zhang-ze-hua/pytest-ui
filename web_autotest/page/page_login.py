import re
import time
from common.base_page import BasePage
from locator.login_locator import LoginLocator
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    """登录页面"""

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.driver.implicitly_wait(15)

    def login(self, phone, pwd):
        """输入账号密码点击登录"""
        self.input_text(LoginLocator.login_phone, phone, "输入手机号")
        self.input_text(LoginLocator.login_pwd, pwd, "输入密码")
        verification_code = self.get_verification_code(LoginLocator.login_verification_code_image, "src", "获取图形验证码")
        self.input_text(LoginLocator.login_verification_code, verification_code, "输入图形验证码")
        self.click_element(LoginLocator.get_sms_code, "点击获取短信验证码")
        time.sleep(3)
        sms_code = self.db2_sms_code(phone)
        self.input_text(LoginLocator.login_sms_code, sms_code, "输入短信验证码")
        self.click_element(LoginLocator.login_button, "点击登录")

    def login2(self, phone, pwd):
        """输入账号密码点击登录"""
        self.input_text(LoginLocator.login_phone, phone, "输入手机号")
        self.input_text(LoginLocator.login_pwd, pwd, "输入密码")
        verification_code = self.get_verification_code(LoginLocator.login_verification_code_image, "src", "获取图形验证码")
        self.input_text(LoginLocator.login_verification_code, verification_code, "输入图形验证码")
        self.click_element(LoginLocator.get_sms_code, "点击获取短信验证码")

    def get_verification_code(self, locator, attr_name, img_info):
        src = self.get_element_attribute(locator, attr_name, img_info)
        uuid = re.findall("uuid=(.*)", src)[0]
        verification_code = self.mysql_verification_code(uuid)
        return verification_code

    def get_error_info(self):
        """获取失败的页面提示信息"""
        return self.get_element_text(LoginLocator.error_case_pwd_empty, '登录_失败提示信息')

    def get_alert_error_info(self):
        """获取失败的弹窗提示信息"""
        ele = self.wait_element_presence(LoginLocator.error_case_phone_error, '登录_页面弹窗错误提示')
        return ele.text

