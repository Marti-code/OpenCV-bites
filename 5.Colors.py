import numpy as np
import cv2
from numpy.core.numeric import ones

capture = cv2.VideoCapture(0)


while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50]) #(bgr)
    upper_blue = np.array([130, 255, 255])

    lower_pink = np.array([120, 0, 0])
    upper_pink = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", result)
    #cv2.imshow("mask", mask)

    if cv2.waitKey(1) == ord('q'): 
        break


capture.release()
cv2.destroyAllWindows()
