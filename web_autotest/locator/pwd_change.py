from selenium.webdriver.common.by import By


class PwdChangeLocator:
    """修改密码页面&&&元素定位"""
    # 原密码
    old_pwd = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[2]/div/div/input")
    # 新密码
    new_pwd = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[2]/div/div/input")
    # 确认密码
    confirm_pwd = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[4]/div/div/input")
    # 原密码不能为空
    old_pwd_empty = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[2]/div/div[2]")
    # 新密码不能为空
    new_pwd_empty = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[3]/div/div[2]")
    # 确认密码不能为空
    confirm_pwd_empty = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[4]/div/div[2]")
    # 确认密码与新密码不一致
    confirm_pwd_new_pwd_difference = (By.XPATH, "/html/body/div[3]/div/div[2]/form/div[4]/div/div[2]")
    # 原密码不正确
    old_pwd_error = (By.XPATH, "/html/body/div[5]/p")
    # 操作成功
    pwd_change_pass = (By.XPATH, "/html/body/div[5]/p")
    # 取消
    button_cancel = (By.XPATH, "//*[text()='取消']")
    # 确定
    button_confirm = (By.XPATH, "//*[text()='确定']")
