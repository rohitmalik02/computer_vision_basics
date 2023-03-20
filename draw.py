import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Python follows B,G,R and not RGB
# paint image a certain color
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

# drawing a square
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Square', blank)

# drawing a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=-1)
# without the thickness, only outline
# thickness -1 -> fills up the shape with specified color
cv.imshow('Rectangle', blank)

# drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255))
# canvas, anchor_point_of_center, radius, color, thickness
cv.imshow('Circle', blank)

# drawing a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.line(canvas, starting_point, ending_point)
cv.imshow('Line', blank)

# writing text
cv.putText(blank,  'Hello', (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 0), 2)
# canvas, text, anchor_point_of_bottom_left_corner, font, font_scale, color, thickness

cv.imshow('Text', blank)

cv.waitKey(0)