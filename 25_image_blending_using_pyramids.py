#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 25_image_blending_using_pyramids.py
# time: 2019-11-27 8:49
# @Software: PyCharm
"""
1.load tow images which are apple and orange
2.find the Gaussian Pyramids for apple and orange
3.form Guassoam Pyramids, find their Laplacian Pyramids
4.join the left half of apple and right half of orange in each levels of Laplacian Pyriamids
5. from the joint image pyramids, reconstruct the origin image
"""
import cv2
import numpy as np
# step 1
orange = cv2.imread('orange.jpg')
apple = cv2.imread('apple.jpg')

orange_copy = orange.copy()
apple_copy = apple.copy()

col, row, ch = orange.shape
apple_and_orange = np.hstack((orange_copy[:, 0:int(col/2)], apple_copy[:, int(col/2):]))

# step 2
gs_orange = [orange_copy]  # to show the Guassian Pyramids result
gs_apple = [apple_copy]

for i in range(5):
    orange_copy = cv2.pyrDown(orange_copy)
    gs_orange.append(orange_copy)
    # gs_orange里面包含了原图以及6张从大到小的高斯金字塔处理过的图片，索引为0，1-5，最小的图orange_copy索引为5

    apple_copy = cv2.pyrDown(apple_copy)
    gs_apple.append(apple_copy)


# step 3
orange_copy = gs_orange[5]
lp_orange_s = [orange_copy]  # to show the Laplacian Pyramids result
apple_copy = gs_apple[5]
lp_apple_s = [apple_copy]
for i in range(5, 0, -1):  # 从倒数第1张图（gs_orange[5]）开始计算并存储，第六步从倒数第1张图（gs_orange[5]）开始，对应起来了
    gs_expanded_orange = cv2.pyrUp(gs_orange[i])
    lp_orange = cv2.subtract(gs_orange[i-1], gs_expanded_orange)
    lp_orange_s.append(lp_orange)
    # lp_orange_s 存储了从小到大的6张图片，0存储出的是gs_orange[5]，1-5 从倒数第1张（gs_orange[5]）开始的上采样图

    gs_expanded_apple = cv2.pyrUp(gs_apple[i])
    lp_apple = cv2.subtract(gs_apple[i-1], gs_expanded_apple)
    lp_apple_s.append(lp_apple)

# step 4
apple_organ_pyramids = []
n = 0
for apple_lp, organ_lp in zip(lp_apple_s, lp_orange_s):  #lp_orange_s[0]是彩色图，即gs_orange[5]，之后才是边缘（lp计算出来的）
    n += 1
    cols, rows, channels = apple_lp.shape
    lp = np.hstack((apple_lp[:, 0:int(cols/2)], organ_lp[:, int(cols/2):]))
    apple_organ_pyramids.append(lp)

# step 5
apple_orange_reconstruct = apple_organ_pyramids[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_organ_pyramids[i], apple_orange_reconstruct)

cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_and_origin', apple_and_orange)
cv2.imshow('apple_orange_reconstruct',apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()