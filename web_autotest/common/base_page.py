import os
import re
import time
import pymysql
import ibm_db
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from common.handle_path import ERROR_IMG
from common.handle_logging import log

"""
1、显式等待（元素被加载，元素可见，元素可点击）
2、获取元素的文本
3、获取元素的属性
4、点击元素
5、文本输入
6、窗口拖动
7、滑动到元素可见
9、执行js代码
"""


class BasePage:
    """
    基础定位方法都在这
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    """等待元素可见"""

    def wait_element_visibility(self, locator, img_info, timeout=15, poll_frequency=0.5):
        # 等待元素可见之前,获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待可见超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_screen_image(img_info)
            raise e
        else:
            # 元素等待可见之后,获取当前的时间
            end_time = time.time()
            log.info("元素--{}--等待可见成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    """等待元素可点击"""

    def wait_element_clickable(self, locator, img_info, timeout=15, poll_frequency=0.5):
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            log.error("元素--{}--等待可点击超时".format(locator))
            log.exception(e)
            self.save_screen_image(img_info)
            raise e
        else:
            end_time = time.time()
            log.info("元素--{}--等待可点击成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    """等待元素被加载 """

    def wait_element_presence(self, locator, img_info, timeout=15, poll_frequency=0.5):
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except Exception as e:
            log.error("元素--{}--等待被加载超时".format(locator))
            log.exception(e)
            self.save_screen_image(img_info)
            raise e
        else:
            end_time = time.time()
            log.info("元素--{}--等待被加载成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    """获取元素的文本"""

    def get_element_text(self, locator, img_info):
        start_time = time.time()
        try:
            ele = self.wait_element_visibility(locator, img_info)
            text = ele.text
        except Exception as e:
            log.error("元素--{}--获取文本失败".format(locator))
            log.exception(e)
            self.save_screen_image(img_info)
            raise e
        else:
            end_time = time.time()
            log.info("元素--{}--获取文本成功,等待时间{}秒".format(locator, end_time - start_time))
            return text

    """获取元素的属性"""

    def get_element_attribute(self, locator, attr_name, img_info):
        start_time = time.time()
        try:
            ele = self.wait_element_visibility(locator, img_info)
            attr_value = ele.get_attribute(attr_name)
        except Exception as e:
            log.error("元素--{}--获取属性失败".format(locator))
            log.exception(e)
            self.save_screen_image(img_info)
            raise e
        else:
            end_time = time.time()
            log.info("元素--{}--获取属性成功,等待时间{}秒".format(locator, end_time - start_time))
            return attr_value

    """点击元素"""

    def click_element(self, locator, img_info):
        start_time = time.time()
        try:
            ele = self.wait_element_clickable(locator, img_info)
            ele.click()
        except Exception as e:
            log.error("元素--{}--点击失败".format(locator))
            log.exception(e)
            self.save_screen_image(img_info)
            raise e
        else:
            end_time = time.time()
            log.info("元素--{}--点击成功,等待时间{}秒".format(locator, end_time - start_time))

    """文本输入"""

    def input_text(self, locator, text_value, img_info):
        start_time = time.time()
        try:
            ele = self.wait_element_visibility(locator, img_info)
            ele.clear()
            ele.send_keys(text_value)
        except Exception as e:
            log.error("元素--{}--输入--{}-失败".format(locator, text_value))
            log.exception(e)
            self.save_screen_image(img_info)
            raise e
        else:
            end_time = time.time()
            log.info("元素--{}--输入--{}--成功,等待时间{}秒".format(locator, text_value, end_time - start_time))

    """对当前页面进行截图"""

    def save_screen_image(self, img_info):
        start_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        filename = '{}_{}.png'.format(start_time, img_info)
        file_path = os.path.join(ERROR_IMG, filename)
        self.driver.save_screenshot(file_path)
        log.info("错误页面截图成功，保存的路径是:{}".format(file_path))

    # def get_error_info(self, locator, img_info):
    #     """获取显示在页面上的提示信息"""
    #     return self.get_element_text(locator, img_info)
    #
    # def get_alert_error_info(self, locator, img_info):
    #     """获取显示在弹窗上的提示信息"""
    #     ele = self.wait_element_presence(locator, img_info)
    #     return ele.text

    """手势密码"""

    def gesture_password(self, locator, pwd, img_info, ):
        ele = self.wait_element_visibility(locator, img_info)
        # 定位手势登录控件
        start_location = ele.location
        ele_width = ele.size["width"]
        ele_height = ele.size["height"]

        # 计算每个点位的坐标，并标记组装
        dic = dict()
        dic["1"] = (start_location["x"] + int(1 / 6 * ele_width), start_location["y"] + int(1 / 6 * ele_height))
        dic["2"] = (start_location["x"] + int(3 / 6 * ele_width), start_location["y"] + int(1 / 6 * ele_height))
        dic["3"] = (start_location["x"] + int(5 / 6 * ele_width), start_location["y"] + int(1 / 6 * ele_height))
        dic["4"] = (start_location["x"] + int(1 / 6 * ele_width), start_location["y"] + int(3 / 6 * ele_height))
        dic["5"] = (start_location["x"] + int(3 / 6 * ele_width), start_location["y"] + int(3 / 6 * ele_height))
        dic["6"] = (start_location["x"] + int(5 / 6 * ele_width), start_location["y"] + int(3 / 6 * ele_height))
        dic["7"] = (start_location["x"] + int(1 / 6 * ele_width), start_location["y"] + int(5 / 6 * ele_height))
        dic["8"] = (start_location["x"] + int(3 / 6 * ele_width), start_location["y"] + int(5 / 6 * ele_height))
        dic["9"] = (start_location["x"] + int(5 / 6 * ele_width), start_location["y"] + int(5 / 6 * ele_height))

        # 根据密码拆分，进行定位滑动
        action = TouchAction(self.driver)
        index = 0
        for i in pwd:
            if index == 0:
                action.press(x=dic["%s" % i][0], y=dic["%s" % i][1]).wait(100)
            else:
                action.move_to(x=dic["%s" % i][0], y=dic["%s" % i][1]).wait(100)
            index += 1
        action.release().perform()

    """连接数据库，查询图片验证码"""

    @staticmethod
    def mysql_verification_code(uuid):
        conn = pymysql.connect(host="107.255.1.242",
                               user="mysqladmin",
                               password="Abcd1234",
                               database="foodmap1030",
                               port=3306)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            sql = "select code from SYS_CAPTCHA where uuid= %s"
            cur.execute(sql, uuid)
            res_one = cur.fetchone()
            return res_one["code"]
        except pymysql.err.ProgrammingError as e:
            raise e
        cur.close()
        conn.close()

    """连接数据库，查询短信验证码"""

    @staticmethod
    def db2_sms_code(mobile):
        local_time = time.strftime("%Y%m%d", time.localtime())
        connstr = "DATABASE=isfstdb;HOSTNAME=172.16.249.14;PORT=60000;PROTOCOL=TCPIP;UID=isfstqry;PWD=isfstqry123;"
        conn = ibm_db.connect(connstr, "", "")
        try:
            sql = "select call_content from isfst.t_iss_call_task where mobile='{}' and OTH_RESPOND_DATE='{}' " \
                  "order by abs(iss_seq) desc".format(mobile, local_time)
            stmt = ibm_db.exec_immediate(conn, sql)
            result = ibm_db.fetch_both(stmt)
            if result:
                sms_code = result["CALL_CONTENT"]
                sms = re.findall("\d{6}", sms_code)
                return sms[0]
            else:
                return None
        except Exception as e:
            raise e
        ibm_db.close(stmt)
        ibm_db.close(conn)
