import cv2 as cv

img = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
# cv.imshow("imge",img)

# Resize
resized = cv.resize(img,(400,400),interpolation=cv.INTER_AREA)   # inter_cubic for enlarging but slow and linear for fast
cv.imshow("resized",resized)

# Grayscale
gray_image = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray_image)

# Blur
blur = cv.GaussianBlur(resized,(9,9),cv.BORDER_DEFAULT)   # ksize is a tuple must be odd no. and both same
cv.imshow("blur", blur)

# Edge cascade
canny = cv.Canny(resized,125,175)
cv.imshow("canny",canny )

# Dilate
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow("dilated",dilated)

# Eroded reverse of dilate
eroded = cv.erode(canny,(3,3),iterations=1)
cv.imshow("eroeded",eroded)


#cropping
croped = resized[100:400,100:400]
cv.imshow("cropped",croped)
cv.waitKey(0)
