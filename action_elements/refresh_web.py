import pyautogui
# import the module
import time
import json
import sys

def do(actions,action):
    print("*"*100,"do refresh_web")
    vv=action['value'].replace(" ","")
    x,y=pyautogui.position()
    action['position']=[x,y]
    time.sleep(float(action['sleep1']))
    pyautogui.press('f5')
    eval("pyautogui.press('{}')".format(vv))
    time.sleep(float(action['sleep2']))
    return int(action['next_id'])
