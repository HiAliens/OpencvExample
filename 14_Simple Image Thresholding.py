#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: Simple Image Thresholding.py
# time: 2019-11-18 9:00
# @Software: PyCharm

import cv2
import numpy as np

img = cv2.imread('gradicent.png', 0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 0 or 1
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 0 to 1, 1 to 0
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # 小于127是原图像素值，大于部分全为127
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # 小于127全位0，大于部分为原图
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 小于127为原图，大于部分为0


cv2.imshow('img', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)

cv2.waitKey(0)
cv2.destroyAllWindows()
