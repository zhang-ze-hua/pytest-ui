from selenium.webdriver.common.by import By


class MyLocator:
    """我的页面&&&元素定位"""
    # ==================================右上角按钮===================================
    # 修改密码
    # button_change_pwd = (By.XPATH, "//*[text()='修改密码']")
    button_change_pwd = (By.XPATH, "/html/body/div[1]/nav/div[2]/ul[2]/li[2]/button[1]")
    # 退出
    button_quit = (By.XPATH, "//*[text()='退出']")
    # 首页
    menu_home = (By.XPATH, "//*[text()='首页']")
    # ==================================右上角按钮===================================

    # ==================================左侧菜单栏===================================

    # =====================系统管理====================
    # 系统管理
    menu_system_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[2]")
    # 菜单管理
    menu_menu_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[2]/ul/li[1]")
    # 用户管理
    menu_user_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[2]/ul/li[2]")
    # 角色管理
    menu_role_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[2]/ul/li[3]")
    # 自动化目录
    menu_autotest_manage = (By.XPATH, "//*[text()='自动化目录']")
    # 目录二
    menu_list2_manage = (By.XPATH, "//*[text()='目录二']")
    # 小程序用户管理
    menu_applets_manage = (By.XPATH, "//*[text()='小程序用户管理']")
    # =====================系统管理====================

    # =====================商户管理====================
    # 商户管理
    menu_shop_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[3]")
    # 商户信息列表
    menu_shop_info_list = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[3]/ul/li")
    # =====================商户管理====================

    # =====================代金券管理==================
    # 代金券管理
    menu_voucher_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[4]/div/span")
    # 代金券管理
    menu_voucher_manage_2 = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[4]/ul/li/span")
    # =====================代金券管理==================

    # =====================报表管理====================
    # 报表管理
    menu_form_manage = (By.XPATH, "//*[text()='报表管理']")
    # 订单明细
    menu_order_detailed = (By.XPATH, "//*[text()='订单明细']")
    # 活动奖励明细
    menu_activity_reward_detailed = (By.XPATH, "//*[text()='活动奖励明细']")
    # 交易数据报表
    menu_trade_data_form = (By.XPATH, "//*[text()='交易数据报表']")
    # 清算数据报表
    menu_liquidation_data_form = (By.XPATH, "//*[text()='清算数据报表']")
    # 核销数据报表
    menu_write_off_data_form = (By.XPATH, "//*[text()='核销数据报表']")
    # 异常数据处理
    menu_abnormal_data_handle = (By.XPATH, "//*[text()='异常数据处理']")
    # 平台数据统计
    menu_platform_data_statistics = (By.XPATH, "//*[text()='平台数据统计']")
    # 礼品兑换明细
    menu_gift_exchange_detailed = (By.XPATH, "//*[text()='礼品兑换明细']")
    # 用户积分明细
    menu_user_integral_detailed = (By.XPATH, "//*[text()='用户积分明细']")
    # =====================报表管理====================

    # =====================审核模块====================
    # 审核模块
    menu_examine_module = (By.XPATH, "//*[text()='审核模块']")
    # 商户审核
    menu_shop_examine = (By.XPATH, "//*[text()='商户审核']")
    # 代金券审核
    menu_voucher_examine = (By.XPATH, "//*[text()='代金券审核']")
    # 活动审核
    menu_activity_examine = (By.XPATH, "//*[text()='活动审核']")
    # 积分奖励值审核
    menu_integral_reward_examine = (By.XPATH, "//*[text()='积分奖励值审核']")
    # 话题审核
    menu_topic_of_conversation_examine = (By.XPATH, "//*[text()='话题审核']")
    # 文章审核
    menu_article_examine = (By.XPATH, "//*[text()='文章审核']")
    # 审核礼品
    menu_gift_examine = (By.XPATH, "//*[text()='审核礼品']")
    # =====================审核模块====================

    # =====================广告管理====================
    # 广告管理
    menu_advert_manage = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[7]/div/span")
    # 广告管理
    menu_advert_manage_2 = (By.XPATH, "/html/body/div[1]/aside/div/ul/li[7]/ul/li[1]/span")
    # 文章管理
    menu_article_manage = (By.XPATH, "//*[text()='文章管理']")
    # =====================广告管理====================

    # =====================内容管理====================
    # 内容管理
    menu_content_manage = (By.XPATH, "//*[text()='内容管理']")
    # 活动管理
    menu_activity_manage = (By.XPATH, "//*[text()='活动管理']")
    # 积分奖励值管理
    menu_integral_reward_manage = (By.XPATH, "//*[text()='积分奖励值管理']")
    # 礼品管理
    menu_gift_manage = (By.XPATH, "//*[text()='礼品管理']")
    # 商户管理
    menu_shop_manage_content = (By.XPATH, "//*[text()='商户管理']")
    # 商圈管理
    menu_trade_area_manage = (By.XPATH, "//*[text()='商圈管理']")
    # 代金券管理
    menu_voucher_manage_content = (By.XPATH, "//*[text()='代金券管理']")
    # 菜品管理
    menu_menu_manage_content = (By.XPATH, "//*[text()='菜品管理']")
    # 点评管理
    menu_comment_manage = (By.XPATH, "//*[text()='点评管理']")
    # 留言管理
    menu_leave_message_manage = (By.XPATH, "//*[text()='留言管理']")
    # 话题管理
    menu_topic_of_conversation_manage = (By.XPATH, "//*[text()='话题管理']")
    # =====================内容管理====================
    # ==================================左侧菜单栏===================================
