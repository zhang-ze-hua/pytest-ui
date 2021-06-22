import unittest
import os
import random
import time
from requests import request
from library.myddt import ddt, data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_logging import log
from common.handle_config import conf
from common.handle_headers import HandleHeader
from common.handle_mysql import HandleMysql


@ddt
class RegisterTestCase(unittest.TestCase):
    """简易注册（手机号+推荐人）   FD0003"""
    excel_path = os.path.join(DATA_DIR, conf.get("data", "excel_name"))
    excel = HandleExcel(excel_path, conf.get("data", "sheet_FD0003"))
    cases = excel.read_data()
    hm = HandleMysql()

    def setUp(self):
        """获取短信验证码"""
        url = conf.get("env", "url") + "/FD0002.do"
        self.mobile = self.create_mobile()
        body_data = {"mblNo": self.mobile, "efftTmScdNum": "90", "attr2": "发送短信验证码"}
        body_data = HandleHeader.handle_header(body_data)
        response = request(method="POST", url=url, json=body_data)
        res = response.json()
        self.verfCdOnlyInd = res["body"]["verfCdOnlyInd"]
        time.sleep(3)
        sql = "select opt_no from sms_info where phone_no ={} group by create_time desc limit 1".format(self.mobile)
        sms_code = self.hm.find_one(sql)
        self.sms = sms_code["opt_no"]

    def tearDown(self):
        self.hm.close()

    @data(*cases)
    def test_register(self, case):
        """注册用例"""
        # 1.准备用例数据
        method = case["method"]
        url = case["url"]
        case_data = case["data"]
        if "#mblpnNo#" in case_data:
            case_data = case_data.replace("#mblpnNo#", self.mobile)
        if "#msgVerfCd#" in case_data:
            case_data = case_data.replace("#msgVerfCd#", self.sms)
        if "#verfCdOnlyInd#" in case_data:
            case_data = case_data.replace("#verfCdOnlyInd#", self.verfCdOnlyInd)
        case_data = eval(case_data)
        body_data = HandleHeader.handle_header(case_data)
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 2.获取实际结果
        response = request(method=method, url=url, json=body_data)
        res = response.json()
        print("实际结果：{}".format(res))
        print("预期结果：{}".format(expected))

        # 3.断言
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

    @classmethod
    def create_mobile(cls):
        """生成一个数据库不存在的手机号"""
        # while True:
        mobile_3 = random.choice([133, 135, 137, 138, 139])
        mobile_8 = random.randint(00000000, 99999999)
        mobile = str(mobile_3) + str(mobile_8)
        # 数据库查询生成的手机号是否存在
        # sql = "select * from xxx where mobile = {}".format(mobile)
        # res = cls.hm.find_count(sql)
        # if res == 0:
        return mobile
