import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break


while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8) #creating array
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    #four videos in one video
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame
    
    cv2.imshow("frame", image)

    if cv2.waitKey(1) == ord('q'): 
        break


capture.release()
cv2.destroyAllWindows()