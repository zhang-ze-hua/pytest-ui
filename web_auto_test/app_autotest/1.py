from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

cap = {
  "platformName": "iOS",
  "platformVersion": "11.4",
  "bundleId": "com.zhongan.insurance",
  "automationName": "XCUITest",
  "udid": "3e8325a7c0***************62bd4a7e",
  "deviceName": "My@Iphone"
}

host = "http://0.0.0.0:4728/wd/hub"
driver = webdriver.Remote(host, cap)
