''' Setup your camera in OpenCV with ¨Python or C++
    Show video from camera
    Split in 3 windows the 3 layers of color, RGB '''
import cv2 as cv
import numpy as np

# Capture from computer camera
cam = cv.VideoCapture(0)

while True:
    check, frame = cam.read()

    # Show video
    cv.imshow('video', frame)

    cv.imwrite("Computer_Vision\Tests\TakePictures\photos",frame)

    # Function split to split BGR colors
    B, G, R = cv.split(frame)

    # Option 1
    ''' cv.imshow("red",R)
    #cv.imshow("green",G)
    #cv.imshow("blue",B) '''

    # Option 2
    '''b, g, r = cv.split(frame)
    zeros = np.zeros(frame.shape[:2], dtype="uint8")

    cv.imshow("RED",cv.merge([zeros, zeros, r]))
    cv.imshow("BLUE",cv.merge([b, zeros, zeros]))
    cv.imshow("GREEN",cv.merge([zeros, g, zeros]))'''

    # Option 3
    # Creating blank image
    blank = np.zeros(frame.shape[:2], dtype='uint8')

    blue = cv.merge([B,blank,blank])
    green = cv.merge([blank,G,blank])
    red = cv.merge([blank,blank,R])

    #cv.imshow('Blue', blue)
    #cv.imshow('Green', green)
    #cv.imshow('Red', red)


    key = cv.waitKey(1)
    # If Esc key pressed break the process
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()