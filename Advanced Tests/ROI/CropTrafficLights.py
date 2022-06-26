import cv2 as cv
import os

if __name__ == '__main__':
    #DIR = r"Computer_Vision\Tests\ROI\ROINeg"
    #DIR2 = r"Computer_Vision\Tests\ROI\CropROI"
    DIR= "Computer_Vision\Tests\ROI\Photos"
    showCrosshair = False
    fromCenter = False


    # Read images from folder and save them un images array
    images = []
    for filename in os.listdir(DIR): # Read the file
        img = cv.imread(os.path.join(DIR,filename)) # Read the images from the file
        if img is not None:
            images.append(img) # Append the images to the list

    print("Crop Traffic Lights")

    # Crop ROI from every image
    for i in range(len(images)):
        img = images[i]
        # Select ROI
        r = cv.selectROI("Image", img, fromCenter, showCrosshair)
        # Crop image
        imgCrop = img[int(r[1]):int(r[1]+r[3]), 
                      int(r[0]):int(r[0]+r[2])]

        cv.imwrite(f"Computer_Vision\Tests\ROI\ROINeg\Image{i}.jpg", imgCrop)

    '''
    # Change the name from a file
    i = 0
    for filename in os.listdir(DIR2):
        os.rename(os.path.join(DIR2,filename), os.path.join(DIR2, "img"+str(i)+".jpg"))
        i += 1
    '''
