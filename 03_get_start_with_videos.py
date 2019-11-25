#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: get_start_with_videos.py
# time: 2019-10-25 0:18
# @Software: PyCharm

import cv2

cap = cv2.VideoCapture(0);

fourcc = cv2.VideoWriter_fourcc(*'XVID')
"filename, fourcc, fps, frameSize, isColor=None"
out = cv2.VideoWriter(r'./output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        weight = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获取视频的宽度
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 获取视频的高度
        print(weight, height)

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
