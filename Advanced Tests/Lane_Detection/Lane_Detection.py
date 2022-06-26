from cv2 import line
import matplotlib as plt
import numpy as np
import cv2 as cv
import os

''' Highway Lane Detection '''
def line_detection(frame):
    ''' Region of Interest Function'''
    def roi(img,vertices):
        # Make an image-shape mask
        mask = np.zeros_like(img)
        # Fill polygon with the roi points
        cv.fillPoly(mask,vertices,255) 
        # Cropp the roi image
        masked_image=cv.bitwise_and(img,mask)
        #cv.imshow("Masked",masked_image)
        return masked_image

    ''' Preprocessing the image '''
    def preprocess(img):
        height = img.shape[0]
        width = img.shape[1]

        # Video 3
        #roi_vertices = [(0,height), (5.7*width/10,6*height/10),(width,height)]
        # Video 4
        #roi_vertices = [(0,height),(5.7*width/10,6.8*height/10),(width,height)]
        # Video 10
        roi_vertices = [(0,height),(5*width/10,6.8*height/10),(width,height)]
        # Video tests
        #roi_vertices = [(0,height),(width/10,height/10),(1*width,2*height)]

        # Grayscale the frame
        gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
        # Get edges
        canny = cv.Canny(gray,100,150)
        # Eroded func to eliminate noise
        #eroded = cv.erode(canny, (3,3), iterations=1)
        # Dilate image to get better edges
        dilated = cv.dilate(canny, (7,7), iterations=3)
        cv.imshow("Edges",dilated)
        # Get the region of interest
        cropped = roi(dilated,np.array([roi_vertices],np.int32))
        return cropped

    ''' Drawing Hough Lines '''
    def draw_hough_lines(img,lines):
        img = np.copy(img)
        # Create a blank image
        blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
        for line in lines:
            for x1,y1,x2,y2 in line:
                # draw hough lines on blank image
                cv.line(blank_image,(x1,y1),(x2,y2),(255,0,255),thickness=7)
        # Overlap the images (img and blank)
        img = cv.addWeighted(img,0.8,blank_image,1,0.0)
        return img

    # Get the preprocess on a cropped variables
    cropped= preprocess(img=frame)
    # Get and draw hough lines from the cropped image
    try:
        #lines = cv.HoughLinesP(cropped,rho=6,threshold=60,theta=np.pi/180,minLineLength=50,maxLineGap=150,lines=np.array([]))
        lines = cv.HoughLinesP(
            cropped,
            rho=8,
            threshold=1,
            theta=np.pi/180,
            minLineLength=300,
            maxLineGap=0,
            lines=np.array([])
            )
        # Draw the hough lines
        img = draw_hough_lines(frame,lines)
        # Return lines in the original img
        return img
    except:
        pass

''' Capture Video '''
def Capture(vid,cap):

    # Save the video
    frame_width = int(vid.get(3))
    frame_height = int(vid.get(4))
    
    size = (frame_width, frame_height)

    result = cv.VideoWriter('Computer_Vision\Tests\Lane_Detection\Lane_1.avi', 
                            cv.VideoWriter_fourcc(*'MJPG'),
                            10, size)
    while True:
        ret,frame = vid.read()

        if ret == True:
            try:
                # Preprocess noise bluring
                frame = cv.GaussianBlur(frame,(3,3),0)
                # Detect lines
                lines_frame = line_detection(frame=frame)
                # Save the video
                result.write(lines_frame)
            
                cv.imshow('Lane detection',lines_frame)
                cv.imshow('Video',frame)
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
    vid = cv.VideoCapture('Computer_Vision\Tests\Lane_Detection\Videos\Video10.mp4')
    # Capture the video and get Lane Detection
    cap = Capture(vid=vid,cap=cap)
'''

img = cv.imread("Computer_Vision\Puzzlebot\GetLine\photos\p1.jpeg")
# Preprocess noise bluring
frame = cv.GaussianBlur(img,(3,3),0)
# Detect lines
lines_frame = line_detection(frame=frame)
cv.imshow('Lane detection',lines_frame)

cv.waitKey(0)
cv.destroyAllWindows()