import cv2 as cv
import numpy as np

img = cv.imread('./Photos/cats.jpg')
cv.imshow('cats', img)

# averaging
average = cv.blur(img, (7,7))
cv.imshow('average', average)

# gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gaussian blur', gauss)
# image, kernel_size, sigmaX
# sigmaX - standard deviation in X direction; if 0, calculated from kernel size
# sigmaY - standard deviation in Y direction; if sigmaY is None, sigmaY is taken to equal sigmaX

# sigma will decide the weights, smaller the sigma, larger will be the weights towards the center



# median blur
# less sensitive to noise than simple averaging or gaussian blur
# but then the blurring effect is not as natural as say gaussian which is quite similar to how our eyes perceive the world
median = cv.medianBlur(img, 7)
cv.imshow('median', median)
# kernel size is one dimensional here instead of 2d like in case of gaussian blur or averaging, because they contain weights that need to be defined for the 2d filter, median on the other hand is a non linear filter which will be replacing the pixel value by the median value, so there is no need to waste space by storing a 2d size, 1d dimension is enough, the function automatically computes median across 'size' number of axes


# bilateral blurring
bilateral = cv.bilateralFilter(img, 5, 45, 55)
# source, d(dimeter/size of pixel neighbourhood), sigmaColor(variance/filter sigma in the color space, neighbourhood size in the color space), sigmaSpace(filter sigma in the coordinate space, used only when d is negative, else neighbourhood size is defined by d)
cv.imshow('bilateral', bilateral)
# other blurring techniques simply average/blur out the image, including edges
# bilateral is kind of a content aware blurring technique where it blurs the insignificant parts of the image and tries to retain/preserve some edge information

# https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed

cv.waitKey(0)