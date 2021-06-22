需要输入密码为例，我写了如下代码，需要传入截图图片路径，还需要输入的密码。前面我已经将各个数字的图片保存在了本地，
并以n0.jpg,n1.jpg,…保存，并和脚本放在一起。我使用python写的脚本，当然你还需要安装opencv,下载路径：
http://opencv.org/releases.html下载后吧build下面的python里面的cv2.pyd文件目录下面的lib\site-packages里面

代码如下

#coding:utf-8
import os
import time
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
def get_pay_keyboard_number_location(im, pwd):
    numbers = set(list(pwd))
    templates = {}
    positions = {}
    nimgpath = ""   #数字图片不在同目录时使用
    for i in numbers:
        templates[i]  = os.path.join(nimgpath, "n{}.jpg".format(i))
 
    start = time.time()
    img_rgb = cv2.imread(im)
 
    for teNum, tepath in templates.items():
        # print(tepath)
        template = cv2.imread(tepath)
        h, w = template.shape[:-1]
 
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .95    # 匹配度参数，1为完全匹配
        loc = np.where(res >= threshold)
        if len(loc) > 0:
            positions[teNum] = zip(*loc[::-1])[0]
        else:
            print("Can not found number: [{}] in image: [{}].".format(tepath, im))
 
    end = time.time()
    print(end-start)
 
    return [positions[n] for n in pwd]
 
if __name__ == "__main__":
    ls = get_pay_keyboard_number_location('keyboard.jpg', '1234567890')
    print(ls)
	
上面的代码实现了获取每个数字的坐标，并以列表进行返回。
拿到坐标后就可以直接的通过appium的tap，如
TouchAction(driver).long_press(x = 180,y = 1400).perform()
进行点击操作