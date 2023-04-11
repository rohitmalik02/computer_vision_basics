import cv2 as cv
import numpy as np
# https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html

img = cv.imread('./Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape, dtype='uint8')

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)
# # can use either canny or thresh as the inputfor contour detection

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(len(contours))
# image, retrieval_method, approximation_method
# contours stores the contour coordinates, heirarchy is an array with the heirarchical info about the contours

# retrieval methods:
"""
In some cases, some shapes are inside other shapes. Just like nested figures. In this case, we call outer one as parent and inner one as child. This way, contours in an image has some relationship to each other. And we can specify how one contour is connected to each other, like, is it child of some other contour, or is it a parent etc. Representation of this relationship is called the Hierarchy

RETR_LIST returns all contours as is, no relationships/hierarchies considered

RETR_EXTERNAL returns only extreme/outer contours, nested contours ignored

RETR_CCOMP arranges all contours in a 2 level heirarchy, parent contours linked to their child contours, heirarchy levels are relative

RETR_TREE returns all contours along with absolute values of heirarchy levels, outermost contour is at level 0, complete result

* contour is a child only if it encapsulated/nested completely by another contour

* heirarchy array stores 4 values, next contour at the same level, previous contour at the same level, first_child of the contour, parent of the contour
"""

# approximation methods:
"""
CHAIN_APPROX_NONE is not memory efficient, stores all points of the contour.

for ex: non need to store all points of the line, simply storing the two end points will work too

CHAIN_APPROX_SIMPLE removes all the redundant points and compresses the contour
"""

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours', blank)

cv.waitKey(0)

# contours vs edges:
# edges are a local concept, which are found by computing difference between neighbouring pixels

# contours are obtained from edges, but their aim is to map boundaries of objects (in a larger sense) and then possibly arrange them in an hierarchy. They also need to be closed curves.