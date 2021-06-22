class LoginCase:
    """登录功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"mobile": "17316181600", "pwd": "sd888888", "expected": "登录成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中
    error_alert_data = [
        {'mobile': "", "pwd": "sd888888", "expected": "请输入正确的手机号"},
    ]
    # 异常的用例数据，错误提示在页面上
    error_case_data = [
        {'mobile': "17316181600", "pwd": "", "expected": "密码不能为空"},
    ]


class TestPwdChange:
    """修改密码功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"old_pwd": "sd888888", "new_pwd": "sd666666", "confirm_pwd": "sd666666", "expected": "修改成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中
    error_alert_data = [
        {"old_pwd": "sd111111", "new_pwd": "sd888888", "confirm_pwd": "sd666666", "expected": "原密码不正确"},
    ]
    # 异常的用例数据，错误提示在页面上
    error_case_data = [
        {"old_pwd": "", "new_pwd": "sd666666", "confirm_pwd": "sd666666", "expected": "原密码不能为空"},
    ]


class TestRoleManageCreate:
    """角色管理--新建功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"role_name": "自动化123", "role_note": "自动化123", "expected": "新增成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中

    # 异常的用例数据，错误提示在页面上
    error_case_data = [
        {"role_name": "", "role_note": "自动化123", "expected": "角色名称不能为空"},
    ]


class TestRoleManageModify:
    """角色管理--修改功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"old_role_name": "自动化美食地图", "new_role_name": "自动化123", "new_role_note": "自动化123", "expected": "新增成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中

    # 异常的用例数据，错误提示在页面上
    error_case_data = [
        {"old_role_name": "自动化美食地图", "new_role_name": "", "new_role_note": "自动化美食地图", "expected": "角色名称不能为空"},
    ]


class TestShopManageCreate:
    """角色管理--新建功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"role_name": "自动化123", "role_note": "自动化123", "expected": "新增成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中

    # 异常的用例数据，错误提示在页面上
    error_case_data = [
        {"role_name": "", "role_note": "自动化123", "expected": "角色名称不能为空"},
    ]


class TestShopManageDelete:
    """商户管理--删除功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"shop_name": "测试67301", "expected": "删除成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中

    # 异常的用例数据，错误提示在页面上
    error_case_data = [
        {"shop_name": "测试67301", "expected": "删除失败"},
    ]


class VoucherManageCase:
    """商户管理--删除功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {"voucher_name": "商户券30", "shop_name": "四季小味馆", "expected": "新增成功"},
    ]
    # 异常的用例数据，错误提示在弹窗中
    error_alert_data = [
        {"voucher_name": "商户券30", "shop_name": "四季小味馆", "expected": "代金券视图不能为空"},
    ]
    # 异常的用例数据，错误提示在页面上
