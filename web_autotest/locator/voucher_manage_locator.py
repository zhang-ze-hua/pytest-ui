from selenium.webdriver.common.by import By


class VoucherManageLocator:
    """代金券管理页面&&&元素定位"""
    # ==================================左上角按钮===================================
    # 输入代金券名称
    input_voucher_name = (By.XPATH, '//*[@id="pane-coupon-couponList"]/div/div/div/form/div[1]/div/div/input')
    # 查询
    button_query = (By.XPATH, '//*[@id="pane-coupon-couponList"]/div/div/div/form/div[5]/div/button[1]')
    # 新增
    button_create = (By.XPATH, '//*[@id="pane-coupon-couponList"]/div/div/div/form/div[5]/div/button[2]')
    # 删除
    button_batch_delete = (By.XPATH, '//*[@id="pane-coupon-couponList"]/div/div/div/form/div[5]/div/button[3]')
    # ==================================左上角按钮===================================

    # ==================================中间表单=====================================
    # 删除
    button_delete = (By.XPATH, '//*[@id="pane-merchant-merchantList"]/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[2]/span')
    # ==================================中间表单=====================================

    # ==================================右下角翻页栏=================================

    # ==================================右下角翻页栏=================================

    # ==================================请选择需要新增券的类型=======================
    # 确定
    alert_button_confirm = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div[2]/div/button[1]')
    # 取消
    alert_button_cancel = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div[2]/div/button[2]')
    # 代金券类型
    voucher_type = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div[1]/div/div/div[1]/input')
    # 商户券
    voucher_shop = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')

    # ==================================请选择需要新增券的类型========================

    # ==================================商户券信息====================================
    # 代金券名称
    voucher_name = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[1]/div/div/div[1]/input')
    # 券领取的开始时间
    voucher_draw_start_time = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[2]/div/div/div[1]/input')
    # 券领取的结束时间
    voucher_draw_end_time = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[3]/div/div/div/input')
    # 有效期类型
    valid_time_type = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[4]/div/div/div/div[1]')
    # 天数
    valid_time_type_day = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
    # 有效天数
    valid_day = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[5]/div/div/div[1]/input')
    # 发放总量
    grant_total = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[6]/div/div/div/input')
    # 实付金额(元)
    actual_pay_money = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[9]/div/div/div[1]/input')
    # 代金券面值(元)
    voucher_money = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[10]/div/div/div/input')
    # 银行成本(元)
    bank_cost = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[11]/div/div/div/input')
    # 每人购买次数
    people_buy_count = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[14]/div/div/div[1]/input')
    # 选择
    button_choice = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[15]/div/div/div/button')
    # 输入商户名称
    input_shop_name = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[15]/div/div/div/div[2]/div/div[2]/form/div/div/div/input')
    # 查询
    button_query_2 = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[15]/div/div/div/div[2]/div/div[2]/form/button')
    # 左侧选择框
    left_choice_box = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[15]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span')
    # 保存
    button_keep = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[15]/div/div/div/div[2]/div/div[3]/div/button[1]')
    # 代金券视图
    voucher_view = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[17]/div/div/div/div/div[1]/div')
    # 券的描述
    voucher_describe = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div/div[18]/div/div/div[1]/div/input')
    # 提交审核
    button_submit = (By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/button[1]')
    # ==================================商户券信息====================================
    # 页面弹窗错误提示
    alert_error_info = (By.XPATH, '/html/body/div[6]/p')
