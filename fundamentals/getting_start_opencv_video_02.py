'''
Capturing video from camera and save it.
'''

import numpy as np 
import cv2

cap = cv2.VideoCapture(0)                               # capture a frame from video file

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480), False)     # create the output with video setup parameters 
# last option is isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()                             # ret is returned with boolean value. If frame is read correctly, it will be True     
    if ret == True:
        #frame = cv2.flip(frame,0)                      # flip every frame in vertical direction        
        frame = cv2.flip(frame,1)                       # flip every frame in horizontal direction
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the flipped frame to grayscale, only used when the isColor option is set to False

        # write the flipped frame        
        # write the grayscale flipped frame
        out.write(frame)
        

        # Display the resulting frame
        cv2.imshow('frame', frame)        
        if cv2.waitKey(1) & 0xFF == ord('q'):           # cv2.waitKey(1) display a frame for 1ms, after that the frame is automatically closed.
            break
    else:
        break

# Release everything if job is finished
cap.release()           # not capture anymore
out.release()
cv2.destroyAllWindows()