import cv2 as cv
import numpy as np

blank = np.zeros((480,640,3),dtype="uint8")

# def func (value):
#     pass
# cv.namedWindow("Trackbars")
# cv.createTrackbar("Hue max","Trackbars",179,179,func)

# cv.createTrackbar("Sat max","Trackbars",255,255,func)

# cv.createTrackbar("Val max","Trackbars",255,255,func)

# cv.createTrackbar("Hue m","Trackbars",104,179,func)

# cv.createTrackbar("Sat m","Trackbars",171,255,func)

# cv.createTrackbar("Val m","Trackbars",130,255,func)  
vid = cv.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,150)
#def func1(image):
 #   blur = cv.medianBlur(image,3)
  #  canny = cv.Canny(blur,125,175)
   # cv.imshow("DS",canny)

def mean (maski,image2):
    m=0
    n=0
    t=0
    for i,v in enumerate(maski):
        for j, val in enumerate(v):
            if val ==255 :
                m += i
                n += j
                t +=1
    if t !=0:
        a= m//t 
        b=n//t
        cv.circle(blank,(b,a),3,(0,255,0),thickness=3)


  
def func2 (image,image2):
    # hue_max = cv.getTrackbarPos("Hue max","Trackbars")
    # sat_max = cv.getTrackbarPos("Sat max","Trackbars")
    # val_max = cv.getTrackbarPos("Val max","Trackbars")
    # hue_m = cv.getTrackbarPos("Hue m","Trackbars")
    # sat_m = cv.getTrackbarPos("Sat m","Trackbars")
    # val_m = cv.getTrackbarPos("Val m","Trackbars")
    # low = np.array((hue_m,val_m,sat_m))
    # high = np.array((hue_max,val_max,sat_max))
    low = np.array((104,171,130))
    high =np.array((179,255,255))
    mask = cv.inRange(image,low,high)
    mean(mask,image2)
    #x1,y1,x2,y2 = cv.boundingRect(mask)
    #masked = cv.bitwise_and(image2,image2,mask=mask)
    #cv.imshow("MASKED",masked)
    #cv.imshow("Draw",image2)
    #cv.circle(image2,(b,a),3,(0,255,0))
while True:
    istte,frame= vid.read()
    flip = cv.flip(frame,1)
    hsv = cv.cvtColor(flip,cv.COLOR_BGR2HSV)
    func2(hsv,flip)
    #func1(flip)
    cv.imshow("asdsaf",flip)
    cv.imshow("DRAWING",blank)
    if cv.waitKey(1) == ord('q'):
        break
