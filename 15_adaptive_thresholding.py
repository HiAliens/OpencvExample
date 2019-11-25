#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: adaptive_thresholding.py
# time: 2019-11-19 13:31
# @Software: PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture(0);

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # _, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 固定的二值化
    th1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2);
    th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2);

    cv2.imshow('cap', th2)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()