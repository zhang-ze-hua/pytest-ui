import unittest
import os
import decimal
from requests import request
from library.myddt import ddt, data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_config import conf
from common.handle_data import replace_data
from common.handle_headers import HandleHeader
from common.handle_logging import log


@ddt
class BuyETestCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, conf.get("data", "excel_name")), "FD0125")
    cases = excel.read_data()

    @data(*cases)
    def test_buy_e(self, case):
        title = case["title"]
        method = case["method"]
        interface = case["url"]
        url = conf.get("env", "url") + "/" + case["url"] + ".do"
        data = case["data"]
        expected = eval(case["expected"])
        case_id = case["case_id "]
        data = replace_data(BuyETestCase, "user", data)

        # 请求
        body_data = HandleHeader.handle_header(eval(data))
        if interface != "FD0004":
            body_data["localHead"]["usrId"] = BuyETestCase.usrId
            body_data["localHead"]["tokenId"] = BuyETestCase.tokenId

        print("{}---请求的数据：{}".format(interface, body_data))
        log.debug("{}---请求的数据：{}".format(interface, body_data))

        response = request(method=method, url=url, json=body_data)
        res = response.json()

        # 响应
        if interface == "FD0004":
            setattr(BuyETestCase, "usrId", res["body"]["usrId"])
            setattr(BuyETestCase, "tokenId", res["body"]["tokenId"])
            setattr(BuyETestCase, "acctNo_sequence", res["body"]["acctNo_sequence"])
        if interface == "FD0257":
            setattr(BuyETestCase, "usrId", res["body"]["depositList"][0]["usrId"])
            setattr(BuyETestCase, "aviPdId", res["body"]["depositList"][0]["aviPdId"])
            setattr(BuyETestCase, "aviPdNm", res["body"]["depositList"][0]["aviPdNm"])
            setattr(BuyETestCase, "basePdId", res["body"]["depositList"][0]["basePdId"])
            setattr(BuyETestCase, "depTerm", res["body"]["depositList"][0]["depTerm"])
            setattr(BuyETestCase, "intRate", res["body"]["depositList"][0]["intRate"])
        if case_id == "2":
            setattr(BuyETestCase, "money1", res["body"]["avlblBal"])
        if case_id == "6":
            setattr(BuyETestCase, "money2", res["body"]["avlblBal"])

        print("{}---实际结果：{}".format(interface, res))
        print("{}---预期结果：{}".format(interface, expected))
        log.debug("{}---实际结果：{}".format(interface, res))
        log.debug("{}---预期结果：{}".format(interface, expected))

        try:
            self.assertEqual(expected["errorCode"], res["sysHead"]["errorCode"])
            self.assertEqual(expected["errorMsg"], res["sysHead"]["errorMsg"])
            if case_id == "6":
                self.assertEqual(decimal.Decimal(BuyETestCase.money1) - decimal.Decimal(BuyETestCase.money2), 100)
        except AssertionError as e:
            log.error("用例--{}--执行不通过".format(title))
            log.exception(e)
            self.excel.write_data(row=case_id + 1, column=7, value="不通过")
            raise e
        else:
            log.error("用例--{}--执行通过".format(title))
            self.excel.write_data(row=case_id + 1, column=7, value="通过")
