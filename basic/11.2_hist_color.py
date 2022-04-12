import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
img = cv.resize(image,(400,400),interpolation=cv.INTER_AREA)
cv.imshow("imaeg",img)

plt.figure()
plt.title("Colour HISTOGRAM")
plt.xlabel("Intensity")
plt.ylabel("NO of pixels")

colors = ('b','g','r')
for i,clr in enumerate(colors):
    hist_C = cv.calcHist([img],[i],None,[256],[0,256])  # for colored image channel =[0,1,2] for b,r,g respectively
    plt.plot(hist_C,color=clr)
plt.show()