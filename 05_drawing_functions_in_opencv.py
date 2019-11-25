#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: drawing_functions_in_opencv.py
# time: 2019-10-26 21:59
# @Software: PyCharm

import numpy as np
import cv2

# img = cv2.imread('lena_copy.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (203, 235, 21), 10)  # 21, 235, 203
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

img = cv2.rectangle(img, (387, 0), (510, 128), (0, 0, 255), 2)

img = cv2.circle(img, (446, 163), 163, (0, 255, 0), -1)  # -1 表示填充


font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img, 'Opencv', (10, 50), font, 10, (255, 255, 255), 7, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()