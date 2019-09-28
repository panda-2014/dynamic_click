# -*-encoding:utf-8-*-  
import pyautogui
import time
import json
import sys,os
import pytesseract  
from PIL import Image  
from PIL import ImageFilter  
from PIL import ImageFont  
from PIL import ImageDraw  
import numpy as np  
from PIL import Image
import cv2  
# pyautogui.screenshot()
def grab_screen_linux(): 
    beg = time.time()
    debug = False
    os.system("mkdir -p temp;gnome-screenshot --file={}".format("temp/s.png"))
    img_rgb = cv2.imread('temp/s.png')
    end = time.time()
    print("#"*100,end - beg)
    return img_rgb


def grab_screen(): 
    from PIL import Image,ImageGrab
    beg = time.time()
    debug = False
    #img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
    img =ImageGrab.grab()
    #img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    img = cv2.cvtColor(numpy.asarray(img),cv2.COLOR_RGB2BGR)
    end = time.time()
    print("#"*100,end - beg)
    return img

def compare(template_img,threshold=0.95):
    #img_rgb=grab_screen()
    img_rgb=grab_screen_linux()
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_img, 0)
    h, w = template.shape[:2]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    ret=False
    box=[]
    for pt in zip(*loc[::-1]):
        box.extend([pt[0],pt[1],pt[0] + w, pt[1] + h])
        ret=True
        print("*"*100)
        break

    return ret,box

def do(actions,action):
    print("*"*100,"do trace image")
    time.sleep(float(action['sleep1']))
    img_path=os.path.join('trace_images',action['value'].replace(" ",""))
    ret,box=compare(img_path)
    action['position']=box
    next_id=0
    if ret:
        print("*"*30,'trace image===> true')
        next_id=action['next_id_yes']
    else:
        print("*"*30,'trace image===> false')
        next_id=action['next_id_no']
    time.sleep(float(action['sleep2']))
    return next_id
