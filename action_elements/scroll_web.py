import pyautogui
# import the module
import time
import json
import sys

def do(actions,action):
    print("*"*100,"do scroll_web")
    vv=action['value'].replace(" ","")
    x,y=pyautogui.position()
    action['position']=[x,y]
    time.sleep(float(action['sleep1']))
    eval("pyautogui.scroll({})".format(vv))
    time.sleep(float(action['sleep2']))
    return int(action['next_id'])
