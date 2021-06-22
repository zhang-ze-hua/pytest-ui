import pytest
from common.handle_logging import log
from data.case_data import VoucherManageCase


class TestVoucherManageCreate:
    @pytest.mark.voucher_manage_create_error
    @pytest.mark.parametrize("case", VoucherManageCase.error_alert_data)
    def test_voucher_manage_create_error(self, case, voucher_manage_fixture):
        login_page, voucher_manage_driver = voucher_manage_fixture
        voucher_manage_driver.create_shop_voucher(case["voucher_name"], case["shop_name"])
        result = voucher_manage_driver.get_alert_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
