#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 图片切片.py
# time: 2019-11-15 20:08
# @Software: PyCharm

import cv2 as cv

img = cv.imread(r'../lena_copy.jpg')
img[:] = [255, 224, 223]
print(img[:])