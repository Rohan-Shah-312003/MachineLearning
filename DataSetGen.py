'''

import random
acc = []
dec = []
hndl = [] #handling
ov = [] #overall rating
for i in range (0,999):
    acc.append((random.randint(0,10))*0.1)
    dec.append((random.randint(0,10))*0.1)
    hndl.append((random.randint(0,10))*0.1)
    ov.append((random.randint(0,10))*0.1)
print(acc)
print(dec)
print(hndl)
print(ov)

'''
import cv2 as cv
img = cv.imread("C:\Users\rohan\Downloads\bologna_sandwich.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window