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
    print("max_val = ", max_val)#���ƥ��ֵ  
    print("min_loc = ", min_loc)  
    print("max_loc = ", max_loc)#������Ͻ�����  
  
    left_top = max_loc  # ���Ͻ�  
    right_bottom = (left_top[0] + w, left_top[1] + h)  # ���½�  
    cv2.rectangle(img, left_top, right_bottom, 255, 2)  # ��������λ��  
  
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
    # ʹ��ģ��ƥ����ͼ����Ѱ������  
    # OpenCV������cv2.matchTemplate(), cv2.minMaxLoc()  
    # ģ��ƥ����������ڴ�ͼ����Сͼ��Ҳ����˵��һ��ͼ����Ѱ������һ��ģ��ͼ���λ��  
  
    #  =================================ƥ��������,ģ��ƥ��  
    # 1.����ԭͼ��ģ��  
    img_rgb = cv2.imread('/home/ts/Pictures/t3.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('/home/ts/Pictures/t4.png', 0)
    h, w = template.shape[:2]
    # 2.��׼���ģ��ƥ��  
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    # 3.�����Python/Numpy��֪ʶ���������  
    loc = np.where(res >= threshold)# ƥ��̶ȴ���%80������y,x,loc����y������x����

    for pt in zip(*loc[::-1]):# *�ű�ʾ��ѡ����,��������loc[::-1]��תһ�£�Ȼ������zip����ƴ����һ��
        right_bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img_rgb, pt, right_bottom, (255, 0, 0), 2)
        print("*"*100)

    cv2.imshow('img_rgb', img_rgb)
    cv2.waitKey(0)

if __name__ == '__main__':  
    main()  

