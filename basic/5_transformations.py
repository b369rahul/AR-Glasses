import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\photo.JPG")
# Resize
resized = cv.resize(img,(400,400),interpolation=cv.INTER_AREA)   # inter_cubic for enlarging but slow and linear for fast
cv.imshow("resized",resized)

# Translation

def translation (image,x,y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1],image.shape[0])
    return cv.warpAffine(image,trans_mat,dimensions)
# +x --> right     +y -->bottom
translated = translation(resized,100,100)
cv.imshow("translated",translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(resized, 45)
cv.imshow('Rotated', rotated)

# FLipping
flip = cv.flip(resized,1)        # 0 -> accross x axis 1 -> accross y axis -1 -> accross both axis  
cv.imshow("flipped",flip)
cv.waitKey(0)