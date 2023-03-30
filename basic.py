import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Greyscale', gray)

# blur image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# bordertype specifies how edges are handled when performing operations like convolution
# other options are constant border, replicating edge pixels etc
cv.imshow('Blur', blur)

# edge detection
canny = cv.Canny(blur, 125, 175)
# could've used normal image too, but additional blur helps weed out unnecessary edges, canny edge detection itself includes a blurring step

# image, threshold_min, threshold_max
# https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
# see hysteresis thresholding

# canny edge detection is a multi step algo

# first is noise reduction, edge detection is susceptible to noise, 5x5 gaussian kernel used to smoothen the image

# step two is edge detection, sobel kernel used in both directions (horizontal and vertical). edge gradient given by root(Gx^2 + Gy^2) and direction given by arctan(Gy/Gx)

# third step is non-maximum supression, basically removing any pipxels that are not edges. detrmined by checking if the point is the local maximum

# fourth and final step is Hysteris thresholding, using threshold values of intensity it is determined if detected edge is actually an edge or not
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# input, kernel(structuring element), iterations
# larger the kernel size, more is the region expansion
cv.imshow('Dilated', dilated)
# The dilation operation usually uses a structuring element for probing and expanding the shapes contained in the input image

# using dilation on an edge detected image, will enhance the edges(the region of interest of the image)

# general effect of dilation is expansion of brighter regions in the image
# although meant for binary images, greysacale implementations also exist 

# Check this out!!!
# https://homepages.inf.ed.ac.uk/rbf/HIPR2/dilate.htm


# Erosion
# opposite of dilation, dilating foreground pixels is equivalent to eroding background pixels
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# INTER_AREA is a weighted interpolation mostly used for downsizing
# 1/area is the weight per pixel. for fractional scaling, weight = portion of pixel in the window/area
# window size = area, for downsizng by a factor of 2, area = 2*2 = 4
cv.imshow('resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)