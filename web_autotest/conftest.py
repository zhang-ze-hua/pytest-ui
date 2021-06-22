import pytest
import time
from selenium import webdriver
from common.handle_config import conf
from common.handle_logging import log
from data.case_data import LoginCase
from locator.my_locator import MyLocator
from page.page_login import LoginPage
from page.page_pwd_change import PwdChangePage
from page.page_role_manage import RoleManagePage
from page.page_shop_manage import ShopManagePage
from page.page_voucher_manage import VoucherManagePage


@pytest.fixture()
def login_fixture():
    """登录功能的前置后置"""
    # 前置条件
    log.info("开始执行登录的用例")
    url = "http://" + conf.get("address", "ip") + ":" + conf.get("address", "port") + conf.get("address", "login_url")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    log.info("登录的用例执行完毕")
    login_page = LoginPage(driver)
    yield login_page
    # 后置条件
    driver.quit()


@pytest.fixture()
def pwd_change_fixture():
    """修改密码功能的前置后置"""
    # 前置条件
    log.info("开始执行用例")
    url = "http://" + conf.get("address", "ip") + ":" + conf.get("address", "port") + conf.get("address", "login_url")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    login_page = LoginPage(driver)
    pwd_change_driver = PwdChangePage(driver)
    login_page.login(LoginCase.success_case_data[0]["mobile"], LoginCase.success_case_data[0]["pwd"])
    pwd_change_driver.click_element(MyLocator.button_change_pwd, "修改密码")
    time.sleep(5)
    yield login_page, pwd_change_driver
    # 后置条件
    driver.quit()
    log.info("用例执行完毕")


@pytest.fixture()
def role_manage_fixture():
    """角色管理功能的前置后置"""
    # 前置条件
    log.info("开始执行用例")
    url = "http://" + conf.get("address", "ip") + ":" + conf.get("address", "port") + conf.get("address", "login_url")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    login_page = LoginPage(driver)
    role_manage_driver = RoleManagePage(driver)
    login_page.login(LoginCase.success_case_data[0]["mobile"], LoginCase.success_case_data[0]["pwd"])
    role_manage_driver.click_element(MyLocator.menu_system_manage, "点击系统管理")
    role_manage_driver.click_element(MyLocator.menu_role_manage, "点击角色管理")
    time.sleep(3)
    yield login_page, role_manage_driver
    # 后置条件
    driver.quit()
    log.info("用例执行完毕")


@pytest.fixture()
def shop_manage_fixture():
    """商户管理功能的前置后置"""
    # 前置条件
    log.info("开始执行用例")
    url = "http://" + conf.get("address", "ip") + ":" + conf.get("address", "port") + conf.get("address", "login_url")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    login_page = LoginPage(driver)
    shop_manage_driver = ShopManagePage(driver)
    login_page.login(LoginCase.success_case_data[0]["mobile"], LoginCase.success_case_data[0]["pwd"])
    shop_manage_driver.click_element(MyLocator.menu_shop_manage, "点击商户管理")
    shop_manage_driver.click_element(MyLocator.menu_shop_info_list, "点击商户信息列表")
    time.sleep(3)
    yield login_page, shop_manage_driver
    # 后置条件
    driver.quit()
    log.info("用例执行完毕")


@pytest.fixture()
def voucher_manage_fixture():
    """代金券管理功能的前置后置"""
    # 前置条件
    log.info("开始执行用例")
    url = "http://" + conf.get("address", "ip") + ":" + conf.get("address", "port") + conf.get("address", "login_url")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    login_page = LoginPage(driver)
    voucher_manage_driver = VoucherManagePage(driver)
    login_page.login(LoginCase.success_case_data[0]["mobile"], LoginCase.success_case_data[0]["pwd"])
    voucher_manage_driver.click_element(MyLocator.menu_voucher_manage, "点击代金券管理")
    voucher_manage_driver.click_element(MyLocator.menu_voucher_manage_2, "点击代金券管理")
    time.sleep(3)
    yield login_page, voucher_manage_driver
    # 后置条件
    driver.quit()
    log.info("用例执行完毕")
    log.info("==================================================")
    log.info("")
    log.info("")
