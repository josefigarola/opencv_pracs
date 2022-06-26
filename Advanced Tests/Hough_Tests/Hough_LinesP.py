''' Probabilistic Hough Lines Transform Method'''
import cv2 as cv
import numpy as np

def Hough_LinesP(edges,img):
    lines = cv.HoughLinesP(
        edges,
        1,
        np.pi/180,
        100,
        minLineLength=100,
        maxLineGap=10
        )

    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv.imshow('Hough Lines P', img)

# Read Image
img = cv.imread('Computer_Vision\Tests\Hough_Tests\photos\\highway2.jpg')
cv.imshow('Highway',img)

# Grayscale Image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Get Canny Edges
canny_edges = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny_edges)

# Hough Lines Probabilistiic method
Hough_LinesP(edges=canny_edges,img=img)

cv.waitKey(0)
cv.destroyAllWindows()