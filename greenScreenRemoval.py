import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('original.avi', fourcc, 20.0, (640,  480))
pro = cv.VideoWriter('new.avi', fourcc, 20.0, (640,  480))
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_green = np.array([0, 80, 0])     ##[R value, G value, B value]
    upper_green = np.array([130, 245, 185])
    mask = cv.inRange(hsv, lower_green, upper_green)
    mask_inv = cv.bitwise_not(mask)
    bg = cv.bitwise_and(frame, frame, mask=mask)
    fg = cv.bitwise_and(frame, frame, mask=mask_inv)

    # Display the resulting frame
    cv.imshow('frame', frame)
    cv.imshow('fg', fg)
    # write the frames
    out.write(frame)
    pro.write(fg)
    
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()