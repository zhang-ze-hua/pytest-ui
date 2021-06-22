import unittest
import os
from requests import request
from library.myddt import ddt, data
from common.handle_config import conf
from common.handle_headers import HandleHeader
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_logging import log


@ddt
class RechargeTestCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, conf.get("data", "excel_name")), "FD0055")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 登录，获取tokenId、usrId、acctNo_sequence
        login_url = conf.get("env", "url") + "/FD0004.do"
        login_body_data = {
            "qryType": "01",
            "mblpnNo": conf.get("user", "mblpnNo"),
            "bsnType": "04",
            "eqmtNo": conf.get("user", "eqmtNo"),
            "ipAdr": conf.get("user", "ipAdr"),
            "macAdr": conf.get("user", "macAdr"),
            "lgnPwd": conf.get("user", "lgnPwd"),
            "serverRndmNo": conf.get("user", "serverRndmNo"),
            "appRndmNo": conf.get("user", "appRndmNo")
        }
        login_body_data = HandleHeader.handle_header(login_body_data)
        login_response = request(method="POST", url=login_url, json=login_body_data)
        login_res = login_response.json()
        cls.usrId = login_res["body"]["usrId"]
        cls.tokenId = login_res["body"]["tokenId"]
        cls.acctNo_sequence = login_res["body"]["acctNo_sequence"]

        # 查询，获取bindAcctNo_sequence
        query_url = conf.get("env", "url") + "/FD0049.do"
        query_body_data = {
            "cardno": cls.acctNo_sequence,
            "usrId": cls.usrId,
            "bindAcctType": "1",
            "txnType": "00",
            "qryType": "01",
            "mblpnNo": conf.get("user", "mblpnNo")
        }
        query_body_data = HandleHeader.handle_header(query_body_data)
        query_body_data["localHead"]["usrId"] = cls.usrId
        query_body_data["localHead"]["tokenId"] = cls.tokenId
        query_response = request(method="POST", url=query_url, json=query_body_data)
        query_res = query_response.json()
        cls.bindAcctNo_sequence = query_res["body"]["eleAcctBindCrdInfArry"][0]["bindAcctNo_sequence"]

    @data(*cases)
    def test_recharge(self, case):
        method = case["method"]
        url = case["url"]
        case_data = case["data"]
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        if "#pymtAcctNo#" in case_data:
            case_data = case_data.replace("#pymtAcctNo#", self.bindAcctNo_sequence)
        if "#clctnAcctNo#" in case_data:
            case_data = case_data.replace("#clctnAcctNo#", self.acctNo_sequence)
        if "#usrId#" in case_data:
            case_data = case_data.replace("#usrId#", self.usrId)
        body_data = HandleHeader.handle_header(eval(case_data))
        body_data["localHead"]["usrId"] = self.usrId
        body_data["localHead"]["tokenId"] = self.tokenId

        # 2.获取实际结果
        response = request(method=method, url=url, json=body_data)
        res = response.json()
        print("实际结果：{}".format(res))
        print("预期结果：{}".format(expected))

        # 3.断言
        try:
            self.assertEqual(expected["errorCode"], res["sysHead"]["errorCode"])
            self.assertEqual(expected["errorMsg"], res["sysHead"]["errorMsg"])
            # 查询数据库，充值前后金额对比

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
