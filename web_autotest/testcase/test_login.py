import pytest
import os
import time
from locator.my_locator import MyLocator
from common.handle_logging import log
from common.handle_excel import HandleExcel
from common.handle_config import conf
from common.handle_path import DATA_DIR


class TestLogin:
    """测试登录"""
    excel = HandleExcel(os.path.join(DATA_DIR, conf.get("excel", "filename")), "登录")
    success_case_data, error_case_data, error_alert_data, column = excel.case_classify()

    @pytest.mark.login_success
    @pytest.mark.parametrize("case", success_case_data)
    def test_login_pass(self, case, login_fixture):
        """正常登录的用例"""
        login_page = login_fixture
        data = eval(case["data"])
        case_id = case["case_id"]
        title = case["title"]
        expected = case["expected"]
        # 登录操作
        login_page.login(data['mobile'], data['pwd'])
        # 获取登录之后的用户信息
        res = login_page.get_element_attribute(MyLocator.button_quit, "text", "获取用户姓名")
        # 断言用例执行是否通过
        try:
            assert '登录成功' == expected
        except AssertionError as e:
            log.error("用例--{}--执行不通过".format(title))
            log.debug("实际结果：{}".format('登录成功'))
            log.debug("预期结果：{}".format(expected))
            log.exception(e)
            self.excel.write_data(row=case_id + 1, column=self.column, value="不通过")
            raise e
        else:
            log.info("用例--{}--执行通过".format(title))
            self.excel.write_data(row=case_id + 1, column=self.column, value="通过")

    @pytest.mark.login_error
    @pytest.mark.parametrize('case', error_case_data)
    def test_login_error_case(self, case, login_fixture):
        """异常用例，窗口上有提示"""
        login_page = login_fixture
        data = eval(case["data"])
        case_id = case["case_id"]
        title = case["title"]
        expected = case["expected"]
        # 执行登录操作
        login_page.login(data['mobile'], data['pwd'])
        # 获取实际提示结果
        result = login_page.get_error_info()
        # 断言
        try:
            assert expected == result
        except AssertionError as e:
            log.error("用例--{}--执行不通过".format(title))
            log.debug("实际结果：{}".format(result))
            log.debug("预期结果：{}".format(expected))
            log.exception(e)
            self.excel.write_data(row=case_id + 1, column=self.column, value="不通过")
            raise e
        else:
            log.info("用例--{}--执行通过".format(title))
            self.excel.write_data(row=case_id + 1, column=self.column, value="通过")

    @pytest.mark.login_error_alert
    @pytest.mark.parametrize('case', error_alert_data)
    def test_login_error_alert(self, case, login_fixture):
        """异常用例，错误信息弹窗提示"""
        login_page = login_fixture
        data = eval(case["data"])
        case_id = case["case_id"]
        title = case["title"]
        expected = case["expected"]
        # 执行登录操作
        login_page.login2(data['mobile'], data['pwd'])
        time.sleep(1)
        # 获取实际提示结果
        result = login_page.get_alert_error_info()
        # 断言
        try:
            assert expected == result
        except AssertionError as e:
            log.error("用例--{}--执行不通过".format(title))
            log.debug("实际结果：{}".format(result))
            log.debug("预期结果：{}".format(expected))
            log.exception(e)
            self.excel.write_data(row=case_id + 1, column=self.column, value="不通过")
            raise e
        else:
            log.info("用例--{}--执行通过".format(title))
            self.excel.write_data(row=case_id + 1, column=self.column, value="通过")
