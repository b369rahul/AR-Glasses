import cv2 as cv

def rescale_frame(frame,scale=0.75):             
                                             # can be used for image,video or live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
     
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread(r"C:\Users\rb200\Pictures\Camera Roll\images.JPG",0)
img_rescaled = rescale_frame(img,0.5)
# r is used for raw string to treat backslash (\) as a literal not an escape character

cv.imshow("Image",img)
cv.imshow("Image 2",img_rescaled)

cv.waitKey(3000)

  
