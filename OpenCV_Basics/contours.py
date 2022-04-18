""" This codes explains contours and threshold function """

import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jfif')
cv.imshow('Gas',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

""" blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges',canny) """

# threshold method binarizes an image 
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

# findcontours method takes the edges of the image and return 2 values:
# 1. Contours is a list of all coordinates o the contours.
# 2. Hierarchies is the herarchial representations of the contours

# The mode:
# RETR_LIST returns all the founded contours
# RETR_EXTERNAL returns extrernal contours
# RETRS_TREE returns all the heriarchical contours

# The method:
# CHAIN_APPROX_NONE does nothing
# CHAIN_APPROX_SIMPLES compresses all the contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

# Implementation of contours, worsk almost the same as canny edges
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)