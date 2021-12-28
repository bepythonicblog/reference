import pyautogui
import cv2
import numpy as np
import time
from PIL import Image

print("start")
time.sleep(5)
#pyautogui.hotkey('alt','tab')
#pyautogui.screenshot('name.png',region=(493,258,406,272))
image = cv2.imread('name.png')
lower=np.array([70,70,70],dtype="uint8")
upper=np.array([180,180,180],dtype="uint8")
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imwrite('gray.png', output)
im=Image.open(r"gray.png")
im.show()
coordinate = ()
im=Image.open(r"gray.png")
im.show()
coordinate = pyautogui.locateCenterOnScreen("empty.PNG")
while coordinate == None:
    for i in range(1,3):
        coordinate = pyautogui.locateCenterOnScreen(str(i)+"g.png")
        print("coordinate: ",coordinate)

#pyautogui.hotkey('ctrl','w')
a,b = coordinate
im1 = Image.open(r"name.png")
im1.show()
time.sleep(10)
x,y = pyautogui.locateCenterOnScreen("sl.PNG",confidence=0.585)
#pyautogui.hotkey('ctrl','w')
pyautogui.click(x,y)
pyautogui.dragTo(a,y,1.75, button='left')