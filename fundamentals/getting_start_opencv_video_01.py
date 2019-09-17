'''
Playing Video from file.
'''

import numpy as np 
import cv2

cap = cv2.VideoCapture('MVI_0043.avi')                  # capture a frame from video file

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()                             # ret is returned with boolean value. If frame is read correctly, it will be True         

    try:
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # convert the captured frame to grayscale image

        # Display the resulting frame
        cv2.imshow('frame',gray)                            # display the image     
        time = 25                                           # video speed can be modified at here. 25 milliseconds will be OK in normal cases.
        if cv2.waitKey(time) & 0xFF == ord('q'):            # wait until the 'q' key is pressed to stop capturing
            break        
    except:
        break
    
# When everything done, release the capture
cap.release()           # not capture anymore
cv2.destroyAllWindows()

