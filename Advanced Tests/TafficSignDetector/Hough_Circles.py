import cv2 as cv
from cv2 import COLOR_BGR2GRAY
import numpy as np

def Hough_Circles(gray, output):
    circles = cv.HoughCircles(
        gray, 
        cv.HOUGH_GRADIENT, 
        1,
        30, 
        param1=50, 
        param2=10, 
        minRadius=35, 
        maxRadius=35
        )

    detected_circles = np.uint16(np.around(circles))
    for (x, y ,r) in detected_circles[0, :]:
        cv.circle(output, (x, y), r, (0, 255, 255), 3)
        #cv.circle(output, (x, y), 2, (0, 255, 255), 3)

    cv.imshow('Hough Circles', output)
    return output