#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: trackbar_example.py
# time: 2019-11-15 20:44
# @Software: PyCharm

import cv2

cv2.namedWindow('image')


def nothing(x):
    print(x)


switch = 'BGR2GRAY'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

cv2.createTrackbar('pos', 'image', 0, 255, nothing)

while(1):
    img = cv2.imread('lena_copy.jpg')
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    pos = cv2.getTrackbarPos('pos', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (100, 200), font, 10, (110, 120, 119))
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image', img)
cv2.destroyAllWindows()