import cv2 as cv
    # only works for live video

vid = cv.VideoCapture(0)  

def change_reso(width,height):
    # only works for live video
    vid.set(3,width)                        # in set 3 represents width 4 represents height
    vid.set(4,height)
change_reso(640,1280)
while True:
    istrue, frame = vid.read()         
    cv.imshow("Video",frame)               

    if ( cv.waitKey(10) & 0xFF )== ord('d'):      # used to quit video with any literal provide inside 
        break                                       # notice & is bitwise operator above

vid.release()
cv.destroyAllWindows()
