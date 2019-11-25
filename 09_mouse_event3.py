#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: mouse_event3.py
# time: 2019-10-27 1:00
# @Software: PyCharm

import numpy as np
import cv2


def click_enent(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv2.imshow('color', mycolorImage)

img = cv2.imread('lena_copy.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_enent)

cv2.waitKey(0)
cv2.destroyAllWindows()