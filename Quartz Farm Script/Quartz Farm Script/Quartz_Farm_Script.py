import pyautogui as pt
import os
import pyautogui
import mouseinfo
import mouse
import pynput
import time

def move_forward(seconds):
    pt.keyDown('w')
    time.sleep(seconds)
    pt.keyUp('w')
    time.sleep(2)
def drop():
    time.sleep(0.001)
    pt.press('q')
    time.sleep(0.1)

def emerald_converter():
    pyautogui.press('e')
    pt.keyDown('shift')
    for i in range(3):
        pyautogui.moveTo(680, 440)
        pyautogui.click(button='left')
        time.sleep(0.2)
        pyautogui.moveTo(1265, 430)
        pyautogui.click(button='left')
        time.sleep(0.2)
    pt.keyUp('shift')
    pyautogui.press('e')
    
def emerald_intake():
    pt.keyDown('shift')
    pt.keyDown('s')
    time.sleep(0.5)
    pt.keyUp('s')
    pt.keyDown('a')
    time.sleep(1)
    pt.keyUp('a')
    pt.keyUp('shift')
    pyautogui.click(button='left')
    time.sleep(10)

def quartz_send():
    pt.keyDown('s')
    time.sleep(0.75)
    pt.keyUp('s')
    pyautogui.click(button='left')

def walk_to_portal():
    pt.keyDown('s')
    time.sleep(0.4)
    pt.keyUp('s')
    eat()
    pt.keyDown('d')
    time.sleep(0.2)
    pt.keyUp('d')
    pt.keyDown('s')
    time.sleep(0.6)
    pt.keyUp('s')
    pt.keyDown('d')
    pt.keyDown('w')
    time.sleep(0.2)
    pt.keyUp('d')
    pt.keyUp('w')

def item_transfer():
    time.sleep(7)
    pt.keyDown('a')
    time.sleep(4)
    pt.keyUp('a')
    pyautogui.press('e')
    y=550
    x=970
    pt.keyDown('ctrl')
    for i in range(3):
        for i in range(9):
            pyautogui.moveTo(x, y)
            drop()
            x=x+35
        x=x-315
        y=y+35
    x=1180
    y=665
    for i in range(2):
        pyautogui.moveTo(x, y)
        drop()
        x=x+35
        time.sleep(0.2)
    pt.keyUp('ctrl')
    pyautogui.press('e')


def menu_scroller():
    pyautogui.click(button='left')
    time.sleep(0.1)
    pyautogui.moveRel(0, -40)
    pyautogui.click(button='left')
    time.sleep(0.1)
    pyautogui.scroll(-400)
    time.sleep(1)
    pyautogui.scroll(-400)
    time.sleep(0.1)
    pyautogui.moveTo(770, 660)
    pyautogui.click(button='left')
    pyautogui.moveTo(1130, 450)
    time.sleep(2.25)
    pt.keyDown('shift')
    pyautogui.click(button='left')
    pt.keyUp('shift')
    time.sleep(0.2)
    pyautogui.press('esc')
    time.sleep(0.1)

def grab_quartz():
    #range 144, 146 for buffer
    for j in range(146):
        menu_scroller()
        move_forward(0.27)
        time.sleep(0.15)
        pt.keyDown('s')
        time.sleep(0.035)
        pt.keyUp('s')
        output2()

def eat():
    pyautogui.press('6')
    pyautogui.mouseDown(button='left')
    time.sleep(2)
    pyautogui.mouseUp(button='left')
    time.sleep(0.2)
    pyautogui.press('7')

def output1(i):
    cycle = 'Cycle'
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    o = cycle + ': ' + str(i+1) + ' '+ current_time
    print(o)

def output2():
    cycle = 'Trade'
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    global_variable()
    o = cycle + ': ' + str(k) + ' '+ current_time
    print(o)

def global_variable():
    global k
    k = k + 1

#------Main--------#
#Time before function runs
time.sleep(7)
#Movement Start
move_forward(0.1)
k = 0
#Main Script

#Amount of 3 stacks of 64 emerald blocks (range)
for i in range(30):
    grab_quartz()
    item_transfer()
    emerald_intake()
    emerald_converter()
    quartz_send()
    walk_to_portal()
    output1(i)

exit()


