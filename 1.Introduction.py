import cv2;

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR);
#img = cv2.imread("image.jpg", -1);

# -1 = cv2.IMREAD_COLOR -> color without transparency
# 0 = cv2.IMREAD_GRAYSCALE -> in grayscale mode
# 1 = cv2.IMREAD_UNCHANGED -> exactly as the original

#resize the image to be 1/3 the size
#img = cv2.resize(img, (300,300)); -> 300 width and 300 height no proportions
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3);

img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE);

#will create the new image with the changes applied to it earlier
cv2.imwrite("new_img.jpg", img);

#Image -> name of the window
cv2.imshow("Image", img);

# 0 -> will wait untill we press any key, but e.g. 5 -> wait 5 sec for a key press or close the window
cv2.waitKey(0);
cv2.destroyAllWindows();