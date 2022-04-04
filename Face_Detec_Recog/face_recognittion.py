import numpy as np
import cv2 as cv

# Using faces_train.py variables and files, this program uses validation images
# in order to detect a face and label the person in the given image

# Create a list of all the people in the images (Manually)
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfiel', 'Madonna', 'Mindy Kaling']

# OpenCV Haar Cascade classifier algorithm
haar_cascade = cv.CascadeClassifier('Face_Detec_Recog\haar_face.xml')

#features = np.load('Face_Detec_Recog\features.npy')
#labels = np.load('Face_Detec_Recog\labels.npy')

face_recgonizer = cv.face.LBPHFaceRecognizer_create()
face_recgonizer.read('face_trained.yml')

# Create a list of all the people in the images (Manually)
p = ['Ben Afflek', 'Elton John', 'Jerry Seinfiel', 'Madonna', 'Mindy Kaling']

img = cv.imread(r'Face_Detec_Recog\Face_Recog_Validation\ben_afflek\1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Unidentify Person',gray)

# Work over grayscale image and determine minimum neighbors
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

# Loop over the image and draw a rectangle over the detected faces
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recgonizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img,str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 0.75, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)