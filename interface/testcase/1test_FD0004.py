import unittest
import os
from requests import request
from library.myddt import ddt, data
from common.handle_logging import log
from common.handle_config import conf
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_headers import HandleHeader


@ddt
class LoginTestCase(unittest.TestCase):
    path = os.path.join(DATA_DIR, conf.get("data", "excel_name"))
    excel = HandleExcel(path, conf.get("data", "sheet_FD0004"))
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        # 准备数据
        method = case["method"]
        url = case["url"]
        data = eval(case["data"])
        body_data = HandleHeader.handle_header(data)
        expected = eval(case["expected"])
        # headers = eval(conf.get("env", "headers"))
        row = case["case_id"] + 1
        # 实际结果
        response = request(method=method, url=url, json=body_data)
        res = response.json()
        print("实际结果：{}".format(res))
        print("预期结果：{}".format(expected))
        # 断言
        try:
            self.assertEqual(expected["errorCode"], res["sysHead"]["errorCode"])
            self.assertEqual(expected["errorMsg"], res["sysHead"]["errorMsg"])
        except AssertionError as e:
            log.error("用例--{}--执行不通过".format(case["title"]))
            log.debug("实际结果：{}".format(res))
            log.debug("预期结果：{}".format(expected))
            log.exception(e)
            self.excel.write_data(row=row, column=7, value="不通过")
            raise e
        else:
            log.info("用例--{}--执行通过".format(case["title"]))
            self.excel.write_data(row=row, column=7, value="通过")
