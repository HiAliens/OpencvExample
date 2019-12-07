#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 31_template_matching.py
# time: 2019-12-02 8:04
# @Software: PyCharm
# 参考：https://www.cnblogs.com/ssyfj/p/9271883.html
import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi_face.jpg', 0)
h, w = template.shape

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# print(res)
# threshold = 0.6;
# loc = np.where(res >= threshold)
# print(loc)
#
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(max_val, max_loc)
tl = max_loc
br = (tl[0] + w, tl[1] + h)
cv2.rectangle(img, tl, br, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()