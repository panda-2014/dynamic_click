import pyautogui
# import the module
import time
import json
import sys

'''
def begin():
    global start,end,actions
    for action in trace['actions']:
        print('action:{}     ====    {}'.format(action['name'],time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))))
        if time.time()>end:
            exit(0)
        if action['name']=='sleep':
            time.sleep(float(action['value']))
        elif action['name']=='move': 
            vv=action['value'].replace(" ","").split(",")
            eval("pyautogui.moveTo({},{},duration={})".format(vv[0],vv[1],vv[2]))
        elif action['name']=='click': 
            vv=action['value'].replace(" ","").split(",")
            eval("pyautogui.click(x={},y={},clicks={},interval={},button='left')".format(vv[0],vv[1],vv[2],vv[3]))
        elif action['name']=='press': 
            vv=action['value'].replace(" ","").split(",")
            eval("pyautogui.mouseDown(x={},y={},button='left')".format(vv[0],vv[1]))
        elif action['name']=='release': 
            vv=action['value'].replace(" ","").split(",")
            eval("pyautogui.mouseUp(x={},y={},button='left')".format(vv[0],vv[1]))
        elif action['name']=='drag': 
            vv=action['value'].replace(" ","").split(",")
            eval("pyautogui.dragTo(x={},y={},duration={},button='left')".format(vv[0],vv[1],vv[2]))
'''


def do(actions,action):
    print("*"*100,"do move")
    vv=action['value'].replace(" ","").split(",")

    x,y,interval=0,0,0

    if vv[0].find("ref")!=-1:
        x,y,interval=10,10,vv[2]
    else:
        x,y,interval=vv[0],vv[1],vv[2]
    action['position']=[vv[0],vv[1]]
    time.sleep(float(action['sleep1']))
    eval("pyautogui.moveTo({},{},duration={})".format(x,y,interval))
    time.sleep(float(action['sleep2']))
    return int(action['next_id'])
