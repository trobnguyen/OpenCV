'''Load a grayscale image and save it'''

import numpy as np 
import cv2
import os

# find absolute file path
#file_path = os.path.abspath("Future-human-Face.png")
file_path = os.path.abspath("messi5.jpg")


"""
cv2.IMREAD_COLOR = 1        : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE = 0    : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED = -1   : Loads image as such including alpha channel
"""

# Load an color image in grayscale
#img = cv2.imread('Future-human-Face.png',0)
img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)      # read a specific image file in the working directory.

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
"""
cv2.WINDOW_AUTOSIZE : default flag
cv2.WINDOW_NORMAL   : window is resizable, it will be helpful when image is too large in dimension and adding track bar to windows.
"""
cv2.imshow('image',img)     # 'image' is the window name
cv2.waitKey(0)              # wait until the key '0' is pressed
cv2.destroyAllWindows()     # destroy all created windows
"""
cv2.destroyWindow() : destroy the specifice window with the exact window name as the argument.
"""
cv2.imwrite('face_gray.jpg',img)