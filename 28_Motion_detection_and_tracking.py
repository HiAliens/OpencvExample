 #!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: Motion_detection_and_tracking.py
# time: 2019-11-29 8:29
# @Software: PyCharm
import cv2
import numpy as np



cap = cv2.VideoCapture('vtest.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter(r'28_images/output.avi',fourcc, 20.0, (768, 576) )
ret, fram1 = cap.read()
# cv2.imwrite(r'28_images/fram1.jpg', fram1)
ret, fram2 = cap.read()
# cv2.imwrite(r'28_images/fram2.jpg', fram2)

while cap.isOpened():
    # weight = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # print(weight, height)  # 768, 567
    diff = cv2.absdiff(fram1, fram2)  # 查找两针之间的差别
    # cv2.imshow('fram1', fram1)
    # cv2.imshow('fram2', fram2)
    # cv2.imshow('diff', diff)
    # cv2.imwrite(r'28_images/diff.jpg', diff)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    # cv2.imwrite(r'28_images/gray.jpg', gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 平滑处理
    # cv2.imshow('blur', blur)
    # cv2.imwrite(r'28_images/blur.jpg', blur)
    dilated = cv2.dilate(blur, None, iterations=3)  # 腐蚀，取局部最大值
    # cv2.imshow('dilated', dilated)
    # cv2.imwrite(r'28_images/dilated.jpg', dilated)
    _, threshold = cv2.threshold(dilated, 25, 255, cv2.THRESH_BINARY)
    # cv2.imshow('threshold', threshold)
    # cv2.imwrite(r'28_images/threshold.jpg', threshold)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # '_'返回值是层级关系，是一个N*4的矩阵，N为len（contours）
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(fram1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(fram1, 'Status:{}'.format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

    #cv2.drawContours(fram1, contours, -1, (0, 255, 0), 2)
    # cv2.imshow('fram1', fram1)
    # cv2.imwrite(r'28_images/fram1_2.jpg', fram1)

    cv2.imshow('feed', fram1)
    fram1 = fram2
    ret, fram2 = cap.read()

    writer.write(fram1)  # 写入视频文件
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
