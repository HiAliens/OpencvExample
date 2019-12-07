#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 23_images_pyramids.py
# time: 2019-11-26 9:43
# @Software: PyCharm
import cv2
import numpy as np
img = cv2.imread('lena_copy.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2)

cv2.imshow('img', img)
cv2.imshow('lr1', lr1)
cv2.imshow('lr2', lr2)
cv2.imshow('hr1', hr1)

cv2.waitKey(0)
cv2.destroyAllWindows()