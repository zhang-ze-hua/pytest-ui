import pytest
from common.handle_logging import log

log.info("********************开始执行********************")
# pytest.main(['-m login_success'])
# pytest.main(["testcase/test_login.py"])
pytest.main(["testcase/1test_login.py::TestLogin::test_login"])

log.info("********************执行完毕********************\n\n\n")
