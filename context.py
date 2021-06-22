列出当前的上下文    driver.current_context
列出所有的上下文    driver.contexts
上下文切换		    driver.switch_to.context()
获取web内容			driver.page_source 
native和webview切换时定位不到，                           desired_caps["recreateChromeDriverSessions"]="true"
定位webview时，打印driver.contexts只有native              desired_caps["chromeOptions"]={"androidProcess": "包名:tools"}

一、识别webview
用定位工具查看页面，发现页面上有些区域无法定位到，这时候可以查看元素属性，如右图它的class属性，上面写着WebView，
那毫无疑问这种页面就是webview了。

二、context
	1.context是上下文，环境
	2.先获取页面contexts环境，获得的是一个list
		print(driver.contexts)               # [NATIVE_APP, WEBVIEW_com.xxxx ]
		NATIVE_APP:这个就是native，也就是原生的
		WEBVIEW_com.xxxx :这个就是webview

三、切换到Webview
	1.要想操作webview上的元素，第一步需要切换环境
	2.切换方法：switch_to.context(参数是webview的context)
		由于第二步已经获取到contexts是一个list对象，取这个list的第二个参数就行，也就是contexts[1]
		contexts = driver.contexts
		driver.switch_to.context(contexts[1])
		driver.current_context #获取当前环境，看是否切换成功

四、切换native
	1.webview上操作完成之后，如果想切换会native环境，有两种方法
		1.driver.switch_to.context("NATIVE_APP")
		2.driver.switch_to.context(contexts[0])
		
		

		

脚本思路：
进入webview后会存在多个handle同Web页签一样，获取所有的handle，然后在遍历所有的handle，通过switch_to_window进行handle切换，
当某个handle可以定位到我们需要定位的元素时，然后我们就可以进行之后的自动化操作了！


from appium import webdriver
import time,os,re
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'Android'    
desired_caps['deviceName'] = 'Android001'   
desired_caps['unicodeKeyboard'] = True      
desired_caps["resetKeyboard"] = True        
desired_caps["newCommandTimeout"]=30       
desired_caps['fullReset'] = 'false'     
desired_caps['appPackage'] = 'com.tencent.mm'           
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'        
desired_caps['recreateChromeDriverSessions'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 10
desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:appbrand0'}
driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub',desired_capabilities = desired_caps)  
time.sleep(2)
driver.implicitly_wait(10)
driver.find_element_by_name('美团外卖').click()
time.sleep(2)
contexts = driver.contexts
print(contexts)
time.sleep(2)
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
print('切换成功')
print driver.current_context
all_handles = driver.window_handles
print(len(all_handles))
for handle in all_handles:
    try:
        driver.switch_to_window(handle)
        print(driver.page_source)
        driver.find_element_by_css_selector('.filter-select.flex-center')    #定位“筛选 ”按钮
        print('定位成功')
        break
    except Exception as e:
        print(e)
driver.find_element_by_css_selector('.filter-select.flex-center').click()
time.sleep(5)
driver.quit()