import cv2 as cv


image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,300),interpolation=cv.INTER_AREA)
#cv.imshow("imaeg",img)

# split channels
b,g,r = cv.split(img)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)

# merge channels
merged = cv.merge([b,g,r])
cv.imshow("merged",merged)

print(img.shape)
print(r.shape)
cv.waitKey(0)
