#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 27_find_and_draw_contours.py
# time: 2019-11-28 13:48
# @Software: PyCharm
import cv2
img = cv2.imread('opencv-logo.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(img_gray, 127, 255, 0)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("the number of the contours is " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 255), 3)  # -1 means the index of these contours

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
