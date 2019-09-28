# -*-encoding:utf-8-*-  
import pytesseract  
from PIL import Image  
from PIL import ImageFilter  
from PIL import ImageFont  
from PIL import ImageDraw  
import numpy as np  
from PIL import Image  
  
import cv2  
  
'''  
def main():  
    img = cv2.imread('/home/ts/Pictures/t1.png', 0)  
    template = cv2.imread('/home/ts/Pictures/t2.png', 0)  
    h, w = template.shape[:2]  # rows->h, cols->w  
    print("h = " ,h )  
    print("w = ", w)  
  
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)  
  
 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  
    print("min_val = ", min_val)  
    print("max_val = ", max_val)#最大匹配值  
    print("min_loc = ", min_loc)  
    print("max_loc = ", max_loc)#最大左上角坐标  
  
    left_top = max_loc  # 左上角  
    right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角  
    cv2.rectangle(img, left_top, right_bottom, 255, 2)  # 画出矩形位置  
  
    cv2.imshow('img', img)  
    cv2.waitKey(0)  
  
if __name__ == '__main__':  
    main()  
'''  


# -*-encoding:utf-8-*-  
import pytesseract  
from PIL import Image  
from PIL import ImageFilter  
from PIL import ImageFont  
from PIL import ImageDraw  
import numpy as np  
from PIL import Image  
  
import cv2  
  
  
def main():  
    # 使用模板匹配在图像中寻找物体  
    # OpenCV函数：cv2.matchTemplate(), cv2.minMaxLoc()  
    # 模板匹配就是用来在大图中找小图，也就是说在一副图像中寻找另外一张模板图像的位置  
  
    #  =================================匹配多个物体,模板匹配  
    # 1.读入原图和模板  
    img_rgb = cv2.imread('/home/ts/Pictures/t3.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('/home/ts/Pictures/t4.png', 0)
    h, w = template.shape[:2]
    # 2.标准相关模板匹配  
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    # 3.这边是Python/Numpy的知识，后面解释  
    loc = np.where(res >= threshold)# 匹配程度大于%80的坐标y,x,loc是先y坐标再x坐标

    for pt in zip(*loc[::-1]):# *号表示可选参数,，所以用loc[::-1]翻转一下，然后再用zip函数拼接在一起。
        right_bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img_rgb, pt, right_bottom, (255, 0, 0), 2)
        print("*"*100)

    cv2.imshow('img_rgb', img_rgb)
    cv2.waitKey(0)

if __name__ == '__main__':  
    main()  

