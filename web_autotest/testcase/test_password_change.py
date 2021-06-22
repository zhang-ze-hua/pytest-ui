import pytest
from data.case_data import TestPwdChange
from common.handle_logging import log


class TestChangePwd:

    @pytest.mark.pwd_change_success
    @pytest.mark.parametrize("case", TestPwdChange.success_case_data)
    def test_pwd_change_pass(self, case, pwd_change_fixture):
        login_page, pwd_change_driver = pwd_change_fixture
        pwd_change_driver.input_pwd(case["old_pwd"], case["new_pwd"], case["confirm_pwd"])
        result = pwd_change_driver.get_alert_pass_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

    @pytest.mark.pwd_change_error
    @pytest.mark.parametrize("case", TestPwdChange.error_case_data)
    def test_pwd_change_error_case(self, case, pwd_change_fixture):
        login_page, pwd_change_driver = pwd_change_fixture
        pwd_change_driver.input_pwd(case["old_pwd"], case["new_pwd"], case["confirm_pwd"])
        result = pwd_change_driver.get_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

    @pytest.mark.pwd_change_error_alert
    @pytest.mark.parametrize('case', TestPwdChange.error_alert_data)
    def test_pwd_change_error_alert(self, case, pwd_change_fixture):
        """异常用例，错误信息弹窗提示"""
        login_page, pwd_change_driver = pwd_change_fixture
        pwd_change_driver.input_pwd(case["old_pwd"], case["new_pwd"], case["confirm_pwd"])
        result = pwd_change_driver.get_alert_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
