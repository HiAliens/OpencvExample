#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: canny_edge_detection.py
# time: 2019-11-23 9:31
# @Software: PyCharm
import cv2
from matplotlib import pyplot as plt




def nothing(x):
    pass


cv2.namedWindow('images')
cv2.createTrackbar('low', 'images', 0, 255, nothing)
cv2.createTrackbar('high', 'images', 0, 255, nothing)
while True:
    img = cv2.imread('lena_copy.jpg', 0)  # read img in gray in order to be show by plt

    if cv2.waitKey(1) & 0xFF == 27:
        break
    low = cv2.getTrackbarPos('low', 'images')  # min_val
    high = cv2.getTrackbarPos('high', 'images')  # max_val
    canny = cv2.Canny(img, low, high)
    names = ['image', 'canny']
    images = [img, canny]
    # for i in range(2):
    #     plt.subplot(1, 2, i+1)
    #     plt.imshow(images[i], 'gray')  # use the 'gray' parameter
    #     plt.title(names[i])
    #     plt.xticks([]), plt.yticks([])
    # plt.show()
    cv2.imshow('images', canny)

cv2.destroyAllWindows()