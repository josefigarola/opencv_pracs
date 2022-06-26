import cv2 as cv
import os 
import numpy as np
from math import sqrt

def euclidean_distance(x1,y1, x2,y2):
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Ditance = {dist}")
    return dist
    
img = cv.imread("Computer_Vision\Tests\DrawSquare\Photos\sem1.jpg")
img = cv.resize(img, (480, 480))
cv.imshow("Image", img)

# Coordinates of points
x1 = img.shape[1]//2-130
y1 = img.shape[0]//2-210

x2 = img.shape[1]//2-75
y2 = img.shape[0]//2-75

# Draw rectangle from given points
cv.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 1)

# Find center of drawn rectangle
centerX = (x1+x2)//2
centerY = (y1+y2)//2

# Draw center of rectangle
cv.circle(img, (centerX,centerY), 1, (255,0,255), 5)

# Draw center of bottom image 
cv.circle(img, (img.shape[1]//2,img.shape[0]//2+240), 1, (255,0,255), 5)

# Get euclidean distance
x1 = centerX 
y1 = centerY
x2 = 240
y2 = 480
dist1 = round(euclidean_distance(x1,y1, x2,y2),2)

#Draw line from center to point
cv.line(img, (centerX,centerY), (x2,y2), (255,0,255), 2)
#Write distance to image
cv.putText(img, str(dist1), (centerX,centerY), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 1)

# Draw circle center of image 
cv.circle(img, (img.shape[1]//2,img.shape[0]//2-130), 1, (0,0,0), 5)
# Draw line from center to point
cv.line(img, (img.shape[1]//2,img.shape[0]//2-130), (img.shape[1]//2,img.shape[0]//2+240), (0,0,0), 2)
dist2 = round(euclidean_distance(x1,y1, x2,y2),2)
cv.putText(img, str(dist2), (img.shape[1]//2,img.shape[0]//2-130), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
