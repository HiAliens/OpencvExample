#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: 29_shape+detection.py
# time: 2019-11-30 9:18
# @Software: PyCharm
import cv2

img = cv2.imread('geometrical_shape.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshole = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY)
contours, levels = cv2.findContours(threshole, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 使用多边拟合曲线，对于给定点集，对多边形进行逼近
# void approxPolyDP(InputArray curve, OutputArray approxCurve, double epsilon, bool closed)
# 第一个参数 InputArray curve：输入的点集
# 第二个参数OutputArray approxCurve：输出的点集，当前点集是能最小包容指定点集的。画出来即是一个多边形。
# 第三个参数double epsilon：指定的精度，也即是原始曲线与近似曲线之间的最大距离。
# 第四个参数bool closed：若为true，则说明近似曲线是闭合的；反之，若为false，则断开。

# cv2.arcLength(cnt， True)  # 计算轮廓的面积
# 参数说明：cnt为输入的单个轮廓值,
# 第二个参数bool closed：若为true，则说明近似曲线是闭合的；反之，若为false，则断开

# cv2.drawContours(img, contours, -1, (0, 0, 0), 5)  # 同样可以画出来
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)  # 返回点集，第二个参数是指定的精度
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)  # 这是介绍了新方法
    # cv2.drawContours(img, contour, 0, (0, 0, 0), 5)
    x = approx.ravel()[0]  # 扁平化，结果同 flatten
    y = approx.ravel()[1] - 10
    print('approx is {}'.format(approx))
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "sqaure", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    elif len(approx) == 10:
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
