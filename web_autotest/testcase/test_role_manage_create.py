import pytest
from common.handle_logging import log
from data.case_data import TestRoleManageCreate


class TestRoleManageCreate:
    @pytest.mark.role_manage_create_success
    @pytest.mark.parametrize("case", TestRoleManageCreate.success_case_data)
    def test_role_manage_create_pass(self, case, role_manage_fixture):
        pass

    @pytest.mark.role_manage_create_error
    @pytest.mark.parametrize("case", TestRoleManageCreate.error_case_data)
    def test_role_manage_create_error_case(self, case, role_manage_fixture):
        login_page, role_manage_driver = role_manage_fixture
        role_manage_driver.create_role(case["role_name"], case["role_note"])
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
