import cv2 as cv
import numpy as np

# Capture from computer camera
cam = cv.VideoCapture(0)
count = 0

while count<5:
    check, frame = cam.read()

    # Show video
    #cv.imshow('video', frame)

    cv.imwrite(f"Computer_Vision\Tests\TakePictures\photos\img{count}.jpg",frame)
    count += 1

    key = cv.waitKey(1)
    # If Esc key pressed break the process
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()