import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,400),interpolation=cv.INTER_AREA)
#cv.imshow("imaeg",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY",gray)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])   # for grascale channel = [0]

plt.figure()
plt.title("GRAYSCALE HISTOGRAM")
plt.xlabel("Intensity")
plt.ylabel("NO of pixels")
plt.plot(gray_hist,color='0')
plt.show()
