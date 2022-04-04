import cv2 as cv

img = cv.imread('photos/cats.jfif')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
# The threshold functions goes through each pixel and comapares to the threshold value
# if it is above to 150 it sets it to 255, and if it is below it is set to 0

# thresh is the binarized image
# threshhold is the passed threshold value 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding
adapative_threh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adapative Thresholding',adapative_threh)

cv.waitKey(0)