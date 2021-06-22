import pytest
from common.handle_logging import log
from data.case_data import TestShopManageDelete


class TestShopManageDelete:
    @pytest.mark.shop_manage_delete_success
    @pytest.mark.parametrize("case", TestShopManageDelete.success_case_data)
    def test_shop_manage_delete_pass(self, case, shop_manage_fixture):
        login_page, shop_manage_driver = shop_manage_fixture
        shop_manage_driver.delete_shop(case["shop_name"])
        result = shop_manage_driver.get_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

