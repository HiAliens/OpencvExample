#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: morphological_transformations_opencv.py
# time: 2019-11-21 9:05
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
形态变形需要用到二值图像（binary images）比如对图像腐蚀、扩张。操作的实质是对邻近像素采用不同的方式进行组合
'''
img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(mask, None, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # erosion +dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # dilation + erosion



titles = ['image', 'mask', 'dilation', 'erosion ', 'opening ', 'closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()