import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,300),interpolation=cv.INTER_AREA)
cv.imshow("imaeg",img)
blank = np.zeros(img.shape[:2],dtype='uint8')

# split channels
b,g,r = cv.split(img)
#merge
blue = cv.merge([b,blank,blank])
cv.imshow("blue",blue)
red = cv.merge([blank,blank,r])
cv.imshow("red",red)
green = cv.merge([blank,g,blank])
cv.imshow("green",green)

cv.waitKey(0)
