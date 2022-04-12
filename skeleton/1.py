import cv2 as cv
import mediapipe as mp
vid = cv.VideoCapture(0)

while True:
    ist, fram = vid.read()
    frame = cv.flip(fram,1)                   
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    result = mp.solutions.holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5).Holistic.process(frame)
    frame = cv.cvtColor((frame,cv.COLOR_RGB2BGR))
    mp.solutions.drawing_utils.draw_landmarks(frame,result.face_landmarks,mp.solutions.holistic.FACE_CONNECTIONS,
                                              mp.solutions.drawing_utils.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=1),
                                              mp.solutions.drawing_utils.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=1))


    cv.imshow("imgage",frame)
    if cv.waitKey(1) == ord('q'):
        break