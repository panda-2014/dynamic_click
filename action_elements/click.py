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
    print("*"*100,"do click")
    vv=action['value'].replace(" ","").split(",")

    x,y,repeat,interval=0,0,0,0
    if vv[0].find("ref")!=-1:
        ref_id=int(vv[0].replace(" ","").split(":")[1])
        box=actions[ref_id]['position']
        print("#"*10,box)
        x,y,repeat,interval=box[0]+int(vv[1]),box[1]+int(vv[2]),vv[3],vv[4]
    else:
        x,y,repeat,interval=vv[0],vv[1],vv[2],vv[3]
    action['position']=[x,y]
    time.sleep(float(action['sleep1']))
    eval("pyautogui.click(x={},y={},clicks={},interval={},button='left')".format(x,y,repeat,interval))
    time.sleep(float(action['sleep2']))
    return int(action['next_id'])
