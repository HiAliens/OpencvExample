#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:Dr.Shang
# file: add_text_to_videos.py
# time: 2019-10-26 23:41
# @Software: PyCharm

import cv2
import datetime

cap = cv2.VideoCapture(0)  # 0：打开0号摄像头，或者给地址打开本地视频文件
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# cap.set(3, 1080) # cv2.CAP_PROP_FRAME_HEIGHT -->1208
# cap.set(5, 1080) # cv2.CAP_PROP_FRAME_WIDTH -->720

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width' + str(cap.get(3)) + 'Height' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()