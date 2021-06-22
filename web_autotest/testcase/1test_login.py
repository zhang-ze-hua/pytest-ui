import pytest
import os
import time
from locator.my_locator import MyLocator
from common.handle_logging import log
from common.handle_excel import HandleExcel
from common.handle_config import conf
from common.handle_path import DATA_DIR
from common.handle_assert import handle_assert


class TestLogin:
    """测试登录"""
    excel = HandleExcel(os.path.join(DATA_DIR, conf.get("excel", "filename")), "登录")
    cases_data, column = excel.read_data()

    @pytest.mark.parametrize("case", cases_data)
    def test_login(self, case, login_fixture):
        # 准备数据
        login_page = login_fixture
        case_id = case["case_id"]
        case_type = case["type"]
        title = case["title"]
        data = eval(case["data"])
        expected = case["expected"]

        # 登录操作，获取实际结果
        result = None
        if case_type == conf.get("excel", "success_case"):
            login_page.login(data['mobile'], data['pwd'])
            res = login_page.get_element_attribute(MyLocator.button_quit, "text", "获取用户姓名")
            result = "登录成功"
        elif case_type == conf.get("excel", "error_page_case"):
            login_page.login(data['mobile'], data['pwd'])
            result = login_page.get_error_info()
        elif case_type == conf.get("excel", "error_alert_case"):
            login_page.login2(data['mobile'], data['pwd'])
            time.sleep(1)
            result = login_page.get_alert_error_info()

        # 断言
        handle_assert(expected, result, case_type, title, case_id, self.column, self.excel)
