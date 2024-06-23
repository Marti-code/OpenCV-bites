import cv2
import numpy as np

#detect colors in hsv (hue, saturation, value)
lowerRange = np.array([200, 0, 20])
upperRange = np.array([250, 255, 255])

video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, lowerRange, upperRange)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) !=0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)


    cv2.imshow("mask", mask)
    cv2.imshow("video", img)

    cv2.waitKey(1)
