import cv2 as cv
from cv2 import COLOR_BGR2GRAY
import numpy as np

# Read Image
img = cv.imread('Computer Vision\Tests\photos\circles.png')
cv.imshow('Circles', img)
print(img.shape[:2])

scale_percent = 220 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
cv.imshow('Resized', resized)

cv.waitKey(0)
cv.destroyAllWindows()