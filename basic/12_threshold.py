import cv2 as cv

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,400),interpolation=cv.INTER_AREA)
#cv.imshow("imaeg",img)

gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray_image)

#Simple Threshold
# in below function if pixel intensity is less than threshold value which we set as 125 below
# it is set its intensity to 0 and if above then set its intensity to 255
thresh_value , thresh = cv.threshold(gray_image, 125, 255, cv.THRESH_BINARY)  
cv.imshow("threshold",thresh)


# Thresh inverse
thresh_value , thresh_inv = cv.threshold(gray_image, 125, 255, cv.THRESH_BINARY_INV)  
cv.imshow("threshold Inverse",thresh_inv)

#Adaptive threshold --> it choses threshold itself by specified method

adaptive_thresh1 = cv.adaptiveThreshold(gray_image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,45,10)
cv.imshow("ADAPTIVE THRESH Median",adaptive_thresh1)

# 45 here is the kernel size and must be odd , 10 is the subtraction value that must be subtracted
#            from the resultant threshold by specified method

adaptive_thresh2 = cv.adaptiveThreshold(gray_image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,45,10)
cv.imshow("ADAPTIVE THRESH Gaussian",adaptive_thresh2)


cv.waitKey(0)