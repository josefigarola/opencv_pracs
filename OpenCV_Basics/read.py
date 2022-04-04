# This program opens and reads images and videos

import cv2 as cv

# Read image
img = cv.imread('photos/newyork.jpg')

# Show the given image
cv.imshow('Cat',img)

# To capture a 
# capture = cv.VideoCapture('path')
#while True: 
#    isTrue, frame = capture.read()

#    cv.imshow('Video',frame)

#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break

#capture.release()

# Delay in ms for key to be pressed
cv.waitKey(5000)
# Close all windows opnened from opencv
cv.destroyAllWindows