''' 
Contour Detection for segmentation
https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/
'''
import matplotlib as plt
import numpy as np
import cv2 as cv
from sympy import im

def cnt_seg(img):
    # Resize the image
    img = cv.resize(img,(256,256))

    ''' Preprocessing the Image '''
    # 1. Convert the image to grayscale
    gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    # 2. Compute the threshold of the grayscale image (the pixels above the threshold are converted to white otherwise zero)
    _, thresh = cv.threshold(gray, np.mean(gray), 255, cv.THRESH_BINARY_INV)
    # 3. Apply canny edge detection to the thresholded image before finally using the ‘cv.dilate’ function to dilate edges detected
    edges = cv.dilate(cv.Canny(thresh,0,255),None)

    ''' Detecting and Drawing Contours ''' 
    # 1. Use the OpenCV find contour function to find all the open/closed regions in the image and store (cnt). 
    #    Use the -1 subscript since the function returns a two-element tuple.
    # 2. Pass them through the sorted function to access the largest contours first.
    # 3. Create a zero pixel mask that has equal shape and size to the original image.
    # 4. Draw the detected contours on the created mask.
    cnt = sorted(cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2], key=cv.contourArea)[-1]
    mask = np.zeros((256,256), np.uint8)
    masked = cv.drawContours(mask, [cnt],-1, 255, -1)

    ''' Segmenting the Regions '''
    # In order to show only the segmented parts of the image, we perform a bitwise AND operation on the original image (img) 
    # and the mask (containing the outlines of all our detected contours)
    # Finally, Convert the image back to RGB to see it segmented(while being comparable to the original image).
    dst = cv.bitwise_and(img, img, mask=mask)
    segmented = cv.cvtColor(dst, cv.COLOR_BGR2RGB)

    cv.imshow('Contours Segmentation',segmented)

''' Reading image''' 
img = cv.imread('Computer_Vision\Tests\Segmentation_tests\photos\city.jpg')
cv.imshow('Image',img)

cnt_seg(img=img)

cv.waitKey(0)
cv.destroyAllWindows()