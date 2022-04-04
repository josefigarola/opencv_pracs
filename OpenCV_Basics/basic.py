""" This program shows the main opencv functions """

import cv2 as cv

# Read image
img = cv.imread('photos/ny.jpg')

# Show the given image
cv.imshow('Caratula',img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# Blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade (Edges present in the image)
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges',canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=2)
cv.imshow('Dilated',dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded',eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

# Delay in ms for key to be pressed
cv.waitKey(0)
# Close all windows opnened from opencv
cv.destroyAllWindows