import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.base_page import BasePage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url="http://107.255.1.238:88/#/login")

ele_phone = driver.find_element_by_xpath("/html/body/div/div/div[1]/form/div[1]/div/div/input")
ele_phone.send_keys("17316181600")

ele_pwd = driver.find_element_by_xpath("//input[@placeholder='密码']")
ele_pwd.send_keys("sd888888")

ele_verification_code_image = driver.find_element_by_xpath(
    "/html/body/div/div/div[1]/form/div[3]/div/div[1]/div[2]/img")
src = ele_verification_code_image.get_attribute("src")
uuid = re.findall("uuid=(.*)", src)[0]
verification_code = BasePage.mysql_verification_code(uuid)

ele_verification_code = driver.find_element_by_xpath(
    "/html/body/div/div/div[1]/form/div[3]/div/div[1]/div[1]/div/input")
ele_verification_code.send_keys(verification_code)

ele_get_sms_code = driver.find_element_by_xpath("/html/body/div/div/div[1]/form/div[4]/div/div[1]/div[2]/button/span")
ele_get_sms_code.click()

time.sleep(5)
sms = BasePage.db2_sms_code("17316181600")
ele_sms_code = driver.find_element_by_xpath("/html/body/div/div/div[1]/form/div[4]/div/div[1]/div[1]/div/input")
ele_sms_code.send_keys(sms)

ele_login_button = driver.find_element_by_xpath("//button/*[text()='登录']")
ele_login_button.click()
# ======================================================================================================

ele1 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH, "/html/body/div[1]/aside/div/ul/li[4]/div/span")))
ele1.click()

ele2 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH, "/html/body/div[1]/aside/div/ul/li[4]/ul/li/span")))
ele2.click()

ele3 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="pane-coupon-couponList"]/div/div/div/form/div[5]/div/button[2]')))
ele3.click()
time.sleep(3)
# print(driver.page_source)

print("==================================\n\n\n\n\n")
ele4 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div[1]/div/div/div[1]/input')))
ele4.click()
time.sleep(3)
# print(driver.page_source)

ele5 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')))
ele5.click()

ele6 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/main/div/div/div/form/div[2]/div/button[1]')))
ele6.click()

driver.quit()
