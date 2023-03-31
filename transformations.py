import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('park', img)

# translation
def translate(img, x, y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)
# affine transformation, lines map to lines and PARALLEL LINES REMAIN PARALLEL
# projective transformation, lines map to lines and PARALLEL LINES MAY NOT BE PARALLEL

translated = translate(img, -100, 100)
# x -> right
# y -> down 
# -x -> left
# -y -> up
cv.imshow('park_translated', translated)

# rotation
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rot_mat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    # rotation point(coordinates of point about which the image wil be rotated), angle, scale
    dimensions = (width, height)
    return cv.warpAffine(img, rot_mat, dimensions)

rotated = rotation(img, 45)
# rotation is counter clockwise
rotated_2 = rotation(rotated, 45)
# although image is 90 degree rotated, some portion is cut off in the first rotation which can't be recoverd (hence ooutput is a weird skewed image)
# mess around with scale factor in the rotation function to retain all info while rotating (set to 0.5)
cv.imshow('park_rotated', rotated_2)

# flipping
flip = cv.flip(img, -1)
# 0 means flipping around the x-axis and positive value (for example, 1) means flipping around y-axis. Negative value (for example, -1) means flipping around both axes
cv.imshow('flip', flip)

cv.waitKey(0)