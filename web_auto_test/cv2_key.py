import os
import cv2
from PIL import Image

def safeKeyBordClick_android(password):
    path = "C:\Jettech\JettechAgent1.6.0\conf\safeKeyBordTemplate\\tempimage"
    imagePath = "C:\Jettech\JettechAgent1.6.0\conf\safeKeyBordTemplate\\tempimage\\shouyin.png"
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        mainIm = Image.open(imagePath)
        mainW, mainH = mainIm.size
        im_ss = mainIm.resize((360, 640))
        im_ss.save(imagePath)
        beishuX = mainW / 360
        beishuY = mainH / 640
    except Exception:
        print("----异常")
    li_num = []
    for i in password:
        li_num.append(i)
    li_num.append("finish")
    for num in li_num:
        img = cv2.imread(imagePath)
        template = cv2.imread("C:\Jettech\JettechAgent1.6.0\conf\safeKeyBordTemplate\%s.png" % num)
        height, width = template.shape[:2]
        result = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
        cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        strmin_val = str(min_val)
        cv2.rectangle(img,min_loc,(min_loc[0]+width, min_loc[1]+height),(0,0,225))
        cv2.imshow(strmin_val,img)
        cv2.waitKey()

        top_left = [(min_loc[0] + 0.3 * width) * beishuX, (min_loc[1] + 0.2 * height) * beishuY]
        if top_left[0] >= 1080:
            top_left[0] = 1079.9
        if top_left[1] >= 2211:
            top_left[1] = 2210.9
        top_left = tuple(top_left)
        print(top_left)

safeKeyBordClick_android("8")