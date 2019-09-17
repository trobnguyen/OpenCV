'''
Capture video form camera and display it.
'''

import numpy as np 
import cv2

cap = cv2.VideoCapture(0)                               # capture a frame from camera
# cap.get(propId)                                       # access the frame properties 
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
if cap.isOpened() == True:
    print('The frame width and height are: %4dx%4d' %(cap.get(3), cap.get(4)))
    ret = cap.set(3,320)
    ret = cap.set(4,240)
    print('The frame width and height after modifying are: %4dx%4d' %(cap.get(3), cap.get(4)))
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()                         # ret is returned with boolean value. If frame is read correctly, it will be True         

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # convert the captured frame to grayscale image

        # Display the resulting frame
        cv2.imshow('frame',gray)                            # display the image            
        if cv2.waitKey(1) & 0xFF == ord('q'):   # wait until the 'q' key is pressed to stop capturing
            break

# When everything done, release the capture
cap.release()           # not capture anymore
cv2.destroyAllWindows()


