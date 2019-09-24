'''
HSV color value detection
'''

import numpy as np 
import cv2

# global variables
x_co, y_co = 30, 30
font = cv2.FONT_HERSHEY_SIMPLEX
#s = np.uint8([[[0, 0, 0]]])

# create min and max filter
min_filt = np.array([0, 0, 0])
max_filt = np.array([179, 255, 255]) 

# get frame source from webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image', on_mouse)
cv2.namedWindow('res', cv2.WINDOW_AUTOSIZE)

# Mouse callback function
def on_mouse(event,x,y,flags,param):
    global x_co, y_co, font, frame, frame_stored, s, hsv, res, mask

    if event == cv2.EVENT_LBUTTONDOWN:        
        x_co, y_co = x,y
        s = hsv_get(x_co,y_co)
        H_val = s[0][0][0]
        S_val = s[0][0][1]
        V_val = s[0][0][2]

        # define range of mask
        lower_filt = np.array([H_val-20, S_val-70, V_val-70])
        upper_filt = np.array([H_val+20, S_val+70, V_val+70])  

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_filt, upper_filt)   

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame_stored, frame_stored, mask= mask) 
        
    #elif event == cv2.EVENT_LBUTTONUP:        
        #frame = cv2.putText(frame,'H:'+str(s[0][0][0])+', S:'+str(s[0][0][1])+', V:'+str(s[0][0][2])+', (X,Y):'+str(x_co)+','+str(y_co),(x_co,y_co),font,0.5,(55,25,255),1,cv2.LINE_AA)

    return mask
        
def hsv_get(x,y):
    colorsB = frame[y,x,0]
    colorsG = frame[y,x,1]
    colorsR = frame[y,x,2]   
    bgr_color = np.uint8([[[colorsB, colorsG, colorsR]]])
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    return hsv_color   

# Take each frame
_, frame = cap.read()
_, frame_stored = cap.read()

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, min_filt, max_filt)   

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame_stored, frame_stored, mask= mask) 

while(1):  
    cv2.imshow('image', frame)  
    cv2.imshow('res', res)  
    #cv2.imshow('hsv', hsv)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
    