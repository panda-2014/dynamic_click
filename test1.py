import pyautogui
# import the module
import time
import sched
import json
import sys

# instantiate an mouse object
def begin():
    #pyautogui.scroll(-10)
    #pyautogui.scroll(-10)
    pyautogui.press('f5')
def do():
    cnt=0
    while(True):
        cnt+=1
        print('cnt:{}: run again    ====    {}'.format(cnt,time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))))
        begin()
        break

if __name__=="__main__":
    s = sched.scheduler(time.time,time.sleep)
    start=time.time()
    s.enter(3,0,do,())
    s.run()
    print('end....')
