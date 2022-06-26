from cv2 import COLOR_BGR2GRAY, COLOR_GRAY2BGR, COLOR_GRAY2BGRA
import matplotlib as plt
import numpy as np
import cv2 as cv

import color_segment as cm
import Hough_Circles as HC
import Hough_Poly as HP

def detect_sign(img):
    # Apply blur to denoise
    img = cv.GaussianBlur(img, (5,5), 0)

    # Get color segmentation
    blue_segment = cm.color_mask_seg(img=img)

    # Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Get canny edges
    canny = cv.Canny(blue_segment, 255, 255)
    cv.imshow("Canny", canny)

    # Hough Circle Transform
    try:
        hough_C = HC.Hough_Circles(canny, img)
    except:
        pass

    # Get Polygons
    try:
        hough_P = HP.Hough_Polygons(img=blue_segment,output=img)
    except:
        pass


''' Capture Video '''
def Capture(vid,cap):
    while True:
        ret,frame = vid.read()

        if ret == True:
            try:
                cv.imshow('Video',frame)
                # Detect traffic lughts
                detect_sign(img=frame)
            except: 
                pass

        elif ret == False:
            print("End of video")
            break

        key = cv.waitKey(1)
        # If Esc key pressed break the process
        if key == 27:
            # Dont show video anymore
            cap = False
            break

    vid.release()
    cv.destroyAllWindows()
    return cap

''' Main Code '''
'''
cap = True
while cap == True:
    # Loop over and over video
    vid = cv.VideoCapture(
        r'Computer_Vision\Tests\TafficSignDetector\Videos\Video1.mp4'
        )
    # Capture the video and get Lane Detection
    cap = Capture(vid=vid,cap=cap)
'''

img = cv.imread("Computer_Vision\Tests\TafficSignDetector\photos\sign1.png")
detect_sign(img)
cv.waitKey(0)
cv.destroyAllWindows()
