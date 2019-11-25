ploy#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: matlib_with_opencv.py
# time: 2019-11-20 9:04
# @Software: PyCharm

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena_copy.jpg')
cv2.imshow('lena', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()