#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: trackbar_example1.py
# time: 2019-11-15 19:34
# @Software: PyCharm

import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


# Create a black image, window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

switch = '0:OFF \n 1:ON'

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:  # esc的ascll为27
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]  # img[:] == img[::1] == img[:::]



cv.destroyAllWindows()