#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: bitwise_operators.py
# time: 2019-11-15 16:01
# @Software: PyCharm

import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("image_1.png")

# bitAnd = cv2.bitwise_and(img2, img1) # 全1才是1
# bitOr = cv2.bitwise_or(img2, img1)  # 有一个1就是1
# bitXor = cv2.bitwise_xor(img2, img1)  # 相同是0不同是1
bitNot = cv2.bitwise_not(img2)  # 取反

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("not-image2", bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()

