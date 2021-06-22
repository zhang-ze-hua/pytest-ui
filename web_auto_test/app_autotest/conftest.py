import pytest
from app_autotest.common.handle_config import conf
from app_autotest.common.handle_logging import log
from app_autotest.common.handle_driver import driver
from app_autotest.page.page_login import LoginPage


@pytest.fixture()
def login_fixture():
    """登录功能的前置后置"""
    # 前置条件
    log.info("开始执行登录的用例")
    login_page = LoginPage(driver)
    yield login_page
    # 后置条件
    driver.quit()
    log.info("登录的用例执行完毕\n\n\n")


