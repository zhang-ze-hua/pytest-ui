from selenium.webdriver.common.by import By


class RoleManageLocator:
    """角色管理页面&&&元素定位"""
    # ==================================左上角按钮===================================
    # 输入角色名称
    input_role_name = (By.XPATH, "//input[@placeholder='角色名称']")
    # 查询
    button_query = (By.XPATH, "//*[@id='pane-sys-role']/div/div/div/form/div[2]/div/button[1]")
    # 新增
    button_create = (By.XPATH, "//*[@id='pane-sys-role']/div/div/div/form/div[2]/div/button[2]")
    # 批量删除
    button_batch_delete = (By.XPATH, "//*[@id='pane-sys-role']/div/div/div/form/div[2]/div/button[3]")
    # ==================================左上角按钮===================================

    # ==================================中间表单=====================================
    # 修改
    button_modify = (By.XPATH, "//*[@id='pane-sys-role']/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr/td[6]/div/button[1]/span")
    # 删除
    button_delete = (By.XPATH, "//*[@id='pane-sys-role']/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr/td[6]/div/button[2]")
    # ==================================中间表单=====================================

    # ==================================右下角翻页栏=================================
    # 修改密码

    # ==================================右下角翻页栏=================================

    # ==================================弹窗=========================================
    # 输入角色名称
    alert_input_role_name = (By.XPATH, '//*[@id="pane-sys-role"]/div/div/div/div[3]/div/div[2]/form/div[1]/div/div/input')
    # 备注
    alert_input_role_note = (By.XPATH, "//input[@placeholder='备注']")
    # 取消
    alert_button_cancel = (By.XPATH, '//*[@id="pane-sys-role"]/div/div/div/div[3]/div/div[3]/span/button[1]')
    # 确定
    alert_button_confirm = (By.XPATH, '//*[@id="pane-sys-role"]/div/div/div/div[3]/div/div[3]/span/button[2]')
    # 角色名称不能为空
    alert_role_name_empty = (By.XPATH, "//*[contains(text(),'角色名称不能为空')]")
    # ==================================弹窗=========================================
