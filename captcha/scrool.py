#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:56:31 2021

@author: mac
"""

import pyautogui
import cv2
import numpy as np
import time
from PIL import Image

print("Start...")
time.sleep(5)
#pyautogui.hotkey('alt','tab')
#,region=(493,258,406,272)
#pyautogui.screenshot('name.png')
pyautogui.hotkey('shift','command','3')
#im.show()
#button7location = pyautogui.locateOnScreen("empty.PNG")
#x, y = pyautogui.center(button7location)
a , b = pyautogui.locateCenterOnScreen("empty.PNG",confidence=0.585)
x , y = pyautogui.locateCenterOnScreen("sl.PNG",confidence=0.585)
#print(a)
#pyautogui.hotkey('ctrl','w')
#im1=Image.open(r"name.png")
#im1.show()
#empty = pyautogui.locateCenterOnScreen("empty.PNG")
#print(empty)
#ex, ey = pyautogui.center(empty)

#x , y = pyautogui.locateCenterOnScreen("sl.PNG",confidence=0.585)

#time.sleep(5)
#pyautogui.hotkey('ctrl','w')
pyautogui.click(x,y)
pyautogui.dragTo(x,a,1.75, button='left')