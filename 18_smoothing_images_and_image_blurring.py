  #!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: smoothing_images_and_image_blurring.py
# time: 2019-11-22 9:15
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena_copy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25  # divided by size ^ 2
dst = cv2.filter2D(img, -1, kernel)  # smooth
blur = cv2.blur(img, (5, 5))  # mean method
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)  # use salt-pepper-noise.png to see result
bilatera = cv2.bilateralFilter(img, 9, 75, 75)  # preserve the border of img

images = [img, dst, blur, gblur, median, bilatera]
names = ['image', '2D Convenlution', 'blur', 'GaussianBlur', 'medianBlur', 'bilateralFilter']

for i in range(6):
    subplot = plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(names[i])
    plt.xticks([]), plt.yticks([])
plt.show()
