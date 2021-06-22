from appium.webdriver.common.mobileby import MobileBy


class LoginLocator:
    """登录页面的元素定位"""
    # 手机号
    login_phone = (MobileBy.XPATH, "/html/body/div/div/div[1]/form/div[1]/div/div/input")
    # 密码
    login_pwd = (MobileBy.XPATH, "//input[@placeholder='密码']")
    # 验证码
    login_verification_code = (MobileBy.XPATH, "/html/body/div/div/div[1]/form/div[3]/div/div[1]/div[1]/div/input")
    # 验证码图片
    login_verification_code_image = (MobileBy.XPATH, "/html/body/div/div/div[1]/form/div[3]/div/div[1]/div[2]/img")
    # 短信验证码
    login_sms_code = (MobileBy.XPATH, "/html/body/div/div/div[1]/form/div[4]/div/div[1]/div[1]/div/input")
    # 获取短信验证码
    get_sms_code = (MobileBy.XPATH, "/html/body/div/div/div[1]/form/div[4]/div/div[1]/div[2]/button/span")
    # 登录
    login_button = (MobileBy.XPATH, "//button/*[text()='登录']")
    # 请输入正确的手机号
    error_case_phone_error = (MobileBy.XPATH, "//*[contains(text(),'请输入正确的手机号')]")
    # 密码不能为空
    error_case_pwd_empty = (MobileBy.XPATH, "//*[contains(text(),'密码不能为空')]")
