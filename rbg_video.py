"""
Detect Blue Objects in BGR
Reference:
    https://github.com/michellektan/180DA-WarmUp/blob/main/Tutorial0-Setup/rbg_video.py

"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # define range of blue color in BGR
    lower_blue = np.array([100, 0, 0])
    upper_blue = np.array([255, 100, 100])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    bluecnts = cv2.findContours(mask.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts) > 0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(frame, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()