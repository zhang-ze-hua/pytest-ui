import os
import re
from appium import webdriver
from app_autotest.common.handle_logging import log
from app_autotest.common.handle_config import conf


class HandleDriver:
    # 获取driver的配置信息
    @staticmethod
    def get_driver_info():
        try:
            # 获取deviceName
            device_id = os.popen('adb devices').readlines()
            device_name = re.findall(r'^\w*\b', device_id[1])[0]

            # 获取platformVersion
            device_version = os.popen('adb shell getprop ro.build.version.release').readlines()
            platform_version = re.findall(r'^\w*\b', device_version[0])[0]

            # 获取appPackage/appActivity
            app_package_info = os.popen("aapt dump badging " + conf.get("app_info", "app_path")).read()
            app_package = re.findall(r"package: name=\'(.*?)\'", app_package_info)[0]
            app_activity = re.findall(r"launchable-activity: name=\'(.*?)\'", app_package_info)[0]

            driver_info = [device_name, platform_version, app_package, app_activity]

        except Exception as e:
            log.error("获取driver的配置信息失败")
            log.exception(e)
            raise e

        else:
            return driver_info

    # 创建driver
    @staticmethod
    def create_driver(driver_info):
        driver_info = driver_info
        try:
            desired_caps = dict()
            # 基本配置信息
            desired_caps["deviceName"] = driver_info[0]
            desired_caps["platformName"] = conf.get("driver_info", "mobile_type")
            desired_caps["platformVersion"] = driver_info[1]
            desired_caps["appPackage"] = driver_info[2]
            desired_caps["appActivity"] = driver_info[3]
            # 不重置信息
            desired_caps["noSign"] = "true"
            desired_caps["noReset"] = "true"
            # 启用UNICODE输入，可以输入中文
            desired_caps["unicodeKeyboard"] = True
            desired_caps["resetKeyboard"] = True
            desired_caps["includeNonModalElements"] = True
            # 设置开启webview
            desired_caps["startIWDP"] = True
            # 设置session
            desired_caps["newCommandTimeout"] = 4000
            desired_caps["automationName"] = "uiautomator2"

            port = conf.get("driver_info", "port")
            driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub" % port, desired_caps)

        except Exception as e:
            log.error("创建driver失败")
            log.exception(e)
            raise e

        else:
            return driver


driver = HandleDriver.create_driver(HandleDriver.get_driver_info())
