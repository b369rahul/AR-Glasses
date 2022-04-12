import cv2 as cv
import numpy as np

import statistics
def func3(list):
    return tuple(list)

blank = np.zeros((480,640,3),dtype="uint8") + 255

def func (value):
    pass
cv.namedWindow("Trackbars")
cv.createTrackbar("Hue max","Trackbars",141,179,func)

cv.createTrackbar("Sat max","Trackbars",255,255,func)

cv.createTrackbar("Val max","Trackbars",255,255,func)

cv.createTrackbar("Hue m","Trackbars",104,179,func)

cv.createTrackbar("Sat m","Trackbars",171,255,func)

cv.createTrackbar("Val m","Trackbars",130,255,func)  
vid = cv.VideoCapture(0)
vid.set(3,480)
vid.set(4,640)
vid.set(10,150)
#def func1(image):
 #   blur = cv.medianBlur(image,3)
  #  canny = cv.Canny(blur,125,175)
   # cv.imshow("DS",canny)
point_x = []
point_y = []
i=0
def func2 (image,image2):
    global blank
    global point_x 
    global point_y 
    global i
    hue_max = cv.getTrackbarPos("Hue max","Trackbars")
    sat_max = cv.getTrackbarPos("Sat max","Trackbars")
    val_max = cv.getTrackbarPos("Val max","Trackbars")
    hue_m = cv.getTrackbarPos("Hue m","Trackbars")
    sat_m = cv.getTrackbarPos("Sat m","Trackbars")
    val_m = cv.getTrackbarPos("Val m","Trackbars")
    low = np.array((hue_m,val_m,sat_m))
    high = np.array((hue_max,val_max,sat_max))
    # low = np.array((94,151,100))
    # high =np.array((179,255,255))
    mask = cv.inRange(image,low,high)
    cv.imshow("mask",mask)
    blur = cv.medianBlur(mask,7)
    canny = cv.Canny(blur,175,256)
    #cv.imshow("CAnny",canny)
    contours, another =  cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    #cnts = []
    # for i,contour in enumerate(contours):
    #     #contour = np.array(contour,dtype = np.uint8)
    #     #cnts.append(contour)
    #     for con in contour:
    #         for c in con:
    #             cnts.append(c)
    if len(contours) !=0:
        cnt = sorted(contours, key = cv.contourArea, reverse = True)[0]
        ((x, y), radius) = cv.minEnclosingCircle(cnt)
        point_x.append(int(x))
        point_y.append(int(y))
        i+=1
        
# Or can use this for x and y
    # cnt = sorted(contours,key=cv.contourArea,reverse=True)[0]
    # abc = np.asarray(cnt,dtype=object)
    # a = np.average(abc,axis=0)
    # x  = int(a[0])
    #  y=int(a[1])
        

        
    #     z=np.array(cnts,np.uint8)   
    # #z=np.array(cnts,np.uint8)
    #     averaged = np.average(z,axis=0)
    #     x = int(averaged[0][0])
    #     y= int(averaged[0][1])
    #     point_y.append(y)
    #     point_x.append(x)

        
    #     #print(averaged)
    # for cnts in contours:
    #     if len(cnts) > 0:
    #         cnt_sorted = sorted(cnts,key=cv.contourArea,reverse=True)
    #         cnt = cnt_sorted[0]
    #         ((x, y), radius) = cv.minEnclosingCircle(cnt)
    #         blank[int(y)][int(x)] = (255,0,0)
    #         print(cnt)
    #print(contours)
    #point_x.append(int(x))
    #point_y.append(int(y))
    #print(points)
    
    #cv.circle(blank,(int(x),int(y)),1,(0,255,0),thickness=5)
    #blank[func3(point_y),func3(point_x)]=(0,255,0)
    #print(point_x,point_y)
            
    
            
    #x1,y1,x2,y2 = cv.boundingRect(mask)
    #masked = cv.bitwise_and(image2,image2,mask=mask)
    #cv.imshow("MASKED",masked)
    #cv.imshow("Draw",image2)
    #cv.circle(image2,(b,a),3,(0,255,0))
color = (0,255,0)
a=1
while True:
    istte,frame= vid.read()
    flip = cv.flip(frame,1)
    hsv = cv.cvtColor(flip,cv.COLOR_BGR2HSV)
    func2(hsv,flip)
    if i>1:
        if point_y[i-1]<=100 and (point_x[i-1]>=600 or point_x[i-1]<=60):
            color = (255,0,0)
            a = i-1
            blank = np.zeros((480,640,3),dtype="uint8") + 255
            # point_y.clear()
            # point_x.clear()            
            # i=0
        elif 350<=point_y[i-1]<=480 and (point_x[i-1]>=600 or point_x[i-1]<=60):
            color = (0,0,255)
            a=i-1
            blank = np.zeros((480,640,3),dtype="uint8") + 255
            # point_y.clear()
            # point_x.clear()            
            # i=0
        elif 250<=point_y[i-1]<=350 and (point_x[i-1]>=600 or point_x[i-1]<=60) :
            color = (0,255,0)
            a=i-1
            blank = np.zeros((480,640,3),dtype="uint8") + 255

        if i>=3:
            for i1, valu1 in enumerate(point_x):
                for i2,valu2 in enumerate(point_y):
                    if i1==i2 and i1>a  :
                        flip =cv.line(flip.copy(),(point_x[i1-1],point_y[i1-1]),(point_x[i1],point_y[i1]),color,thickness=3)
            # if point_x[i]>=550 and 250<= point_y[i] <=350:
            #     point_y.clear()
            #     point_x.clear()
            cv.line(blank,(point_x[i-1],point_y[i-1]),(point_x[i-2],point_y[i-2]),color,thickness=3)
            
                # blank = np.zeros((480,640,3),dtype="uint8") + 255
                # point_y.clear()
                # point_x.clear()            
                # i=0

    #func1(flip)
    joint = np.column_stack([flip,blank])
    cv.imshow("AIR DRAW",joint)
    #cv.imshow("Drawing image",flip)
    #cv.imshow("Drawwa",blank)
    if cv.waitKey(1) == ord('q'):
        break
