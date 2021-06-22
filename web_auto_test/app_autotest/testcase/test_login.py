import pytest
from app_autotest.data.case_data import LoginCase
from app_autotest.locator.my_locator import MyLocator
from app_autotest.common.handle_logging import log


class TestLogin:
    """测试登录"""
    @pytest.mark.login_success
    @pytest.mark.parametrize("case", LoginCase.success_case_data)
    def test_login_pass(self, case, login_fixture):
        """正常登录的用例"""
        login_page = login_fixture
        # 进行登录的操作
        login_page.login(case['mobile'], case['gesture_pwd'])
        # 点击我的
        login_page.click_element(MyLocator.mine_menu, "点击我的")
        # 获取登录之后的用户信息
        res = login_page.get_element_attribute(MyLocator.user_name, "text", "获取用户姓名")
        # 断言用例执行是否通过
        try:
            assert '登录成功' == case['expected']
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

    @pytest.mark.login_error
    @pytest.mark.parametrize('case', LoginCase.error_case_data)
    def test_login_error_case(self, case, login_fixture):
        """异常用例，窗口上有提示"""
        login_page = login_fixture
        # 执行登录操作
        login_page.login(case['mobile'], case['gesture_pwd'])
        # 获取实际提示结果
        result = login_page.get_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

    @pytest.mark.login_error_alert
    @pytest.mark.parametrize('case', LoginCase.error_alert_data)
    def test_login_error_alert(self, case, login_fixture):
        """异常用例，错误信息弹窗提示"""
        login_page = login_fixture
        # 执行登录操作
        login_page.login1(case['mobile'])
        # 获取实际提示结果
        result = login_page.get_alert_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
