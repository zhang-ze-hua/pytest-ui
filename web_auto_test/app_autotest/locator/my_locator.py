from appium.webdriver.common.mobileby import MobileBy


class MyLocator:
    """我的页面&&&元素定位"""
    # 修改密码
    mine_menu = (MobileBy.XPATH, "//*[text()='修改密码']")
    # 退出
    button_quit = (MobileBy.XPATH, "//*[text()='退出']")
