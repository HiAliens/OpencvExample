#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 23_images_pyramids_2.py
# time: 2019-11-26 10:02
# @Software: PyCharm
"""
拉普拉斯金字塔池化
"""
import cv2
import numpy as np
img = cv2.imread('apple.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

# laplacian
layer = gp[5]
cv2.imshow('upper lever Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('origin', img)
cv2.waitKey(0)
cv2.destroyAllWindows()