import cv2

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
    else:
        print("frame is null")