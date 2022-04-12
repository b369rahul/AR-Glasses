import cv2 as cv
import numpy as np

blank = np.zeros((400,400,3),dtype='uint8')  # height,width,color channels
cv.imshow("blank",blank)
# blank[:]= 250,0,0           # BGR
# cv.imshow("Blue",blank)

# blank[200:300 , 250:350] = 255,0,255         # first is height and second is width
# cv.imshow("colouring some",blank)

# cv.rectangle(blank, (0,100),(100,200),(0,250,100),thickness=10)      # the frame , starting ,ending cordinates, color,thickness 
# cv.imshow("Rectangle",blank)            # any negative value of thickness can be used for filling rectangle
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,250,0),thickness=3)
#cv.imshow("circle",blank)
# cv.line 
cv.putText(blank,"Helli",(100,200),cv.FONT_HERSHEY_TRIPLEX,1.2,(0,250,0),thickness=3)
cv.imshow("Hello",blank)
cv.waitKey(0)