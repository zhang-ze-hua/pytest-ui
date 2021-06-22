import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner
from BeautifulReport import BeautifulReport
from common.handle_path import TESTCASE_DIR, REPORT_DIR
from common.handle_logging import log

log.info("========================测试开始========================")

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(TESTCASE_DIR))

# bf = BeautifulReport(suite)
# bf.report("登录测试报告", "login.html", REPORT_DIR)

fp = open(os.path.join(REPORT_DIR, "register.html"), "wb")
runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行结果", tester="xx")
runner.run(suite)
fp.close()

log.info("========================测试结束========================\n\n")
