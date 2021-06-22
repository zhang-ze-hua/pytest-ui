import pytest, time
from common.handle_logging import log
from data.case_data import TestRoleManageModify


class TestRoleManageModify:
    @pytest.mark.role_manage_modify_success
    @pytest.mark.parametrize("case", TestRoleManageModify.success_case_data)
    def test_role_manage_modify_pass(self, case, role_manage_fixture):
        pass

    @pytest.mark.role_manage_modify_error
    @pytest.mark.parametrize("case", TestRoleManageModify.error_case_data)
    def test_role_manage_modify_error_case(self, case, role_manage_fixture):
        login_page, role_manage_driver = role_manage_fixture
        role_manage_driver.modify_role(case["old_role_name"], case["new_role_name"], case["new_role_note"])
        result = role_manage_driver.get_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
