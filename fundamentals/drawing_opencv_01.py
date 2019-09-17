'''
handle mouse events in OpenCV.
'''

import numpy as np 
import cv2

# Mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 40, (255,255,0), 5)

# Load an image
img = cv2.imread('Future-human-Face.png',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:        # wait until the 'Exc' key is pressed to stop capturing
        break

cv2.destroyAllWindows()