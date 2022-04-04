# This program opens and reads images and videos
# to the rescale the frame from this files

import cv2 as cv

# Read image
img = cv.imread('photos/cat2.jfif')

# Show the given image
cv.imshow('Cat',img)

# Function to rescale an images, videos or live videos
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Function to change the resolution of the video
# This method works ONLY for live videos
""" def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height) """

resized_image = rescaleFrame(img,scale=5.0)
cv.imshow('Cat resized',resized_image)

# To capture a video and resize
# capture = cv.VideoCapture('path')
#while True: 
#    isTrue, frame = capture.read()

#    frame_resized = rescaleFrame(frame)

#    cv.imshow('Video',frame)
#    cv.imshow('Video resized',frame_resized)

#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break

#capture.release()
#cv.destroyAllWindows

# Delay in ms for key to be pressed
cv.waitKey(5000)
# Close all windows opnened from opencv
cv.destroyAllWindows