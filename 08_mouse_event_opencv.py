#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: mouse_event_opencv.py
# time: 2019-10-27 0:11
# @Software: PyCharm

import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):  # 点击鼠标会自动给出xy坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red )
        cv2.putText(img, strBGR, (x, y), font, 1, (128, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)

img = cv2.imread('lena_copy.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()