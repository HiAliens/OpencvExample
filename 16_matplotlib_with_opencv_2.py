#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: matplotlib_with_opencv_2.py
# time: 2019-11-20 9:42
# @Software: PyCharm

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena_copy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th0 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
th1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_TOZERO, 11, 2)
# th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_TOZERO_INV, 11, 2)
# th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_TRUNC, 11, 2)

images_names = ['origin', 'BINARY', 'BINARY_INV', 'THRESH_TOZERO', 'THRESH_TOZERO_INV', 'THRESH_TRUNC']
images = [gray, th0, th1]
for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([0])
    plt.title(images_names[i])
plt.show()
