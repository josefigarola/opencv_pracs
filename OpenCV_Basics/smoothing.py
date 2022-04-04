import cv2 as cv

img = cv.imread('photos/libro.png')
cv.imshow('Libro',img)

# Averaging blur: Define a kernel window over a portion of an image
# The window will compute the pixel intensity of the center of the window
# as the average of the surrouding pixels
average = cv.blur(img,(7,7)) # The higher the window, the higher the intensity of the blur
cv.imshow('Average',average)

# Gaussian blur: Each surrounding pixels has a weight 
# and the avergae of product of the weight gives the value of the center one
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

# Median blur: Same thing as average but it finds the median of the surrounding pixels
# It is good to eliminate noise
# It is not meant for high kernel values
median = cv.medianBlur(img,3)
cv.imshow('Median blur',median)

# Bilateral blur: Applies bluring but retains the edges
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)