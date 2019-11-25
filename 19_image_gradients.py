#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 21_image_gradients.py
# time: 2019-11-24 9:09
# @Software: PyCharm
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)  # cv2.CV_64F is the data type to process the negtive data
lap = np.uint8(np.absolute(lap))
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
canny = cv2.Canny(img, 100, 200)

sobelCombined = cv2.bitwise_or(sobel_x, sobel_y)


titles = ['origin', 'Laplacian', 'sobel_x', 'sobel_y', 'sobelCombined', 'canny']
images = [img, lap, sobel_x, sobel_y, sobelCombined, canny]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()
