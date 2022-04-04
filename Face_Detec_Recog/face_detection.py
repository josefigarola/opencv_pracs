# Face detection vs Face Recognition
""" Face detection merely detects the presence of a face in an image,
while face recognition involves identifying whose face it is.

A classifier is essentially and algorithm that decides wheter a given image is positive
or negative,wheter a face is present or not. OpenCV comes with pretrained classifiers

Two main classifiers: Haar Cascades & Local Binary Patterns

https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml 

Haar Cascade are sensitive to noise in an image, so it is to be expected no to be 100 percent efficient """

import cv2 as cv

img = cv.imread('Face_Detec_Recog\Face_Detect_Photos\people2.jpg')
#cv.imshow('People',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Resized People Image',gray)

# OpenCV Haar Cascade classifier algorithm
haar_cascade = cv.CascadeClassifier('Face_Detec_Recog\haar_face.xml')

# Work over grayscale image and determine minimum neighbors
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

# Loop over the image and draw a rectangle over the detected faces
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces',img)

cv.waitKey(0)