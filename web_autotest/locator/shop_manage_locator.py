from selenium.webdriver.common.by import By


class ShopManageLocator:
    """商户管理页面&&&元素定位"""
    # ==================================左上角按钮===================================
    # 输入商户名
    input_shop_name = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/form/div[1]/div/div/input')
    # 查询
    button_query = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/form/div[5]/div/button[1]')
    # 新增
    button_create = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/form/div[5]/div/button[2]')
    # 批量删除
    button_batch_delete = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/form/div[5]/div/button[3]')
    # 审批状态
    approval_state = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/form/div[2]/div/div/div[1]/input')
    # 审核中
    approval_ing = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[4]/span')

    # ==================================左上角按钮===================================

    # ==================================中间表单=====================================
    # 删除
    button_delete = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[2]/span')
    # ==================================中间表单=====================================

    # ==================================右下角翻页栏=================================
    # 修改密码

    # ==================================右下角翻页栏=================================

    # ==================================弹窗=========================================
    # 取消
    alert_button_cancel = (By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
    # 确定
    alert_button_confirm = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')
    # ==================================弹窗=========================================
