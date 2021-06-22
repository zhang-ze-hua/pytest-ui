from appium.webdriver.common.mobileby import MobileBy


class LoginLocator:
    """登录页面的元素定位"""
    # 更多方式登录
    more_way_login = (MobileBy.ID, "com.mobile.mbank.login:id/tv_changeLoginWay")
    # 登录
    login = (MobileBy.ID, "com.mobile.mbank.login:id/btn_login")
    # 切换/注册账号
    # change_account = (MobileBy.ID, "com.mobile.mbank.common:id/tv_item")
    change_account = (MobileBy.XPATH, "//*[@text='切换/注册账号']")
    # 请输入手机号码/身份证号码
    input_account = (MobileBy.ID, "com.mobile.mbank.login:id/et_login")
    # 注册/登录
    register_login = (MobileBy.ID, "com.mobile.mbank.login:id/btn_login")
    # 手势密码九宫格
    gesture_password = (MobileBy.ID, "com.mobile.mbank.login:id/pv_lock")
    # 手势密码错误
    error_info = (MobileBy.XPATH, "//*[@text='手势密码的连接点必须在4个点以上，请重新输入']")
    # 账户不能为空
    alert_error_info = (MobileBy.XPATH, "//*[@text='账户不能为空']")
