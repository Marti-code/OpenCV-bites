import cv2

#we need to read them in grayscale
img = cv2.imread("D:\#DATA\Programming\Python\Projects\OpenCV\PC2021591.png", 0)
template = cv2.imread("D:\#DATA\Programming\Python\Projects\OpenCV\PC2021591_template.png", 0)

#can do that with grayscale
height, width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    img2 = img.copy() #so every method will have a new image to work with

    result = cv2.matchTemplate(img2, template, int(method)) #returns an array
    min_value, max_value, min_location, max_location = cv2.minMaxLoc(result)

    #location -> top-left corner
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_location
    else:
        location = max_location

    location = min_location
    bottom_right = (location[0]+width, location[1]+height)
    cv2.rectangle(img2, location, bottom_right, 255, 3)
    cv2.imshow("Match",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()