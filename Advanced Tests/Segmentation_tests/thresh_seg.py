''' 
Thresholding for segmentation
https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/
'''
import matplotlib as plt
import numpy as np
import cv2 as cv
from sympy import im

def thresh_seg(img):
    # filter_image function
    def filter_image(image, mask):
        r = image[:,:,0] * mask
        g = image[:,:,1] * mask
        b = image[:,:,2] * mask
        return np.dstack([r,g,b])

    ''' Preprocessing the Image ''' 
    # Convert the image to the RBG color space from BGR in order to finally convert it to grayscale.
    img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img_gray=cv.cvtColor(img_rgb,cv.COLOR_RGB2GRAY)

    ''' Segmentation Process '''
    # 1. Create a “filter_image” function that multiplies the mask (created in the previous section) 
    #    with the RGB channels of our image. Further, they are concatenated to form a normal image.
    # 2. Next, we calculate the threshold (thresh) 
    #    for the gray image and use it as a deciding factor 
    #    i.e. values lying below this threshold are selected and others are discarded. This creates a mask-like (img_otsu) image that can later be used to segment our original image.
    # 3. Finally, apply the “filter_image” function on the original image(img) 
    #    and the mask formed using thresholding (img_otsu)
    _, thresh = cv.threshold(img_gray, np.mean(img_gray), 255, cv.THRESH_OTSU)
    img_otsu  = img_gray < thresh
    filtered = filter_image(img, img_otsu)

    cv.imshow("Threshold Segmentation", filtered)

''' Reading image''' 
img = cv.imread('Computer_Vision\Tests\Segmentation_tests\photos\_fruit.jpg')
cv.imshow('Image',img)

thresh_seg(img=img)

cv.waitKey(0)
cv.destroyAllWindows()