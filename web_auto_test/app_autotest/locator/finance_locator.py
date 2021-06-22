from appium.webdriver.common.mobileby import MobileBy


class FinanceLocator:
    """理财页面&&&元素定位"""
    # 我的
    finance_menu = (MobileBy.ID, "com.mobile.mbank.launcher:id/tab_finance")
