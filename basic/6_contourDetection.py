import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
# Resize
img = cv.resize(image,(400,300),interpolation=cv.INTER_AREA)   # inter_cubic for enlarging but slow and linear for fast
#cv.imshow("resized",img)
#blank
blank = np.zeros((img.shape[0],img.shape[1],3),dtype='uint8')
#cv.imshow("blank",blank)
# blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) 
# gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# canny
canny =cv.Canny(blur,125,175)
cv.imshow("canny",canny)

# threshold  --> binary image
ret , thresh = cv.threshold(gray,125,175,cv.THRESH_BINARY)
#cv.imshow("threshold",thresh)

# it takes binary image (e.g. canny or thresh) and find contours
contours ,  heirarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#print(contours)
cnt = sorted(contours,key=cv.contourArea,reverse=True)[0]
abc = np.asarray(cnt,dtype=object)
print(abc)
a = np.average(abc,axis=2)
print(a)
x = int(a[0][0])  
y=int(a[0][1])

# draw contours
cv.drawContours(blank,contours,-1,(255,255,0),thickness=1)   # canny is better than threshold
#cv.imshow("contours",blank)
cv.waitKey(0)