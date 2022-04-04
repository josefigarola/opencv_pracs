import os 
import cv2 as cv
import numpy as np

# Create a list of all the people in the images (Manually)
p = ['Ben Afflek', 'Elton John', 'Jerry Seinfiel', 'Madonna', 'Mindy Kaling']

# Create a list of all the people in the images by a given folder
people = []
for i in os.listdir(r'Face_Detec_Recog\Face_Recog_Photos'):
    people.append(i)

DIR = r'Face_Detec_Recog\Face_Recog_Photos'

# OpenCV Haar Cascade classifier algorithm
haar_cascade = cv.CascadeClassifier('Face_Detec_Recog\haar_face.xml')

# Loop over every folder in the base folder and loop over very image
# Grab the image and add that to the training set
features = [] # Image array of the faces
labels = [] # Whose faces does it belong to

def create_train():
    # Loop over very person in the people list
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        # Loop over every image in the folder
        for image in os.listdir(path):
            img_path = os.path.join(path,image)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, minNeighbors=4)
            # Grab faces region of interest
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                # Append to the features and labels list now that we have the ROI
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')
print('------Traininig done------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recgonizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features and labels lists
face_recgonizer.train(features,labels)

# Save yml and npy files for face_recognition.py
face_recgonizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)