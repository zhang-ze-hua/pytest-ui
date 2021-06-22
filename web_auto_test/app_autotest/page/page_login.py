from app_autotest.common.base_page import BasePage
from app_autotest.locator.login_locator import LoginLocator
from app_autotest.locator.my_locator import MyLocator
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

    def login(self, user, pwd):
        """输入账号密码点击登录"""
        self.click_element(MyLocator.mine_menu, "点击我的")
        self.click_element(MyLocator.now_login, "点击立即登录")
        self.click_element(LoginLocator.more_way_login, "点击更多")
        self.click_element(LoginLocator.change_account, "点击切换/注册账号")
        self.input_text(LoginLocator.input_account, user, "输入手机号码")
        self.click_element(LoginLocator.register_login, "点击注册/登录")
        self.gesture_password(LoginLocator.gesture_password, pwd, "手势密码")

    def login1(self, user):
        """输入账号密码点击登录"""
        self.click_element(MyLocator.mine_menu, "点击我的")
        self.click_element(MyLocator.now_login, "点击立即登录")
        self.click_element(LoginLocator.more_way_login, "点击更多")
        self.click_element(LoginLocator.change_account, "点击切换/注册账号")
        self.input_text(LoginLocator.input_account, user, "输入手机号码")
        self.click_element(LoginLocator.register_login, "点击注册/登录")

    def get_error_info(self):
        """获取登录失败的提示信息"""
        return self.get_element_text(LoginLocator.error_info, '登录_失败提示信息')

    def get_alert_error_info(self):
        """获取页面弹窗的错误提示信息"""
        ele = self.wait_element_presence(LoginLocator.alert_error_info, '登录_页面弹窗错误提示')
        return ele.text

    def app_quit(self):
        """退出程序"""
        self.driver.quit()
    #
    # def click_re_mobile(self):
    #     """取消记住手机号"""
    #     self.click_element(loc.re_mobile, '登录_点击取消记住手机号')
