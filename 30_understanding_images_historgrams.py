#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 30_understanding_images_historgrams.py
# time: 2019-12-01 8:12
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena_copy.jpg', 0)  # gray
# img = np.zeros((200, 200), dtype=np.uint8)
# cv2.rectangle(img, (0, 100), (200, 200), (255), -1)
# b, g, r = cv2.split(img)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
"""imaes:输入的图像
channels:选择图像的通道
mask:掩膜，是一个大小和image一样的np数组，其中把需要处理的部分指定为1，不需要处理的部分指定为0，一般设置为None，表示处理整幅图像
histSize:使用多少个bin(柱子)，一般为256
ranges:像素值的范围，一般为[0,255]表示0~255
"""
# hist是一个shape为(256,1)的数组，表示0-255每个像素值对应的像素个数，下标即为相应的像素值
# plot一般需要输入x,y,若只输入一个参数，那么默认x为range(n)，n为y的长度
plt.plot(hist)
# cv2.imshow('image', img)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)


# plt.hist(img.ravel(), 256, [0, 256])
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
