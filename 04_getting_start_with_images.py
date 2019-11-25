#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: getting_start_with_images.py.py
# time: 2019-10-21 14:25
# @Software: PyCharm

import cv2

img_path = r'opencv-master/samples/data/lena.jpg'

img = cv2.imread(img_path, -1)
# 判断图片是否存在
print(img)
# 读
cv2.imshow('lena', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # 写
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows()

