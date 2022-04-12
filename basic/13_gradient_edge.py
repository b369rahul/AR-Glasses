import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,400),interpolation=cv.INTER_AREA)
#cv.imshow("imaeg",img)

gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray_image)

# Canny (defined earlier)
# LAplacian 

lapla = cv.Laplacian(gray_image,cv.CV_64F)
lapla = np.uint8(np.absolute(lapla))
cv.imshow("LAPLACIAN",lapla)

# SOPEL  calculate in different direction
sobelx = cv.Sobel(gray_image,cv.CV_64F,1,0)
sobely = cv.Sobel(gray_image,cv.CV_64F,0,1)
sobel_merge = cv.bitwise_or(sobelx,sobely)

cv.imshow("SOBEL X",sobelx)
cv.imshow("SOBEL Y",sobely)
cv.imshow("SOBEL MERGE",sobel_merge)

cv.waitKey(0)