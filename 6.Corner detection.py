import numpy as np
import cv2

img = cv2.imread("D:\#DATA\Programming\Python\Projects\OpenCV\image.jpg", -1)
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#returns all the corners as floats
corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
corners = np.int0(corners) #converting into int

for corner in corners:
    x,y = corner.ravel() #flatten an array [[1,2],[4,1]] -> [1,2,4,1]
    cv2.circle(img, (x,y), 5, (255,0,0), -1)

#drawing lines connecting all the corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
