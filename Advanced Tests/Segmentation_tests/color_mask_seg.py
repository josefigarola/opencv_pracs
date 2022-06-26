''' 
Color Masking for segmentation
https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/
'''
from cv2 import COLOR_BGR2GRAY, COLOR_GRAY2BGR, COLOR_GRAY2BGRA
import matplotlib as plt
import numpy as np
import cv2 as cv

def color_mask_seg(img):
    ''' Preprocessing the Image '''
    # OpenCV default colorspace is BGR so we convert it to RGG
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # Next, we convert it to the HSV colorspace
    hsv_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2HSV)

    ''' Define the Color Range to be Detected '''
    # Define the RGB range for the color we want to detect. 
    # Use the OpenCV in range function to create a mask of all the pixels that fall within the range that we defined
    # It will later help to mask these pixels
    dark_blue = (90, 70, 50)
    light_blue = (128, 255, 255)
    # You can use the following values for green
    dark_green = (40, 40, 40)
    light_green = (70, 255, 255)

    ''' For RED Values'''
    # You can use the following values for red 
    # Boundary 1
    dark_red1 = (0, 100, 20)
    light_red1 = (10, 255, 255)
    # Boundary 2
    dark_red2 = (160, 100, 20) 
    light_red2 =  (179, 255, 255) 

    # Combine masks
    #lower_mask = cv.inRange(img, dark_red1, light_red1)
    #upper_mask = cv.inRange(img, dark_red2, light_red2)
    #red_full_mask = lower_mask + upper_mask

    # Apply mask
    mask = cv.inRange(hsv_img, dark_green, light_green)
#
    #result = img.copy()
    #result = cv.bitwise_and(result, result, mask=red_full_mask)
    #cv.imshow("Red",result)

    ''' Apply the Mask '''
    # Use the bitwise AND operation to apply our mask to the query image
    result = cv.bitwise_and(img, img, mask=mask)
    # Overlapping Frames
    gray = cv.cvtColor(img, COLOR_BGR2GRAY)
    gray2color = cv.cvtColor(gray, COLOR_GRAY2BGR)
    dst = cv.addWeighted(gray2color, 0.5, result, 1.0, 0.0)
    cv.imshow("Overlap Images", dst)
    cv.imshow("Color Mask Segmentation", result)

''' Reading image''' 
img = cv.imread('Computer_Vision\Tests\Segmentation_tests\photos\semaforo1.jpg')
cv.imshow('Image',img)

color_mask_seg(img=img)

cv.waitKey(0)
cv.destroyAllWindows()