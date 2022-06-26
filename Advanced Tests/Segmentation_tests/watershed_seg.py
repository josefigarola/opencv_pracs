''' Watershed segmentation code '''
from cv2 import GaussianBlur, morphologyEx, threshold
import matplotlib as plt
import numpy as np
import cv2 as cv

def watershed_seg(img):
    ''' Preprocessig the imga '''
    # Aplpy blur on src image
    blur = GaussianBlur(img, (3,3), 0)
    # Grayscale and binarize the image implementing otsu binarization
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    ret, thresh = threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    #cv.imshow('Binarized',thresh)

    ''' Flling/Removig empty spaces '''
    # Apply nose removal using morphologyEx function
    # MORPH_OPEN: useful for removing small objects
    # MPORH_CLOSE useful to remove small holes
    closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, (9,9), iterations = 1)
    #cv.imshow('Filling', closing)

    ''' Dilation '''
    dilated = cv.dilate(closing,(3,3),iterations=3)
    #cv.imshow("Dilated",dilated)

    ''' Euclidean distance '''
    # Apply distance transform on the binary image 
    # Compute euclidean distance
    dist = cv.distanceTransform(closing, cv.DIST_L2, 3)
    #cv.imshow("Euclidean",dist)
    # Apply a threshold
    # ret, thresh = cv.threshold(dist,0.1*dist.max(),255,0)

    ''' Find contours'''
    markers = np.zeros(dist.shape, dtype=np.int32)
    dist_8u = dist.astype('uint8')
    contours, _ = cv.findContours(dist_8u, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cv.drawContours(markers, contours, i, (i+1), -1)

    ''' Create markers '''
    markers = cv.circle(markers, (15,15), 5, len(contours)+1, -1)

    ''' Apply watershed function '''
    markers = cv.watershed(img, markers)
    img[markers == -1] = [0,0,255]
    cv.imshow("Watershed",img)

#img = cv.imread('Computer_Vision\Tests\Segmentation_tests\photos\semaforo2.jpg')
#watershed_seg(img=img)

#cv.waitKey(0)
#cv.destroyAllWindows()