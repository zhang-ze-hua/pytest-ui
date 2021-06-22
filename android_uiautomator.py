####### resourceId 方式
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")')

####### text 方式
driver.find_element_by_android_uiautomator('new UiSelector().text("%s")')  正常匹配
driver.find_element_by_android_uiautomator(‘new UiSelector().textContains("%s")’) 模糊匹配
driver.find_element_by_android_uiautomator(‘new UiSelector().textStartsWith("%s")’) 开头匹配
driver.find_element_by_android_uiautomator(‘new UiSelector().textMatches("%s")’) 正则表达式

####### description 方式
driver.find_element_by_android_uiautomator('new UiSelector().description("%s")')   使用content_desc的值定位

####### className 方式
driver.find_element_by_android_uiautomator('new UiSelector().className("%s")')

####### index 方式
driver.find_element_by_android_uiautomator('new UiSelector().index("%s")')

####### className + index 方式
driver.find_element_by_android_uiautomator('new UiSelector().className("%s").childSelector(new UiSelector().index("%d"))')

####### 通过父级元素定位子级元素
driver.find_element_by_android_uiautomator(‘new UiSelector().text("%s").fromParent(new UiSelector().text("%s"))‘)        

####### 通过同级元素定位同级元素
driver.find_element_by_android_uiautomator(‘new UiSelector().className("%s").childSelector(new UiSelector().text("%s"))‘)

####### 利用坐标定位
driver.find_element_by_xpath('//*[@bounds="[60,1341][1020,1453]"]')

####### 向下滑动找到目标元素为止
driver.find_elements_by_android_uiautomator(
'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("%s").instance(0))'
)


parent = child.find_element_by_xpath('./..')
children = parent.find_element_by_xpath('./*')




1、获取 content-desc 的方法为 get_attribute("name") ，而且还不能保证返回的一定是 content-desc （content-desc 为空时会返回 text 属性值）
2、get_attribute 方法不是我们在 uiautomatorviewer 看到的所有属性都能获取的（此处的名称均为使用 get_attribute 时使用的属性名称）：
3、ele.size  返回大小，如{'height': 51, 'width': 270}      
   ele.location   返回坐标，如{'x': 810, 'y': 2274}
   
可获取的：
	字符串类型：
		name(返回 content-desc 或 text)
		text(返回 text)
		className(返回 class，只有 API=>18 才能支持)
		resourceId(返回 resource-id，只有 API=>18 才能支持)
		
	布尔类型（如果无特殊说明， get_attribute 里面使用的属性名称和 uiautomatorviewer 里面的一致）：
		enabled
		checkable
		checked
		clickable
		focusable
		focused
		longClickable（返回 long-clickable）
		scrollable
		selected
		displayed（此元素是否在当前界面存在。调用的是 UIObject 的 exists() 方法，详情请看http://developer.android.com/reference/android/support/test/uiautomator/UiObject.html#exists()）
	
	获取不到，但会显示在 uiautomatorviewer 中的属性：
		index
		package
		password
		bounds（可通过 get_position 来获取其中部分内容）
		
		
		
		
		
		
收键盘 driver.hideKeyboard()	  	
		
		
		
		
		
7.1. 从上向下层级定位元素
	方法：先获取元素的父或祖，再往下层级定位元素（祖定位父，父再定位子）

	（1）子或父仅有一个时：
		xpath = "//*[@父属性='父属性值']/子class属性值"
		xpath = "//*[@祖属性='祖属性值']/父class属性值/子class属性值"

	（2）子或父有多个相同的class属性值时添加索引：
		**注**：索引号指相同class属性值下对应的第几个值，从1开始取值，而非从0开始取值。
		xpath = "//*[@父属性='父属性值']/子class属性值[索引号]"
		xpath = "//*[@祖属性='祖属性值']/父class属性值[索引号]/子class属性值[索引号]"

	（3）父或祖属性为class定位的另一种方法：
		xpath = "//祖class属性值/父class属性值[索引号]/子class属性值[索引号]"
		xpath = "//父class属性值/子class属性值[索引号]"
		
	# 通过父ListView定位第二个LinearLayout元素
	xpath_down = driver.find_element_by_xpath("//*[@resource-id='android:id/list']/android.widget.LinearLayout[2]")
	xpath_down_class = driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[2]")
		
		
7.2. 从下向上层级定位元素
	方法：先获取元素的子孙，再往上层级定位元素（子定位父，父再定位祖）

	（1）子定位父
		xpath = "//*[@子属性='子属性值']/.."
		xpath = "//*[@子属性='子属性值']/parent::*"
		xpath = "//*[@子属性='子属性值']/parent::父class属性值"
		
	（2）子定位父再定位祖
		xpath = "//*[@子属性='子属性值']/../.."
		xpath = "//*[@子属性='子属性值']/parent::*/parent::*"
		xpath = "//*[@子属性='子属性值']/parent::父class属性值/parent::父class属性值"

	# 子定位父
	xpath_up1 = driver.find_element_by_xpath("//*[@text='双卡和移动网络']/..")
	xpath_up2 = driver.find_element_by_xpath("//*[@text='双卡和移动网络']/parent::*")
	xpath_up3 = driver.find_element_by_xpath("//*[@text='双卡和移动网络']/parent::android.widget.RelativeLayout")
	# 子定位父，父定位祖
	xpath_up_up = driver.find_element_by_xpath("//*[@text='双卡和移动网络']/../..")

	
7.3. 兄弟之间定位
	方法：先获取元素的父，再通过父获取兄弟元素（子1定位父，父再定位子2）

	xpath = "//*[@属性='属性值']/../兄弟class属性值"
	
	# 先定位父，再往下定位兄弟
	xpath_brother = driver.find_element_by_xpath("//*[@text='蓝牙']/../android.widget.TextView")