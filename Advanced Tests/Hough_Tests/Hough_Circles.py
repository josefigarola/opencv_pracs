''' Hough Circles Transform Method'''
import cv2 as cv
from cv2 import COLOR_BGR2GRAY
import numpy as np

def Hough_Circles(gray, output):
    circles = cv.HoughCircles(
        gray, 
        cv.HOUGH_GRADIENT, 
        1,
        20, 
        param1=50, 
        param2=30, 
        minRadius=0, 
        maxRadius=0
        )

    detected_circles = np.uint16(np.around(circles))
    for (x, y ,r) in detected_circles[0, :]:
        cv.circle(output, (x, y), r, (0, 0, 0), 3)
        # cv.circle(output, (x, y), 2, (0, 255, 255), 3)

    cv.imshow('Hough Circles', output)

# Read Image
img = cv.imread('Computer_Vision\Tests\Hough_Tests\photos\circles.png')
cv.imshow('Circles', img)

# Copy Image
output = img.copy()

# Graysacle The Image
gray = cv.cvtColor(img, COLOR_BGR2GRAY)

# Blur Grayscale
gray = cv.medianBlur(gray, 5)

# Get Hough Circles
Hough_Circles(gray, output)

cv.waitKey(0)
cv.destroyAllWindows()