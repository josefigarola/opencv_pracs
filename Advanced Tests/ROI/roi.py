import cv2 as cv
import numpy as np

if __name__ == '__main__' :

    # Read image
    img = cv.imread("Computer_Vision\Tests\ROI\_ramo.jpg")

    # Select ROI
    showCrosshair = False
    fromCenter = False
    r = cv.selectROI("Image", img, fromCenter, showCrosshair)
    # Crop image
    imgCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    cv.imwrite(r"Computer_Vision\Tests\ROI\Cropramo.jpg", imgCrop)

    # Display cropped image
    cv.imshow("Image", imgCrop)
    cv.waitKey(0)