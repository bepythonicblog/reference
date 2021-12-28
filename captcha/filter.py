#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:38:24 2021

@author: mac
"""
import pyautogui
import cv2
import numpy as np
import time
from PIL import Image

print("Start...")
time.sleep(5)

img_m = np.zeros([160, 120, 3],dtype="uint8")

for i in range(1,7):
    image = cv2.imread(str(i)+'.png')
    lower = np.array([80,80,80],dtype="uint8")
    upper = np.array([180,160,180],dtype="uint8")
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    cv2.imwrite(str(i)+'g.png', output)
    output = np.resize(output,(160, 120, 3))
    img_m = img_m + output

cv2.imwrite('im_g.png', img_m)
im1 = Image.open(r"im_g.png")
im1.show()

