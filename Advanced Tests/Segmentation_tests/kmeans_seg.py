''' 
K-Means Method for segmentation
https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/
'''
import matplotlib as plt
import numpy as np
import cv2 as cv
from sympy import im

''' Function to segment image with K value '''
def K_means(img, Kvalue):
    ''' Preprocessing the Image ''' 
    # Preprocess the image by converting it to the RGB color space
    # Reshape it along the first axis to convert it into a 2D vector 
    # i.e. if the image is of the shape (100,100,3) (width, height, channels) 
    # then it will be converted to (10000,3). Next, convert it into the float datatype
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    twoDimage = img.reshape((-1,3))
    twoDimage = np.float32(twoDimage)

    ''' Defining Parameters ''' 
    # Define the criteria by which the K-means algorithm is supposed to cluster pixels
    # The ‘K’ variable defines the no of clusters/groups that a pixel can belong to 
    # (You can increase this value to increase the degree of segmentation)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = Kvalue
    attempts=10

    ''' Apply K-Means '''
    # The K variable randomly initiates K different clusters and the ‘center’ variable defines the center of these clusters
    # The distance of each point from these centers is computed and then they are assigned to one of the clusters 
    # Then they are divided into different segments according to the value of their ‘label variable'
    ret,label,center=cv.kmeans(twoDimage,K,None,criteria,attempts,cv.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape((img.shape))

    cv.imshow("K Means = " + str(K), result_image)

''' Reading image''' 
img = cv.imread('Computer_Vision\Tests\Segmentation_tests\photos\_beach.jpg')
cv.imshow('Image',img)

''' Apply different values for K-Means'''
K = 8 # Greater values segment more colors
K_means(img=img, Kvalue=K)
cv.waitKey(0)
cv.destroyAllWindows()