import cv2 as cv
import numpy as np
import mouse as ms

import statistics
def func3(list):
    return tuple(list)

blank = np.zeros((480,640,3),dtype="uint8") + 255

def func (value):
    pass
cv.namedWindow("Trackbars")
cv.createTrackbar("Hue max","Trackbars",17,179,func)

cv.createTrackbar("Sat max","Trackbars",255,255,func)

cv.createTrackbar("Val max","Trackbars",180,255,func)

cv.createTrackbar("Hue m","Trackbars",0,179,func)

cv.createTrackbar("Sat m","Trackbars",213,255,func)

cv.createTrackbar("Val m","Trackbars",191,255,func)  
vid = cv.VideoCapture(0)
vid.set(3,1280)
vid.set(4,640)
vid.set(10,150)
def position(a,b):
    l5=ms.move(a,b)
def get_mask(image_1,image_2):
    hue_max = cv.getTrackbarPos("Hue max","Trackbars")
    sat_max = cv.getTrackbarPos("Sat max","Trackbars")
    val_max = cv.getTrackbarPos("Val max","Trackbars")
    hue_m = cv.getTrackbarPos("Hue m","Trackbars")
    sat_m = cv.getTrackbarPos("Sat m","Trackbars")
    val_m = cv.getTrackbarPos("Val m","Trackbars")
    low = np.array((hue_m,val_m,sat_m))
    high = np.array((hue_max,val_max,sat_max))
#    blur = cv.medianBlur(image_1,1)
    mask = cv.inRange(image_1,low,high)
    canny = cv.Canny(mask,125,255)
    eroded = cv.erode(canny,(3,3))
    dilated = cv.dilate(eroded,(5,5),iterations=5)
    #cv.imshow("CANNY",canny)
    cv.imshow("MASK",mask)
    #cv.imshow("DILATEED",dilated)
    #cv.imshow("ERODED",eroded)
    contours,h = cv.findContours(dilated,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    if len(contours) !=0:
        cnt1 = sorted(contours, key = cv.contourArea, reverse = True)[0]
        if len(contours) >1:
            cnt2 = sorted(contours, key = cv.contourArea, reverse = True)[1]
            #print(cv.contourArea(cnt1),cv.contourArea(cnt2))
            if cv.contourArea(cnt2)>400 and cv.contourArea(cnt1)>400:
                l=ms.press(button=ms.LEFT)
                l2= ms.release(button=ms.LEFT)
        if cv.contourArea(cnt1)>200:
            ((x, y), radius) = cv.minEnclosingCircle(cnt1)
            l3= position(x,y)
while True:
    istrue, frame = vid.read()
    flip = cv.flip(frame,1)
    frame_hsv = cv.cvtColor(flip,cv.COLOR_BGR2HSV)
    get_mask(frame_hsv,flip)
    if cv.waitKey(1) == ord('q'):
        break 