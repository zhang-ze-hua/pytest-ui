import os

# 获取项目所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例数据所在的目录路径
DATA_DIR = os.path.join(BASE_DIR, "data")

# 配置文件所在的目录路径
CONF_DIR = os.path.join(BASE_DIR, "conf")

# 测试报告所在的目录路径
REPORT_DIR = os.path.join(BASE_DIR, "result/reports")

# 日志文件所在的目录路径
LOG_DIR = os.path.join(BASE_DIR, "result/logs")

# 测试用例所在的目录路径
TESTCASE_DIR = os.path.join(BASE_DIR, "testcase")
