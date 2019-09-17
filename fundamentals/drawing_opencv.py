'''
Drawing on an image.
'''

import numpy as np 
import cv2

# Create a black image
#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('Future-human-Face.png',1)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)     
# The cv2.line() takes the following parameters: where, start coordinates, end coordinates, color (bgr), line thickness.
img = cv2.rectangle(img, (15,25), (200,150), (0,0,255), 10)
img = cv2.circle(img, (100,63), 55, (0,255,0), -1)          # -1 to fill the shape

# Create polygon shape
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
img = cv2.polylines(img, [pts], True, (0,255,255), 3)
# where is the object being drawn to, the coordinates, should we "connect" the final and starting dot, the color, and again the thickness.

# Create ellipse shape
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Write a text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV Tuts!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image', img)
while (True):
    if cv2.waitKey(1) & 0xFF == ord('q'):   # wait until the 'q' key is pressed to stop capturing
        break
cv2.destroyAllWindows()