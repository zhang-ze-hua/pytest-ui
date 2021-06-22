一、Appium API -- TouchAction
Appium的辅助类，主要针对手势操作，比如滑动、长按、拖动等。

1、按压控件
方法：press()
开始按压一个元素或坐标点（x,y）。通过手指按压手机屏幕的某个位置。
举例：TouchAction(driver).press(x=0,y=308).release().perform()

release() 结束的行动取消屏幕上的指针。
Perform() 执行的操作发送到服务器的命令操作。
release在前，perform在后，顺序不对有影响

2、长按控件
方法：longPress()
开始按压一个元素或坐标点（x,y）。相比press()方法，longPress()多了一个入参，既然长按，得有按的时间吧。
duration以毫秒为单位。1000表示按一秒钟。其用法与press()方法相同。
举例：TouchAction(driver).longPress(x=1 ,y=302,duration=1000).release().perform()

3、移动
方法：moveTo()
将指针（光标）从过去指向指定的元素或点。
举例：TouchAction(driver).moveTo(x=0,y=308).release().perform()

4、暂停
方法：wait()
暂停脚本的执行，单位为毫秒。
举例：TouchAction(driver).wait(1000)



三、兼容不同分辨率
直接用坐标点找会有一些问题，比如手机屏幕大小不同，找点的位置可能会有偏差，如何解决呢？
由下图可见，先获取第一个触摸点的坐标location及size。分别定义为start_height、start_width、start_x、start_y
（其中start_x、start_y为触摸点左上角的坐标）；即可计算出第一个触摸点的中心点坐标分别为：start_x + start_width/2,
 start_y + start_height/2,然后在计算出第二个触摸点的中心点大致坐标为：start_x+start_width*2, y=start_y+start_height*2

其他坐标均可按照此计算方式，详情见具体例子。
from time import sleep
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
sleep(3)
action = TouchAction(driver)
# action.press(x=98, y=321).wait(100).move_to(x=208, y=321).wait(100).move_to(x=206, y=432).wait(100).move_to(x=98, y=432).perform().release()
start = driver.find_element_by_xpath('//*')
start_height = start.size['height']
start_width = start.size['width']
start_x = start.location['x']
start_y = start.location['y']
begin_x = start_x + start_width/2
begin_y = start_y + start_height/2

action.press(x=start_x, y=start_y).wait(100)
.move_to(x=start_x+start_width*2, y=begin_y).wait(100)
.move_to(x=start_x+start_width*2, y=start_y+start_height*2).wait(100)
.move_to(x=begin_x,y=start_y+start_height*2)
.release().perform()