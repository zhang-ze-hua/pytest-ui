import unittest
import os
from requests import request
from library.myddt import ddt, data
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from common.handle_headers import HandleHeader
from common.handle_config import conf
from common.handle_data import replace_data


@ddt
class WithdrawalTestCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, conf.get("data", "excel_name")), "FD0060")
    cases = excel.read_data()

    @data(*cases)
    def test_withdrawal(self, case):
        method = case["method"]
        url = conf.get("env", "url") + "/" + case["url"] + ".do"
        case_data = case["data"]
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        case_data = replace_data(WithdrawalTestCase, "user", case_data)
        login_body_data = HandleHeader.handle_header(eval(case_data))

        if case["url"] != "FD0004":
            login_body_data["localHead"]["usrId"] = self.usrId
            login_body_data["localHead"]["tokenId"] = self.tokenId

        response = request(method=method, url=url, json=login_body_data)
        res = response.json()

        if case["url"] == "FD0004":
            setattr(WithdrawalTestCase, "usrId", res["body"]["usrId"])
            setattr(WithdrawalTestCase, "tokenId", res["body"]["tokenId"])
            setattr(WithdrawalTestCase, "acctNo_sequence", res["body"]["acctNo_sequence"])
        if case["url"] == "FD0049":
            setattr(WithdrawalTestCase, "bindAcctNo_sequence", res["body"]["eleAcctBindCrdInfArry"][0]["bindAcctNo_sequence"])

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
