'''
Display a color image using matplotlib
OpenCV follows BGR order, while matplotlib likely follows RGB order.
'''

import numpy as np 
import cv2
from matplotlib import pyplot as plt 

# Load an color image
img = cv2.imread('Future-human-Face.png',1)
b, g, r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121); plt.imshow(img)    # expects distorted color   #subplot(nrows, ncols, index, **kwargs)
'''121 means 1 row, 2 columns, at 1st index'''
plt.subplot(122); plt.imshow(img2)   # expect true color
plt.show()

cv2.imshow('bgr image',img)     # expects true color
cv2.imshow('rgb image',img2)    # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()

