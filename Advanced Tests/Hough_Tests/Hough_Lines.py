''' Hough Lines Transform Method'''
import cv2 as cv
from cv2 import COLOR_BGR2GRAY
import numpy as np

def Hough_Lines(gray,canny_edges):
    # Input edge image, Distance resolution in pixels, Angle resolution in radians
    lines = cv.HoughLines(canny_edges, 1, np.pi / 180, 200)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        
        # x1 stores the rounde off valu of (r*cos(theta) - 1000*sin(theta))
        x1 = int(x0 + 1000 * (-b))
        # y1 stores the rounde off valu of (r*sin(theta) + 1000*cos(theta))
        y1 = int(y0 + 1000 * (a))
        # x1 stores the rounde off valu of (r*cos(theta) + 1000*sin(theta))
        x2 = int(x0 - 1000 * (-b))
        # y1 stores the rounde off valu of (r*sin(theta) - 1000*cos(theta))
        y2 = int(y0 - 1000 * (a))

        cv.line(img, (x1,y1), (x2, y2), (0,0,255), 2)
        cv.imshow('Hough Lines', img)


# Read Image
img = cv.imread('Computer_Vision\Tests\photos\sudoku.png')
cv.imshow('Sudoku', img)

# Graysacle The Image
gray = cv.cvtColor(img, COLOR_BGR2GRAY)

# Get Canny Edges
canny_edges = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny_edges)

# Get Hough Lines
Hough_Lines(gray=gray, canny_edges=canny_edges)

cv.waitKey(0)
cv.destroyAllWindows()