import cv2;

img = cv2.imread("D:\#DATA\Programming\Python\Projects\OpenCV\image.jpg", -1);

tag = img[800:1100, 900:1200];
img[100:400, 500:800] = tag;

img =cv2.resize(img, (0,0), fx=0.3, fy=0.3);

cv2.imshow("image", img);
cv2.waitKey(0);
cv2.destroyAllWindows();