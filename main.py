import pyautogui
# import the module
import time
import sched
import json
import sys
import action_elements.click

# instantiate an mouse object
def begin():
    global start,end,actions
    next_id=1
    while next_id>0:
        if time.time()>end:
            exit(0)
        exec("import action_elements.{}".format(actions[next_id]['name']))
        next_id=eval("action_elements.{}.do(actions,actions[next_id])".format(actions[next_id]['name']))
        print("=================>",next_id)
        if next_id<0:
            print("exit with -1")
 
def do():
    cnt=0
    while(True):
        cnt+=1
        print('cnt:{}: run again    ====    {}'.format(cnt,time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))))
        begin()

actions={}
def parser_action(action_file):
    global actions
    trace=None
    with open(action_file,'r') as load_f:
        trace = json.load(load_f)

    ts,end=0,0
    if trace['start']=='':
        ts=2
        end=time.time()+30
    else:
        ts = time.mktime(time.strptime(trace['start'], "%Y-%m-%d %H:%M:%S"))-time.time()
        end = time.mktime(time.strptime(trace['end'], "%Y-%m-%d %H:%M:%S"))

    for _action in trace['actions']:
        actions[_action['id']]=_action

    return ts,end

if __name__=="__main__":
    ts,end=parser_action("./trace.json")
    print('begin.... {}'.format(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))))
    s = sched.scheduler(time.time,time.sleep)
    start=time.time()
    s.enter(ts,0,do,())
    s.run()
    print('end....')
