import cv2 as cv

def rescale_frame(frame,scale=0.5):
    # can be used for image,video or live video
    width = int(frame.shape[1] * scale)            # 0 for height and 1 for width
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
     
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# videocapture is a class which takes an argument of any video or webcam=0 and is initialised defining an obejct

vid = cv.VideoCapture(r"C:\Users\rb200\Pictures\Video Projects\video.mp4")   # file path/ 0 could be used for cam

# r is used for raw string to treat backslash (\) as a literal not an escape character

while True:
    istrue, frame = vid.read()         # istrue is used to check if it was able to capture frameḍ
    frame_resized = cv.resize(frame,(240,340))
    cv.imshow("Video",frame)            # same as in image
    cv.imshow("Resized Video",frame_resized)

    if ( cv.waitKey(10) & 0xFF )== ord('d'):      # used to quit video with any literal provide inside 
        break                                       # notice & is bitwise operator above

vid.release()
cv.destroyAllWindows()

# cv.waitkey(x) has 2 functions wait for x miliseconds and 
# If a key was pressed during that time it returns the key's ASCII code and stops
