import cv2
import random
# in OpenCV colors are not RGB but BGR -> blue, green, red

img = cv2.imread("D:\#DATA\Programming\Python\Projects\OpenCV\image.jpg", -1)

print(img.shape) #(heigh, width)
print(img[0]) #pixels from the first row
print(img[0][34:67]) #pixels form the first row from 34 to 67
print(img[4][67]) #pixel from the 5-th row at 67 position

#setting random color values to the rows
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randrange(255), random.randrange(255), random.randrange(255)]


#copying part of a pic and pasting it
tag = img[500:700, 600:900]
#from 500 to 700 rows, then 600 to 900 columns in those rows
img[100:300, 500:800] = tag

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()