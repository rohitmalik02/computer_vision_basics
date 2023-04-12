import cv2 as cv
import matplotlib.pyplot as plt

img =  cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to l*a*b
# l -> lightness, a,b -> chromaticity
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

"""
HSV/HSL vs L*A*B

Both HSV and L*A*B were introduced to mimic how humans perceive colors. HSV/HSL separates colours from intensity channels, while this is better than RGB, but still not perfect. The gamut size is smaller than L*A*B and the computatations required are greater than RGB.

The L component of the HSL and the V component of HSV describe the brightness of a color relative to a base color. If this base color is blue you will get a darker color than if this base color is yellow, HSL and HSV are very useful if you need to create a lighter or darker version of a color but aren't very useful if you want to know how bright a color is.

L*A*B covers more colours, much more than RGB plus it tracks even the smallest changes in colors just like our eyes do. It is more accurate and more importantly immune to external like light intensity changes that can create incoherent color reproduction like in case of RGB or CMYK. Also it separates the colour from luma(brightness).

A perceptual uniform color space ensures that the difference between two colors (as perceived by the human eye). It is proportional to the Euclidian distance within the given color space

"""

# opencv follows BGR, but outside the library such as matplotlib, conventional RGB format is used
# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)