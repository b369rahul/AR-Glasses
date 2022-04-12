import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,400),interpolation=cv.INTER_AREA)
#cv.imshow("imaeg",img)
blank = np.zeros(img.shape[:2],dtype='uint8')

rectangle  = cv.rectangle(blank.copy(),(120,100),(270,300),255,-1)
cv.imshow("rectangle",rectangle)

masked = cv.bitwise_and(img,img,mask=rectangle)
cv.imshow("MASKED",masked)

cv.waitKey(0)

