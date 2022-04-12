import cv2 as cv
import numpy as np
def func (value):
    pass
vid = cv.VideoCapture(0)
cv.namedWindow("Trackbars")
cv.createTrackbar("Hue max","Trackbars",179,179,func)

cv.createTrackbar("Sat max","Trackbars",255,255,func)

cv.createTrackbar("Val max","Trackbars",255,255,func)

cv.createTrackbar("Hue m","Trackbars",104,179,func)

cv.createTrackbar("Sat m","Trackbars",111,255,func)

cv.createTrackbar("Val m","Trackbars",110,255,func)    
blank = np.zeros((400,400,3),dtype="uint8")

# def draw(*maski):
#     for j,m1 in enumerate(maski):
#         for i,v in enumerate(m1):
#             if v==255:
#                 cv.circle(tram,(i,j),1,(0,255,0))

while True:
    istrue, fr = vid.read()
    fram = cv.flip(fr,1)
    frame = cv.resize(fram,(400,400))
    frame_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    hue_max = cv.getTrackbarPos("Hue max","Trackbars")
    sat_max = cv.getTrackbarPos("Sat max","Trackbars")
    val_max = cv.getTrackbarPos("Val max","Trackbars")
    hue_m = cv.getTrackbarPos("Hue m","Trackbars")
    sat_m = cv.getTrackbarPos("Sat m","Trackbars")
    val_m = cv.getTrackbarPos("Val m","Trackbars")
    mask = cv.inRange(frame_hsv,(hue_m,val_m,sat_m),(hue_max,val_max,sat_max))
    print(mask)
    median_b = cv.medianBlur(mask,3)
    cv.imshow("SFSF",frame)
    #cv.imshow("video",frame_hsv)
    cv.imshow("Mask",median_b)
    masked = cv.bitwise_and(frame,frame,mask=median_b)
    for j,m1 in enumerate(mask):
        for i,v in enumerate(m1):
            if v==255:
                cv.circle(frame,(i,j),1,(0,255,0))
    #cv.imshow("MASKED",masked)
   
    cv.imshow("Draw",frame)
    if (cv.waitKey(1) == ord('q')) :
        break