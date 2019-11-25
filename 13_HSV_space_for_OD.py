#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: HSV_space_for_OD.py
# time: 2019-11-16 19:04
# @Software: PyCharm

import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0);

cv2.namedWindow('tracing')
cv2.createTrackbar('L_H', 'tracing', 0, 255, nothing)
cv2.createTrackbar('L_S', 'tracing', 0, 255, nothing)
cv2.createTrackbar('L_V', 'tracing', 0, 255, nothing)

cv2.createTrackbar('H_H', 'tracing', 255, 255, nothing)
cv2.createTrackbar('H_S', 'tracing', 255, 255, nothing)
cv2.createTrackbar('H_V', 'tracing', 255, 255, nothing)


while (cap.isOpened()):
    # frame = cv2.imread('smarties.png')  # BGR
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('L_H', 'tracing')
    l_s = cv2.getTrackbarPos('L_S', 'tracing')
    l_v = cv2.getTrackbarPos('L_V', 'tracing')

    h_h = cv2.getTrackbarPos('H_H', 'tracing')
    h_s = cv2.getTrackbarPos('H_S', 'tracing')
    h_v = cv2.getTrackbarPos('H_V', 'tracing')

    low_b = np.array([l_h, l_s, l_v])
    high_b = np.array([h_h, h_s, h_v])

    mask = cv2.inRange(hsv, low_b, high_b)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

