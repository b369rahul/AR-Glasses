import cv2 as cv

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,300),interpolation=cv.INTER_AREA)
cv.imshow("imaeg",img)

# averaging
avg_b = cv.blur(img,(5,5))
cv.imshow("avg",avg_b)

# Gaussian blur
gauss_b = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("gauss",gauss_b)
 
# Median blur
median_b = cv.medianBlur(img,3)
cv.imshow("Median", median_b)

# Bilateral blur
bilateral = cv.bilateralFilter(img,5,50,50)
cv.imshow("bilateral",bilateral)

cv.waitKey(0)