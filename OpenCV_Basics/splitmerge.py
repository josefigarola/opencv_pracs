import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jfif')
cv.imshow('Gas',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank',blank)

# Split function separates the BGR colors
b,g,r = cv.split(img)

""" cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r) """
# Lighter pixels show there's far more concentration of the color
# Darker areas show there's little or no pixels

# Setting the color channels to only see those colors
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Images shapes
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge function combines the colors of the BGR splitted before
merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)

cv.waitKey(0)