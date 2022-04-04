import cv2 as cv
import numpy as np

img = cv.imread('photos/ny.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Laplacian
# Computes to gradients of the grayscale image generating positive and negative slopes
# pixels cant have neg values, therefore the absolute value of the image to then
# convert it to uint8
lap = cv.Laplacian(gray, cv.CV_64F)
lap =np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
# Computs gradients into directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Sobel X',sobelx)
cv.imshow('Combined Sobel ',combined_sobel)

# Canny (comparison purpose)
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)