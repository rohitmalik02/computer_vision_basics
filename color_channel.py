import cv2 as cv
import numpy as np

img = cv.imread('./Photos/park.jpg')
cv.imshow('park', img)

b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)
# output is a greyscale image representing the color intensities

# to represent channels with their actual colors
m,n = img.shape[:2] #ignoring number of channels
blank = np.zeros((m,n), dtype='uint8')

blue = cv.merge([b, blank, blank])
cv.imshow('blue', blue)

green = cv.merge([blank, g, blank])
cv.imshow('green', green)

red = cv.merge([blank, blank, r])
cv.imshow('red', red)

merged = cv.merge([b, g, r])
cv.imshow('merged', merged)

cv.waitKey(0)