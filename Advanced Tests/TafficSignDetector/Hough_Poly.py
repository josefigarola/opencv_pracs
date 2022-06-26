from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2 as cv

def Hough_Polygons(img,output):

    # Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Converting image to a binary image
    # (black and white only image).
    _,thresh= cv.threshold(gray, 135, 255, cv.THRESH_BINARY)
    cv.imshow("thesh",thresh)
 
    # Detecting shapes in image by selecting region
    # with same colors or intensity.
    contours,_=cv.findContours(thresh, cv.RETR_TREE,
                                cv.CHAIN_APPROX_SIMPLE)

    # Searching through every region selected to
    # find the required polygon.
    for cnt in contours :
        area = cv.contourArea(cnt)

        # Shortlisting the regions based on there area.
        if area > 400:
            approx = cv.approxPolyDP(cnt,
                                    0.009 * cv.arcLength(cnt, True), True)

            # Checking if the no. of sides of the selected region is 7.
            if(len(approx) >= 4):
                cv.drawContours(output, [approx], 0, (0, 0, 255), 3)

    # Showing the image along with outlined arrow.
    cv.imshow('Hough Polygons', output)

    return img