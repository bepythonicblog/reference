#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:07:39 2021

@author: mac
"""
import pyautogui
import cv2
import numpy as np
import time
from PIL import Image
from matplotlib import pyplot as plt

print("Start...")
time.sleep(5)
image = cv2.imread('name.png')
lower = np.array([70,70,70],dtype="uint8")
upper = np.array([180,180,180],dtype="uint8")
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imwrite('gray.png', output)
im = Image.open(r"gray.png")
im.show()

coordinate = pyautogui.locateCenterOnScreen("empty.PNG",confidence=0.585)
while coordinate == None:
    for i in range(1,3):
        im = str(i)+"g.png"
        ima = cv2.imread(im)
        plt.imshow(ima)
        coordinate = pyautogui.locateCenterOnScreen(im,confidence=0.585)
        print("coordinate: ",coordinate)
