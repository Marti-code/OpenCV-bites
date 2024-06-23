import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    #draw a cross
    img = cv2.line(frame, (0,0), (width, height), (255, 0,0), 10) #(image, (starting position), (ending position), (bgr color), line thickness)
    img = cv2.line(img, (0,height), (width, 0), (0, 0,255), 5) 
    
    #draw a rectangle
    img = cv2.rectangle(img, (110, 100), (230, 200), (0,255,0), 5)

    #draw a circle
    img = cv2.circle(img, (300,300), 200, (120, 120, 120), -1) # -1 -> the circle will be filled in

    #draw text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Hello Vitberg", (200,400), font, 2, (0,0,0), 4, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'): 
        break

capture.release()
cv2.destroyAllWindows()